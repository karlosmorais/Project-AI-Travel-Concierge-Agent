
from azure.ai.projects.models import BingGroundingAgentTool

t = BingGroundingAgentTool()
print("Dict:", t.as_dict())

# Check if we can set connection_id
try:
    t.connection_id = "test-conn"
    print("Set connection_id success. Dict:", t.as_dict())
except Exception as e:
    print(f"Set connection_id failed: {e}")

# Check if we can set definitions?
try:
    print("Definitions attr check:", getattr(t, 'definitions', 'Missing'))
except:
    pass
