"""EncounterSmith: agente per la generazione degli incontri."""
from datapizza.agents import Agent

def create_encounter_smith_agent(client):
    """
    Crea l'agente EncounterSmith per la generazione degli incontri.
    """
    system_prompt = (
        "Sei un designer di incontri per D&D 5e. "
        "Genera una lista di incontri (combattimento, sociali, esplorazione/puzzle) "
        "per la storia fornita, con id, tipo, descrizione, difficoltà suggerita e note."
    )
    return Agent(
        name="EncounterSmith",
        client=client,
        system_prompt=system_prompt
    )

