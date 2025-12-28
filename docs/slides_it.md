# Santa's Tavern of Quests – Slide del Progetto

---

## Slide 1: Introduzione
- Santa's Tavern of Quests è un generatore AI di avventure one-shot per D&D a tema natalizio.
- Crea istantaneamente un'avventura completa: trama, incontri, PNG, tesori e scheda stampabile per il GM.
- Basato sul framework multi-agente `datapizza-ai`.

---

## Slide 2: Obiettivi del Progetto
- Aiutare i Dungeon Master a gestire sessioni di D&D natalizie con preparazione minima.
- Generare storia, incontri, oggetti magici e lore su misura per il party.
- Garantire avventure divertenti, bilanciate e tematicamente coerenti.

---

## Slide 3: Architettura degli Agenti
- **SantaDMPlanner**: Orchestratore del processo di generazione e coordinatore degli agenti.
- **StoryWeaver**: Crea la narrazione principale e la struttura dell'avventura.
- **EncounterSmith**: Progetta incontri di combattimento, sociali e enigmi bilanciati.
- **LootElf**: Genera oggetti magici a tema natalizio.
- **LoreKeeper**: (Opzionale, RAG) Mantiene la coerenza narrativa e gli elementi ricorrenti.
- **RulesAndSafetyElf**: Controlla le regole e assicura che il tono sia adatto al pubblico.

---

## Slide 4: Funzionalità Principali
- Generazione automatica di pacchetti avventura in formato JSON.
- Integrazione con API D&D 5e per mostri e dati.
- Controllo del tono (accogliente, epico, dark, per famiglie).
- Esportazione in markdown/HTML per la stampa.

---

## Slide 5: Tool Principali
- **Monster Finder Tool**: Trova mostri per Grado di Sfida tramite l'API D&D 5e.
- **Lore Tool**: Basato su RAG, mantiene la coerenza narrativa e suggerisce elementi ricorrenti.
- I tool sono modulari e riutilizzabili dagli agenti.

---

## Slide 6: Stack Tecnologico e Automazione
- Python 3.10–3.12, framework `datapizza-ai`.
- Gestione dipendenze con `pip` e `uv`.
- Linting e auto-fix con `ruff`.
- Test automatizzati con `pytest`.
- Pre-commit hook per qualità del codice e aggiornamento dipendenze.

