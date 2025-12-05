"""StoryWeaver: agente per la generazione della struttura narrativa."""

from datapizza.agents import Agent

def create_story_weaver_agent(client):
    """
    Crea l'agente StoryWeaver per la generazione della storia.
    """
    system_prompt = (
        "Sei un Dungeon Master esperto di D&D 5e. "
        "Crea una avventura natalizia in 3 atti, con titolo, pitch, sinossi, atti e scene. "
        "Ogni atto deve avere nome, descrizione e scene con descrizione e riferimenti agli incontri. "
        "Includi una lista di NPC rilevanti."
    )
    return Agent(
        name="StoryWeaver",
        client=client,
        system_prompt=system_prompt
    )

