"""Gestione della configurazione e client OpenAI per Santa's Tavern."""

import os
from datapizza.clients.openai import OpenAIClient
from datapizza.embedders.openai import OpenAIEmbedder


EMBEDDING_MODEL_NAME = "text-embedding-3-small"


def get_openai_client() -> OpenAIClient:
    """
    Restituisce un client OpenAI configurato per datapizza-ai.
    Solleva un'eccezione se la chiave API non è presente.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY non trovato nelle variabili d'ambiente. "
            "Impostalo per poter utilizzare Santa's Tavern."
        )
    model_name = os.getenv("MODEL_NAME", "gpt-5.1")
    return OpenAIClient(api_key=api_key, model=model_name)


def get_openai_embedding_client() -> OpenAIEmbedder:
    """
    Restituisce un client OpenAI configurato per le embedding.
    Solleva un'eccezione se la chiave API non è presente.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY non trovato nelle variabili d'ambiente. "
            "Impostalo per poter utilizzare Santa's Tavern."
        )
    embedding_model_name = os.getenv("EMBEDDING_MODEL_NAME", EMBEDDING_MODEL_NAME)
    return OpenAIEmbedder(api_key=api_key, model_name=embedding_model_name)
