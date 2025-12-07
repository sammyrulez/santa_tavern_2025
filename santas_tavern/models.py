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
    stat_blocks: Optional[str] = None  # Stat block in formato tabella markdown

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

json_schema = AdventurePacket.model_json_schema()

