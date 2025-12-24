from datapizza.agents import Agent

from santas_tavern.tools.lore import get_elements_from_characters_background


def create_lore_background_agent(client):
    """
    Crea l'agente LoreNBackground per aggiungere note di lore e background specifiche per il setting e i personaggi.
    """

    system_prompt = (
        "Includi elementi di lore e background specifici per i personaggi che utlizzeranno la campagna. "
        "Genera dettagli come tradizioni culturali, riferimenti alla loro storia personale, soprattutto per quello che riguarda la sezione 'adventure hook' "
        "Utilizza gli strumenti a tua disposizione per trovare elementi significativi per rendere l'avventura personalizzata "
    )
    return Agent(
        name="LoreNBackground",
        client=client,
        system_prompt=system_prompt,
        tools=[get_elements_from_characters_background],
    )
