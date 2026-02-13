import os
import uuid
import time
from azure.cosmos import CosmosClient
from typing import Dict, Any, Optional

class LongTermMemory:
    """
    Long-term memory system using Cosmos DB.
    """
    
    def __init__(self, max_memories: int = 1000, importance_threshold: float = 0.5):
        self.container = self._get_container()
        self.max_memories = max_memories
        self.importance_threshold = importance_threshold

    def _get_container(self):
        url = os.environ.get("COSMOS_ENDPOINT")
        key = os.environ.get("COSMOS_KEY")
        database_name = os.environ.get("COSMOS_DB")
        container_name = os.environ.get("COSMOS_CONTAINER")
        
        client = CosmosClient(url, credential=key)
        database = client.get_database_client(database_name)
        return database.get_container_client(container_name)

    def add_memory(self, session_id: str, content: str, memory_type: str = "interaction", importance_score: float = 0.5, tags: list = None):
        """
        Store a memory item in Cosmos DB.
        """
        item = {
            "id": str(uuid.uuid4()),
            "session_id": session_id,
            "content": content,
            "type": memory_type,
            "importance": importance_score,
            "tags": tags or [],
            "timestamp": time.time(),
            "pk": "memory"  # Partition key for user memories
        }
        self.container.upsert_item(item)

    def get_memory(self, session_id: str) -> list:
        """
        Retrieve memories for a session.
        """
        query = "SELECT * FROM c WHERE c.session_id = @session_id AND c.pk = 'memory'"
        parameters = [{"name": "@session_id", "value": session_id}]
        
        items = list(self.container.query_items(
            query=query,
            parameters=parameters,
            enable_cross_partition_query=True
        ))
        
        return items
