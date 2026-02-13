
import os
import sys
from azure.cosmos import CosmosClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from dotenv import load_dotenv
load_dotenv()

def list_databases():
    try:
        url = os.environ.get("COSMOS_ENDPOINT")
        key = os.environ.get("COSMOS_KEY")
        client = CosmosClient(url, credential=key)
        
        dbs = list(client.list_databases())
        print(f"Databases:")
        for db in dbs:
            print(f" - {db['id']}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_databases()
