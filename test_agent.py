
import asyncio
import os
import json
from app.main import run_request

async def test():
    print("Testing Agent...")
    user_input = "Plan a trip to Paris in June."
    try:
        result = await asyncio.to_thread(run_request, user_input)
        print("\nResult:")
        print(result)
        
        # Validation
        data = json.loads(result)
        if "plan" in data:
            print("\n✅ Plan found in response.")
        else:
            print("\n❌ Plan NOT found in response.")
            
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(test())
