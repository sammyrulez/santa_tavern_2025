"""StoryWeaver: agente per la generazione della struttura narrativa."""

from datapizza.agents import Agent
from typing import List
from santas_tavern.models import json_schema
import  json



def create_story_weaver_agent(client, sqad: List[Agent]):
    """
    Crea l'agente StoryWeaver per la generazione della storia.
    """
    system_prompt = (
        "Sei un Dungeon Master esperto di D&D 5e. "
        "Crea una avventura natalizia in 3 atti, con titolo, pitch, sinossi, atti e scene. "
        "Gli Atti devono essere collegati a incontri D&D generati da altri agenti e devono essere esattamente tre ",
        "Il titolo dell'atto non deve contentere numeri. ",
        "Ogni atto deve avere nome, descrizione e scene con descrizione e riferimenti agli incontri. "
        "Includi una lista di NPC rilevanti.",
        "Includi statistiche per i mostri da affrontare rilevanti.",
        "Usa le seguenti risorse a tua disposizione per arricchire la storia: "+ ", ".join([helper.name for helper in sqad]) + ". ",
        "Restituisci l'avventura in formato JSON conforme al seguente schema: " + json.dumps(json_schema, indent=2) + " \n Rispetta scripolosamente la struttura e i valori delle enum indicate nello schema!"
    )
    agent = Agent(name="StoryWeaver", client=client,
    system_prompt="\n".join(system_prompt), )

    for helper in sqad:
        agent.can_call(helper)
    return agent

