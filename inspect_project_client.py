
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

try:
    print("AIProjectClient dir:")
    print(dir(AIProjectClient))
    
    project_conn_str = os.environ.get("PROJECT_ENDPOINT")
    # ...
    if not project_conn_str:
        print("Missing PROJECT_ENDPOINT")
        exit(1)
        
    project_client = AIProjectClient(
        endpoint=project_conn_str,
        credential=DefaultAzureCredential(),
    )
    
    print("\n--- Inspecting create Signature ---")
    try:
        fn = getattr(project_client.agents, "create")
        import inspect
        print(inspect.signature(fn))
    except Exception as e:
        print(f"Error inspecting create: {e}")
    
except Exception as e:
    print(f"Error: {e}")
