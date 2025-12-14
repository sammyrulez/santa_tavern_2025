from santas_tavern.config import get_openai_client
from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient
from pydantic import BaseModel


class Verdict(BaseModel):
    result: bool
    feedback: str


def llm_as_a_judge(adventure_text: str) -> Verdict:
    client: OpenAIClient = get_openai_client()
    agent = Agent(
        name="judge-agent",
        system_prompt=f"""Sei un DM esperto che deve valutare le avventure generate da un altro agente. Fornisci feedback costruttivo e suggerimenti per migliorare la trama, i personaggi e gli incontri.
                       Valuta anche la coerenza interna e l'aderenza al tema natalizio.
                       Valuta gli incontri che siano bilanciati per il livello del party e che offrano varietà e sfide interessanti.
                       Gli oggetti magici devono essere tematici e non eccessivamente potenti
                       Controlla la coerenza delle regole D&D e l'allineamento del tono.
                       Il feedback deve essere estremamente conciso e puntuale.
                       Fornisci il tuo giudizio in formato JSON con i campi 'result' (booleano) e 'feedback' (stringa).\n
                    
                        {str(Verdict.model_json_schema())} """,
        client=client,
        max_steps=5,
    )

    res = agent.run(adventure_text)
    verdict = res.text.replace("```json", " ").replace("```", " ")
    return Verdict.model_validate_json(verdict)
