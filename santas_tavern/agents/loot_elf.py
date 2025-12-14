"""LootElf: agente per la generazione di oggetti magici natalizi."""

from datapizza.agents import Agent


def create_loot_elf_agent(client):
    """
    Crea l'agente LootElf per la generazione di oggetti magici natalizi.
    """
    system_prompt = (
        "Sei un elfo magico che crea oggetti magici natalizi per D&D 5e. "
        "Genera una lista di oggetti magici con nome, rarità, effetto e breve descrizione."
    )
    return Agent(name="LootElf", client=client, system_prompt=system_prompt)
