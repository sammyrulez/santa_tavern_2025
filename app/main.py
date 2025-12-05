import  os

from datapizza.clients.openai import OpenAIClient
from datapizza.agents import Agent


client = OpenAIClient(
    api_key=os.environ["OPENAI_API_KEY"],
    model="gpt-4.1-mini",  # o quello che preferisci
)

story_agent = Agent(
    name="story_weaver",
    client=client,
    system_prompt=(
        "Sei un Dungeon Master esperto di D&D 5e. "
        "Crei one-shot a tema natalizio, con atmosfera fantasy."
    ),
)

encounter_agent = Agent(
    name="encounter_smith",
    client=client,
    system_prompt=(
        "Sei un game designer di D&D 5e. "
        "Generi incontri bilanciati per il party usando solo testo."
    ),
)

loot_agent = Agent(
    name="loot_elf",
    client=client,
    system_prompt=(
        "Sei un artigiano di magia. Crea oggetti magici "
        "a tema Natale, bilanciati per il livello indicato."
    ),
)

planner_agent = Agent(
    name="santa_dm_planner",
    client=client,
    system_prompt=(
        "Coordini altri agent per costruire una one-shot di D&D "
        "a tema natalizio. Devi restituire un JSON ben strutturato "
        "con trama, scene, incontri e loot."
    ),
)

# Il planner può chiamare gli altri agent
planner_agent.can_call([story_agent, encounter_agent, loot_agent])
