"""SantaDMPlanner: orchestratore principale per la generazione dell'avventura."""
import json

from santas_tavern.models import (
    AdventureGenerationParams, AdventurePacket, Act, Encounter, NPC, MagicItem, EncounterType, EncounterDifficulty
)
from santas_tavern.agents.story_weaver import create_story_weaver_agent
from santas_tavern.agents.encounter_smith import create_encounter_smith_agent
from santas_tavern.agents.loot_elf import create_loot_elf_agent
from santas_tavern.agents.lore_keeper import create_lore_keeper_agent
from santas_tavern.agents.rules_safety_elf import create_rules_safety_elf_agent


def create_planner_agent(client):
    """Restituisce una funzione di orchestrazione per la generazione dell'avventura."""


    encounter_smith = create_encounter_smith_agent(client)
    loot_elf = create_loot_elf_agent(client)
    lore_keeper = create_lore_keeper_agent(client)
    rules_safety_elf = create_rules_safety_elf_agent(client)
    story_weaver = create_story_weaver_agent(client, [encounter_smith, loot_elf, lore_keeper, rules_safety_elf])

    def generate_adventure(params: AdventureGenerationParams) -> AdventurePacket:
        # Step 1: Genera la struttura della storia
        #with open('/Users/sam/projects/santa_tavern_2025/example_story.json', 'r', encoding='utf-8') as f:
        #    story = f.read()
        story = story_weaver.run(f"Crea una avventura natalizia per D&D 5e con il seguente tema: {str(params)}.").text

        packet = AdventurePacket.model_validate_json(story)
        return packet

    return generate_adventure
