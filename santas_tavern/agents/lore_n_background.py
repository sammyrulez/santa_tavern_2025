from datapizza.agents import Agent


def create_lore_background_agent(client):
    """
    Crea l'agente LoreNBackground per aggiungere note di lore e background specifiche per il setting e i personaggi.
    """
    system_prompt = "Aggiungi una sezione 'lore_and_background' con dettagli di lore, "
    return Agent(name="LoreNBackground", client=client, system_prompt=system_prompt)
