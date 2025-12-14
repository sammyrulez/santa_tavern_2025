"""LoreKeeper: agente stub per aggiungere note di lore."""

from datapizza.agents import Agent


def create_lore_keeper_agent(client):
    """
    Crea l'agente LoreKeeper (stub) per aggiungere note di lore.
    """
    system_prompt = (
        "Aggiungi una breve sezione 'lore_notes' con tradizioni natalizie, NPC ricorrenti o dettagli di ambientazione. "
        "Non serve una ricerca esterna, solo suggerimenti creativi."
    )
    return Agent(name="LoreKeeper", client=client, system_prompt=system_prompt)
