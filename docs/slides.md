# Santa's Tavern of Quests 

---

## Introduction
- Santa's Tavern of Quests is an AI-powered generator for D&D one-shots with a cozy Christmas theme.
- Instantly creates a full adventure: plot, encounters, NPCs, loot, and printable GM sheet.
- Built on the `datapizza-ai` multi-agent framework.

---

## Project Goals
- Help Dungeon Masters run Christmas-themed D&D sessions with minimal prep.
- Generate story, encounters, magic items, and lore tailored to the party.
- Ensure adventures are fun, balanced, and thematically consistent.

---

##  Agent Architecture
- **SantaDMPlanner**: Orchestrates the generation process and coordinates agents.
- **StoryWeaver**: Crafts the main narrative and adventure structure.
- **EncounterSmith**: Designs balanced combat, social, and puzzle encounters.
- **LootElf**: Creates Christmas-themed magic items.
- **LoreKeeper**: (Optional, RAG) Maintains lore consistency and recurring elements.
- **RulesAndSafetyElf**: Checks rules and ensures tone matches the audience.

---

##  Key Features
- Automated generation of adventure packets in JSON format.
- Integration with D&D 5e API for monsters and data.
- Tone control (cozy, epic, dark, family-friendly).
- Export to markdown/HTML for easy printing.

---

##  Main Tools
- **Monster Finder Tool**: Finds monsters by Challenge Rating using the D&D 5e API.
- **Lore Tool**: RAG-powered, maintains narrative consistency and suggests recurring lore.
- Tools are modular and reusable by agents.

---
## Testing with LLMs as a Judge
- Use LLMs to evaluate adventure quality, balance, and thematic consistency.
- Automate feedback loops to refine agent outputs based on LLM assessments.


---

## Tech Stack & Automation
- Python 3.10–3.12, `datapizza-ai` framework.
- Dependency management with `pip` and `uv`.
- Linting and auto-fixing with `ruff`.
- Automated testing with `pytest`.
- Pre-commit hooks for code quality and dependency updates.


