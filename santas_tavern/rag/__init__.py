from pathlib import Path


from datapizza.embedders import ChunkEmbedder
from datapizza.modules.parsers.docling import DoclingParser
from datapizza.modules.splitters import NodeSplitter
from datapizza.pipeline import IngestionPipeline
from datapizza.clients.openai import OpenAIClient
from datapizza.core.vectorstore import VectorConfig
from datapizza.embedders.openai import OpenAIEmbedder
from datapizza.modules.prompt import ChatPromptTemplate
from datapizza.modules.rewriters import ToolRewriter
from datapizza.pipeline import DagPipeline
from datapizza.vectorstores.qdrant import QdrantVectorstore


from santas_tavern.config import (
    get_openai_embedding_client,
    EMBEDDING_MODEL_NAME,
    get_openai_client,
)

COLLECTION_NAME = "my_lore"

vectorstore = QdrantVectorstore(location=":memory:")
vectorstore.create_collection(
    COLLECTION_NAME,
    vector_config=[VectorConfig(name=EMBEDDING_MODEL_NAME, dimensions=1536)],
)

embedder_client: OpenAIEmbedder = get_openai_embedding_client()
openai_client: OpenAIClient = get_openai_client()

ingestion_pipeline = IngestionPipeline(
    modules=[
        DoclingParser(),
        NodeSplitter(max_char=1000),  # Split Nodes into Chunks
        ChunkEmbedder(client=embedder_client),  # Add embeddings to Chunks
    ],
    vector_store=vectorstore,
    collection_name=COLLECTION_NAME,
)


query_rewriter = ToolRewriter(
    client=openai_client,
    system_prompt="Estrai elementi significativi dalla domanda dell'utente per migliorare il recupero delle informazioni.",
    max_rewrite_steps=2,
)


# Use the same qdrant of ingestion (prefer host and port instead of location when possible)
retriever = QdrantVectorstore(location=":memory:")
retriever.create_collection(
    COLLECTION_NAME, vector_config=[VectorConfig(name="embedding", dimensions=1536)]
)

prompt_template = ChatPromptTemplate(
    user_prompt_template="Domanda dell'utente: {{user_prompt}}\n:",
    retrieval_prompt_template="Estrai il contenuto:\n{% for chunk in chunks %}{{ chunk.text }}\n{% endfor %}",
)

dag_pipeline = DagPipeline()
dag_pipeline.add_module("rewriter", query_rewriter)
dag_pipeline.add_module("embedder", embedder_client)
dag_pipeline.add_module("retriever", retriever)
dag_pipeline.add_module("prompt", prompt_template)
dag_pipeline.add_module("generator", openai_client)

dag_pipeline.connect("rewriter", "embedder", target_key="text")
dag_pipeline.connect("embedder", "retriever", target_key="query_vector")
dag_pipeline.connect("retriever", "prompt", target_key="chunks")
dag_pipeline.connect("prompt", "generator", target_key="memory")


def run_import_pipeline(input_dir: str) -> None:
    input_path = Path(input_dir)
    files = [str(p.absolute()) for p in list(input_path.iterdir())]
    ingestion_pipeline.run(files, metadata={"source": "user_upload"})


def run_query_pipeline(user_prompt: str) -> str:
    result = dag_pipeline.run({"user_prompt": user_prompt})
    return result["generator"].text
