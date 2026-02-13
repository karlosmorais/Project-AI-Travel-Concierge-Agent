
import os
import sys
from azure.cosmos import CosmosClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from dotenv import load_dotenv
load_dotenv()

def delete_db(db_name):
    try:
        url = os.environ.get("COSMOS_ENDPOINT")
        key = os.environ.get("COSMOS_KEY")
        client = CosmosClient(url, credential=key)
        
        print(f"Deleting database: {db_name}...")
        client.delete_database(db_name)
        print(f"✅ Database {db_name} deleted.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        delete_db(sys.argv[1])
    else:
        print("Usage: python delete_db.py <db_name>")
