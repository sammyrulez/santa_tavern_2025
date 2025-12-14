"""RulesAndSafetyElf: agente per la revisione e la coerenza dell'avventura."""

from datapizza.agents import Agent


def create_rules_safety_elf_agent(client):
    """
    Crea l'agente RulesAndSafetyElf per la revisione finale dell'avventura.
    """
    system_prompt = (
        "Controlla la coerenza delle regole D&D e l'allineamento del tono. "
        "Se il tono è 'kids', evita elementi horror. "
        "Restituisci una versione raffinata del pacchetto avventura."
    )
    return Agent(name="RulesAndSafetyElf", client=client, system_prompt=system_prompt)
