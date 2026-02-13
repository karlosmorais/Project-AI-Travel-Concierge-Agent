import os
import asyncio
from semantic_kernel.connectors.ai.open_ai import AzureTextEmbedding
from azure.cosmos import CosmosClient, PartitionKey
from typing import List
import uuid

async def embed_texts(texts: List[str], kernel) -> List[List[float]]:
    """
    Generate embeddings for a list of texts using Semantic Kernel's AzureTextEmbedding.
    """
    # Assuming kernel has the embedding service registered
    # If not passed, we might need to instantate it here or pass the service directly
    # Ideally, we should use the service from the kernel
    
    service_id = "embedding" # We'll name it this in main.py
    embedding_gen = kernel.get_service(service_id)
    
    embeddings = await embedding_gen.generate_embeddings(texts)
    # Ensure it's a list for JSON serialization
    import numpy as np
    if isinstance(embeddings, np.ndarray):
        embeddings = embeddings.tolist()
    elif isinstance(embeddings, list) and len(embeddings) > 0 and isinstance(embeddings[0], np.ndarray):
        embeddings = [e.tolist() for e in embeddings]
        
    return embeddings

def get_cosmos_container():
    """Get the Cosmos DB container client."""
    url = os.environ.get("COSMOS_ENDPOINT")
    key = os.environ.get("COSMOS_KEY")
    database_name = os.environ.get("COSMOS_DB")
    container_name = os.environ.get("COSMOS_CONTAINER")
    
    client = CosmosClient(url, credential=key)
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)
    return container

async def upsert_snippet(kernel, content: str, source: str):
    """
    Generate embedding and store snippet in Cosmos DB.
    """
    # 1. Generate embedding
    embeddings = await embed_texts([content], kernel)
    vector = embeddings[0]
    
    # 2. Prepare item
    item = {
        "id": str(uuid.uuid4()),
        "content": content,
        "source": source,
        "vector": vector,
        "pk": "knowledge" # Partition key
    }
    
    # 3. Upsert to Cosmos DB
    container = get_cosmos_container()
    container.upsert_item(item)
    print(f"Upserted item from {source}")