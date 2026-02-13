
import os
import sys
from azure.cosmos import CosmosClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from dotenv import load_dotenv
load_dotenv()

def list_containers():
    try:
        url = os.environ.get("COSMOS_ENDPOINT")
        key = os.environ.get("COSMOS_KEY")
        client = CosmosClient(url, credential=key)
        db_name = "snippets-karlos" # os.environ.get("COSMOS_DB")
        db = client.get_database_client(db_name)
        
        containers = list(db.list_containers())
        print(f"Containers in {db_name}:")
        for c in containers:
            print(f" - {c['id']}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_containers()
