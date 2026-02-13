
import os
import sys
from azure.cosmos import CosmosClient, PartitionKey

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from dotenv import load_dotenv
load_dotenv()

def setup_cosmos():
    print("🚀 Initializing Cosmos DB...")
    endpoint = os.environ.get("COSMOS_ENDPOINT")
    key = os.environ.get("COSMOS_KEY")
    db_name = os.environ.get("COSMOS_DB")
    container_name = os.environ.get("COSMOS_CONTAINER")
    partition_key_path = os.environ.get("COSMOS_PARTITION_KEY", "/id")

    if not all([endpoint, key, db_name, container_name]):
        print("❌ Missing Cosmos DB configuration.")
        return

    try:
        client = CosmosClient(url=endpoint, credential=key)
        
        # Create Database
        db = client.create_database_if_not_exists(id=db_name)
        print(f"✅ Database '{db_name}' ready.")
        
        # Define Vector Embedding Policy
        vector_embedding_policy = {
            "vectorEmbeddings": [
                {
                    "path": "/vector",
                    "dataType": "float32",
                    "distanceFunction": "cosine",
                    "dimensions": 1536
                }
            ]
        }

        # Define Indexing Policy
        indexing_policy = {
            "indexingMode": "consistent",
            "automatic": True,
            "includedPaths": [{"path": "/*"}],
            "excludedPaths": [{"path": "/_etag/?"}, {"path": "/vector/*"}],
            "vectorIndexes": [
                {"path": "/vector", "type": "quantizedFlat"}
            ]
        }
        
        # Try creating with vector support
        try:
            container = db.create_container_if_not_exists(
                id=container_name,
                partition_key=PartitionKey(path=partition_key_path),
                vector_embedding_policy=vector_embedding_policy,
                indexing_policy=indexing_policy,
                offer_throughput=400
            )
            print(f"✅ Container '{container_name}' ready with vector support.")
        except Exception as e:
            print(f"⚠️ Failed to create with vector policy: {e}")
            print("Trying standard container...")
            container = db.create_container_if_not_exists(
                id=container_name,
                partition_key=PartitionKey(path=partition_key_path),
                offer_throughput=400
            )
            print(f"✅ Container '{container_name}' ready (standard).")
        
    except Exception as e:
        print(f"❌ Error initializing Cosmos DB: {e}")
        try:
            with open("cosmos_error.log", "w", encoding="utf-8") as f:
                f.write(str(e))
                if hasattr(e, "message"):
                    f.write(f"\nMessage: {e.message}")
                if hasattr(e, "http_error_message"):
                    f.write(f"\nHTTP Error: {e.http_error_message}")
        except:
            pass

if __name__ == "__main__":
    setup_cosmos()
