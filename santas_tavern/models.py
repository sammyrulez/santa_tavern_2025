"""Modelli Pydantic per Santa's Tavern of Quests."""

from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from enum import Enum

class EncounterType(str, Enum):
    COMBAT = "combat"
    SOCIAL = "social"
    EXPLORATION = "exploration"
    PUZZLE = "puzzle"

class EncounterDifficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class MagicItemRarity(str, Enum):
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    VERY_RARE = "very_rare"

class Scene(BaseModel):
    """Descrizione di una scena all'interno di un atto."""
    name: str
    description: str
    encounter_ids: List[str] = Field(default_factory=list)

class Encounter(BaseModel):
    """Un incontro D&D generato dall'agente EncounterSmith."""
    id: str
    type: EncounterType
    description: str
    difficulty: EncounterDifficulty
    party_level: int
    party_size: int
    notes: Optional[str] = None

class NPC(BaseModel):
    """Personaggio non giocante."""
    name: str
    role: str
    personality: str

class MagicItem(BaseModel):
    """Oggetto magico natalizio."""
    id: str
    name: str
    rarity: MagicItemRarity
    effect_text: str
    flavor: Optional[str] = None

class Act(BaseModel):
    """Un atto della storia."""
    name: str
    description: str
    scenes: List[Scene]

class AdventurePacket(BaseModel):
    """Pacchetto avventura completo per il DM."""
    title: str
    pitch: str
    synopsis: str
    tone: str
    acts: List[Act]
    encounters: List[Encounter]
    npcs: List[NPC]
    magic_items: List[MagicItem]
    lore_notes: Optional[str] = None
    gm_notes: Optional[str] = None

class AdventureGenerationParams(BaseModel):
    """Parametri di input per la generazione dell'avventura."""
    party_level: int
    party_size: int
    tone: str = "cozy"
    duration_hours: float = 3.0

json_schema ={
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "AdventurePacket",
  "type": "object",
  "properties": {
    "title": {
      "type": "string",
      "description": "Titolo dell'avventura."
    },
    "pitch": {
      "type": "string",
      "description": "Pitch in una frase."
    },
    "synopsis": {
      "type": "string",
      "description": "Sinossi dell'avventura."
    },
    "tone": {
      "type": "string",
      "description": "Tono dell'avventura."
    },
    "acts": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": { "type": "string" },
          "description": { "type": "string" },
          "scenes": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": { "type": "string" },
                "description": { "type": "string" },
                "encounter_ids": {
                  "type": "array",
                  "items": { "type": "string" }
                }
              },
              "required": ["name", "description", "encounter_ids"]
            }
          }
        },
        "required": ["name", "description", "scenes"]
      }
    },
    "encounters": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "type": {
            "type": "string",
            "enum": ["combat", "social", "exploration"]
          },
          "description": { "type": "string" },
          "difficulty": {
            "type": "string",
            "enum": ["easy", "medium", "hard"]
          },
          "party_level": { "type": "integer" },
          "party_size": { "type": "integer" },
          "notes": { "type": ["string", "null"] }
        },
        "required": ["id", "type", "description", "difficulty", "party_level", "party_size"]
      }
    },
    "npcs": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": { "type": "string" },
          "role": { "type": "string" },
          "personality": { "type": "string" }
        },
        "required": ["name", "role", "personality"]
      }
    },
    "magic_items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": { "type": "string" },
          "name": { "type": "string" },
          "rarity": {
            "type": "string",
            "enum": ["common", "uncommon", "rare", "very_rare"]
          },
          "effect_text": { "type": "string" },
          "flavor": { "type": ["string", "null"] }
        },
        "required": ["id", "name", "rarity", "effect_text"]
      }
    },
    "lore_notes": {
      "type": ["string", "null"],
      "description": "Note di lore opzionali."
    },
    "gm_notes": {
      "type": ["string", "null"],
      "description": "Note opzionali per il GM."
    }
  },
  "required": [
    "title",
    "pitch",
    "synopsis",
    "tone",
    "acts",
    "encounters",
    "npcs",
    "magic_items"
  ]
}

