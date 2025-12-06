"""EncounterSmith: agente per la generazione degli incontri."""
from datapizza.agents import Agent
from santas_tavern.tools.monsters import find_monsters_by_challenge_rating

def create_encounter_smith_agent(client):
    """
    Crea l'agente EncounterSmith per la generazione degli incontri.
    """
    system_prompt = (
        "Sei un designer di incontri per D&D 5e. "
        "Genera una lista di incontri (combattimento, sociali, esplorazione, puzzle) "
        "per la storia fornita, con id, tipo, descrizione, difficoltà suggerita e note."
        "se gli incontri includono combattimenti, specifica i mostri coinvolti con nome, quantità e stat block in formato markdown."
        "il risultato deve essere in formato in testo , senza includere riferimenti a JSON, Python o altri formati."
    )
    return Agent(
        name="EncounterSmith",
        client=client,
        system_prompt=system_prompt,
        tools=[find_monsters_by_challenge_rating]
    )

