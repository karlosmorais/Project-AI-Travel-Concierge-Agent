
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

print("Verifying DefaultAzureCredential...")
cred = DefaultAzureCredential()

try:
    print("Attempting to get token for scope: https://cognitiveservices.azure.com/.default")
    token = cred.get_token("https://cognitiveservices.azure.com/.default")
    print(f"Success! Token received (len={len(token.token)})")
except Exception as e:
    print(f"Failed via DefaultAzureCredential: {e}")

# Check env vars
print("\nEnvironment Variables Check:")
keys = ["AZURE_CLIENT_ID", "AZURE_TENANT_ID", "AZURE_CLIENT_SECRET", "AZURE_OPENAI_API_KEY", "PROJECT_CONNECTION_STRING"]
for k in keys:
    v = os.environ.get(k)
    print(f"{k}: {'Set' if v else 'Missing'}")
