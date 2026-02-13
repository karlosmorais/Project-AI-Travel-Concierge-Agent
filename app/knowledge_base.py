# app/knowledge_base.py
import asyncio
from typing import Dict, Any, List
from app.rag.retriever import retrieve
from app.main import create_kernel

def search_card_benefits(card_name: str, category: str) -> List[Dict[str, Any]]:
    """
    Search knowledge base for card benefits.
    """
    try:
        kernel = create_kernel()
        query = f"{card_name} benefits for {category}"
        results = asyncio.run(retrieve(kernel, query))
        return results
    except Exception as e:
        print(f"Error searching knowledge base: {e}")
        return []

def get_card_recommendation(mcc: str, country: str) -> Dict[str, Any]:
    """
    Get card recommendation from knowledge base.
    """
    # Placeholder
    return {
        "card": "BankGold",
        "benefit": "4x points on dining",
        "source": "Knowledge Base"
    }