"""Gestione della configurazione e client OpenAI per Santa's Tavern."""

import os
from datapizza.clients.openai import  OpenAIClient


def get_openai_client() -> OpenAIClient:
    """
    Restituisce un client OpenAI configurato per datapizza-ai.
    Solleva un'eccezione se la chiave API non è presente.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY non trovato nelle variabili d'ambiente. "
            "Impostalo per poter utilizzare Santa's Tavern."
        )
    model_name = os.getenv("MODEL_NAME", "gpt-4.1-mini")
    return OpenAIClient(api_key=api_key, model=model_name)

