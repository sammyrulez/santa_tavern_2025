from datapizza.tools import tool
from santas_tavern.rag import run_query_pipeline


@tool(
    name="get_elements_from_characters_background",
    description="Estrai elementi significativi riguardo al background personaggi,  dai documenti. In particolare luoghi e eventi legati al passato e alla professione.",
)
def get_elements_from_characters_background(
    question_about_character_background: str,
) -> str:
    print("question_about_character_background", question_about_character_background)
    pipeline_result = run_query_pipeline(question_about_character_background)
    print(pipeline_result)
    return pipeline_result
