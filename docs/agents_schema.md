# Schema di funzionamento degli agenti – Santa's Tavern of Quests

```mermaid
flowchart TD
    Start([Start])
    Planner[SantaDMPlanner\n(Orchestrator)]
    Story[StoryWeaver\n(Narrative)]
    Encounter[EncounterSmith\n(Encounters)]
    Loot[LootElf\n(Loot)]
    Lore[LoreKeeper\n(Lore, RAG)]
    Rules[RulesAndSafetyElf\n(Rules & Safety)]
    Output([Output Adventure Packet])

    Start --> Planner
    Planner --> Story
    Planner --> Encounter
    Planner --> Loot
    Planner --> Lore
    Planner --> Rules
    Story --> Output
    Encounter --> Output
    Loot --> Output
    Lore --> Output
    Rules --> Output
```

## Descrizione
- **SantaDMPlanner**: coordina il flusso e attiva gli altri agenti.
- **StoryWeaver**: genera la narrazione principale.
- **EncounterSmith**: crea incontri bilanciati.
- **LootElf**: produce oggetti magici a tema.
- **LoreKeeper**: mantiene la coerenza narrativa (opzionale, RAG).
- **RulesAndSafetyElf**: verifica regole e tono.
- Tutti gli agenti contribuiscono al pacchetto finale dell'avventura.

