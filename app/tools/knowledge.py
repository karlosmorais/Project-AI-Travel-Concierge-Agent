from semantic_kernel.functions import kernel_function
from app.rag.retriever import retrieve
import json

class KnowledgeTools:
    def __init__(self, kernel):
        self.kernel = kernel

    @kernel_function(name="search_knowledge", description="Search internal knowledge base for policies and card info.")
    async def search_knowledge(self, query: str) -> str:
        """
        Search the RAG knowledge base for information.
        """
        try:
            results = await retrieve(self.kernel, query)
            return json.dumps(results)
        except Exception as e:
            return json.dumps({"error": str(e)})