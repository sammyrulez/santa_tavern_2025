"""SantaDMPlanner: orchestratore principale per la generazione dell'avventura."""

from santas_tavern.models import (
    AdventureGenerationParams, AdventurePacket, Act, Encounter, NPC, MagicItem
)
from santas_tavern.agents.story_weaver import create_story_weaver_agent
from santas_tavern.agents.encounter_smith import create_encounter_smith_agent
from santas_tavern.agents.loot_elf import create_loot_elf_agent
from santas_tavern.agents.lore_keeper import create_lore_keeper_agent
from santas_tavern.agents.rules_safety_elf import create_rules_safety_elf_agent


def create_planner_agent(client):
    """Restituisce una funzione di orchestrazione per la generazione dell'avventura."""

    story_weaver = create_story_weaver_agent(client)
    encounter_smith = create_encounter_smith_agent(client)
    loot_elf = create_loot_elf_agent(client)
    lore_keeper = create_lore_keeper_agent(client)
    rules_safety_elf = create_rules_safety_elf_agent(client)

    def generate_adventure(params: AdventureGenerationParams) -> AdventurePacket:
        # Step 1: Genera la struttura della storia
        story = story_weaver.run(params.model_dump())
        # Step 2: Genera gli incontri
        encounters = encounter_smith.run({
            "party_level": params.party_level,
            "party_size": params.party_size,
            "tone": params.tone,
            "acts": story["acts"]
        })
        # Step 3: Genera gli oggetti magici
        magic_items = loot_elf.run({
            "party_level": params.party_level,
            "acts": story["acts"]
        })
        # Step 4: Genera NPC
        npcs = story.get("npcs", [])
        # Step 5: Aggiungi note di lore
        lore_notes = lore_keeper.run({
            "story": story,
            "encounters": encounters,
            "magic_items": magic_items
        })
        # Step 6: Assembla il pacchetto avventura
        packet = AdventurePacket(
            title=story["title"],
            pitch=story["pitch"],
            synopsis=story["synopsis"],
            tone=params.tone,
            acts=[Act(**a) for a in story["acts"]],
            encounters=[Encounter(**e) for e in encounters],
            npcs=[NPC(**n) for n in npcs],
            magic_items=[MagicItem(**m) for m in magic_items],
            lore_notes=lore_notes,
            gm_notes=story.get("gm_notes")
        )
        # Step 7: Passaggio finale di revisione
        final_packet = rules_safety_elf.run(packet.model_dump())
        return AdventurePacket(**final_packet)

    return generate_adventure

