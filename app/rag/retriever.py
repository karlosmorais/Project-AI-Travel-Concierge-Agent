import os
from typing import List, Dict
from azure.cosmos import CosmosClient

async def retrieve(kernel, query: str, top_k: int = 3) -> List[Dict]:
    """
    Retrieve relevant snippets from Cosmos DB using vector similarity.
    """
    # 1. Generate query embedding
    service_id = "embedding"
    embedding_gen = kernel.get_service(service_id)
    embeddings = await embedding_gen.generate_embeddings([query])
    query_vector = embeddings[0]
    
    # Ensure list for Cosmos DB param
    import numpy as np
    if isinstance(query_vector, np.ndarray):
        query_vector = query_vector.tolist()
    elif hasattr(query_vector, "tolist"): # specific to some SK types
        query_vector = query_vector.tolist()
    
    # 2. Setup Cosmos DB client
    url = os.environ.get("COSMOS_ENDPOINT")
    key = os.environ.get("COSMOS_KEY")
    database_name = os.environ.get("COSMOS_DB")
    container_name = os.environ.get("COSMOS_CONTAINER")
    
    client = CosmosClient(url, credential=key)
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)
    
    # 3. Execute Vector Search
    # Note: Cosmos DB NoSQL vector search syntax might vary slightly based on preview version
    # Standard syntax: SELECT c.content, c.source, VectorDistance(c.vector, @embedding) AS score FROM c ...
    
    sql_query = """
    SELECT TOP @top_k c.content, c.source, VectorDistance(c.vector, @embedding) AS score
    FROM c
    ORDER BY VectorDistance(c.vector, @embedding)
    """
    
    parameters = [
        {"name": "@top_k", "value": top_k},
        {"name": "@embedding", "value": query_vector}
    ]
    
    items = list(container.query_items(
        query=sql_query,
        parameters=parameters,
        enable_cross_partition_query=True
    ))
    
    return items