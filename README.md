# Santa's Tavern of Quests 🎄🧙‍♂️

Agentic D&D one-shot generator for cozy Christmas sessions, built with [`datapizza-ai`](https://github.com/datapizza-labs/datapizza-ai).

> Turn a few campaign parameters into a complete, ready-to-run Christmas adventure: plot, encounters, NPCs, magic loot, and a printable GM sheet.

---

## 🎯 Project Overview

**Santa's Tavern of Quests** is an AI-powered assistant for Dungeon Masters who want to run a **Christmas-themed Dungeons & Dragons one-shot** without spending hours in prep.

It uses the `datapizza-ai` framework to orchestrate multiple specialized agents that collaborate to:

- Design a Christmas D&D story adapted to your party  
- Build a sequence of scenes and encounters  
- Create balanced combat/social/puzzle encounters  
- Forge thematic magic items (candy canes, cursed stockings, flying sleighs…)  
- Keep lore consistent across multiple adventures  
- Produce a final, structured “Adventure Packet” ready for the table

This project is designed as a submission for the **Datapizza Christmas AI Challenge 2025**.

---

## ✨ Core Features

- **Multi-agent architecture using `datapizza-ai`**  
  - Agents with clear, focused responsibilities coordinated by a planner agent. :contentReference[oaicite:0]{index=0}  

- **Adventure Packet generation**
  - Plot hook, 3-act structure, key scenes
  - NPCs, factions, locations (villages, toy factories, polar citadels…)
  - Mix of combat / social / exploration / puzzle encounters
  - Thematic loot and rewards

- **Christmas + D&D theming**
  - Friendly or mysterious Santa-like figures
  - Elves, toy golems, winter spirits, Krampus-style antagonists
  - Tone control: from cozy & family-friendly to darker winter fantasy

- **JSON-first design**
  - Output is a well-defined JSON schema (easy to reuse in tools, VTTs, or UIs)
  - Optional markdown/HTML export for a printable GM handout

- **Optional RAG for campaign continuity**
  - Plug in past adventures / notes so the system can reuse NPCs, locations, and traditions  
  - Uses Datapizza’s RAG components (parsers, splitters, vectorstore) for retrieval. :contentReference[oaicite:1]{index=1}  

---

## 🧩 Agent Architecture

The system is built around several collaborating agents:

### 1. `SantaDMPlanner` (orchestrator)

- Main entrypoint for user requests
- Interacts with the user (CLI / API)
- Delegates work to the specialist agents
- Assembles the final **Adventure Packet** response

### 2. `StoryWeaver` – Bardo del Solstizio

- Generates the **core narrative**:
  - campaign pitch
  - 3-act structure
  - main conflict & resolutions
- Adapts tone (cozy / epic / dark / kids-friendly)

### 3. `EncounterSmith` – Forgiatore di Incontri

- Designs **balanced encounters** based on:
  - party size
  - party level
  - preferred difficulty
- Produces mixture of:
  - combat scenes
  - social scenes
  - exploration / puzzle moments

### 4. `LootElf` – Artigiano di Doni Magici

- Creates **Christmas-themed magic items**, e.g.:
  - Candy Cane Blade (cold-flavored weapon)
  - Silent Sleigh of the North Wind
  - Cursed stockings for darker campaigns

### 5. `LoreKeeper` – Cronista del Natale

- (Optional, RAG-powered)  
- Reads previous adventures / notes and suggests:
  - recurring NPCs
  - consistent traditions & locations
  - hooks tying the new one-shot to your existing world

### 6. `RulesAndSafetyElf` – Regole & Tone Guard

- Final refinement pass:
  - checks D&D-style consistency of mechanics (at a high level)
  - nudges tone to match target audience (kids vs adults)

---

## 🏗️ Tech Stack

- **Language**: Python `>= 3.10, < 3.13` :contentReference[oaicite:2]{index=2}  
- **Framework**: [`datapizza-ai`](https://github.com/datapizza-labs/datapizza-ai) (agents, tools, RAG)
- **LLM Provider**: OpenAI by default, easily swappable
- **Vector Store (optional)**: Qdrant or other vector backend supported via Datapizza RAG abstractions :contentReference[oaicite:3]{index=3}  

---

## 🚀 Getting Started

### 1. Prerequisites

- Python `3.10`–`3.12`
- An API key for a supported LLM (e.g. OpenAI)
- (Optional) A running Qdrant instance or cloud account for RAG

### 2. Installation

```bash
git clone https://github.com/<your-username>/santas-tavern-of-quests.git
cd santas-tavern-of-quests

python -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate

pip install -r requirements.txt
# datapizza-ai is installed via requirements, or:
# pip install datapizza-ai
