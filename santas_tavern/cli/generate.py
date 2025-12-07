"""CLI per generare una avventura natalizia D&D."""

import argparse
import os
import json
from santas_tavern.config import get_openai_client
from santas_tavern.models import AdventureGenerationParams, AdventurePacket, EncounterType, EncounterDifficulty
from santas_tavern.agents.planner import create_planner_agent

def _translate_encounter_type(enc_type:EncounterType) -> str :
    """Traduci EncounterType in italiano."""
    translations = {
        EncounterType.COMBAT: "Combattimento",
        EncounterType.PUZZLE: "Enigma",
        EncounterType.EXPLORATION: "Esplorazione",
        EncounterType.SOCIAL: "Interazione Sociale",
    }
    return translations.get(enc_type, "Sconosciuto")

def _translate_encounter_difficulty(difficulty: EncounterDifficulty) -> str:
    """Traduci EncounterDifficulty in italiano."""
    translations = {
        EncounterDifficulty.EASY: "Facile",
        EncounterDifficulty.MEDIUM: "Media",
        EncounterDifficulty.HARD: "Difficile",
    }
    return translations.get(difficulty, "Sconosciuto")


def format_adventure_markdown(packet) -> str:
    """Formatta il pacchetto avventura in markdown leggibile per il GM."""
    md = f"# {packet.title}\n\n"
    md += f"**Pitch:** {packet.pitch}\n\n"
    md += f"**Sinossi:** {packet.synopsis}\n\n"
    md += f"**Tono:** {packet.tone}\n\n"
    md += "## Struttura della storia\n"
    for i, act in enumerate(packet.acts, 1):
        md += f"### Atto {i}: {act.name}\n{act.description}\n"
        for scene in act.scenes:
            md += f"#### Scena: {scene.name}\n  {scene.description}\n"
            if scene.encounter_ids:
                md += "\n##### Incontri\n"
                for enc in [ enc for enc in packet.encounters if enc.id in scene.encounter_ids ]:
                    md += f"- [{_translate_encounter_type(enc.type)}] {enc.description} (Difficoltà: {_translate_encounter_difficulty(enc.difficulty)})\n"
                    if enc.stat_blocks:
                        md += "  - Stat Blocks:\n" + enc.stat_blocks + "\n---\n"

    md += "\n## NPC\n"
    for npc in packet.npcs:
        md += f"- {npc.name} ({npc.role}): {npc.personality}\n"
    md += "\n## Oggetti Magici\n"
    for item in packet.magic_items:
        md += f"- {item.name} ({item.rarity}): {item.effect_text}\n"
        if item.flavor:
            md += f"  _{item.flavor}_\n"
    if packet.lore_notes:
        md += f"\n## Note di Lore\n{packet.lore_notes}\n"
    if packet.gm_notes:
        md += f"\n## Note per il GM\n{packet.gm_notes}\n"
    return md


def main():
    parser = argparse.ArgumentParser(
        description="Genera una one-shot natalizia D&D con Santa's Tavern."
    )
    parser.add_argument("--party-level", type=int, required=True, help="Livello del party")
    parser.add_argument("--party-size", type=int, required=True, help="Numero di giocatori")
    parser.add_argument("--tone", type=str, default="cozy", help="Tono dell'avventura")
    parser.add_argument("--duration-hours", type=float, default=3, help="Durata in ore")
    parser.add_argument("--output-dir", type=str, default="./output", help="Directory di output")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    client = get_openai_client()
    planner = create_planner_agent(client)
    params = AdventureGenerationParams(
        party_level=args.party_level,
        party_size=args.party_size,
        tone=args.tone,
        duration_hours=args.duration_hours
    )
    #packet = planner(params)

    json_path = os.path.join(args.output_dir, "adventure_packet.json")
    md_path = os.path.join(args.output_dir, "adventure_notes.md")
    #with open(json_path, "w", encoding="utf-8") as f:
    #    f.write(packet.model_dump_json(indent=2))
    with open(json_path, "r") as f:
        packet =  AdventurePacket.model_validate_json(f.read())
        with open(md_path, "w", encoding="utf-8") as f:
                f.write(format_adventure_markdown(packet))

    print(f"Avventura generata:\n- {json_path}\n- {md_path}")

if __name__ == "__main__":
    main()

