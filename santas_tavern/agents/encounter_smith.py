"""EncounterSmith: agente per la generazione degli incontri."""
from datapizza.agents import Agent
from santas_tavern.tools.monsters import find_monsters_by_challenge_rating

from santas_tavern.config import get_openai_client

def create_encounter_smith_agent(client):
    """
    Crea l'agente EncounterSmith per la generazione degli incontri.
    """
    system_prompt = (
        "Sei un designer di incontri per D&D 5e. "
        "Genera una lista di incontri (combattimento, sociali, esplorazione, puzzle) "
        "per la storia fornita, con id, tipo, descrizione, difficoltà suggerita e note."
        "specifica i mostri coinvolti con nome, quantità e stat block in formato tabella markdown."
        "il risultato deve essere in formato in testo , senza includere riferimenti a JSON, Python o altri formati."
    )
    return Agent(
        name="EncounterSmith",
        client=client,
        system_prompt=system_prompt,
        tools=[find_monsters_by_challenge_rating]
    )

"""client = get_openai_client()

agent = create_encounter_smith_agent(client)
res = agent.run("Il nostro eroe netra nella tana di un Orco con CR 0.5 e un Goblin con CR 0.25.")
print(res.text)"""

