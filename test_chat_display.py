#!/usr/bin/env python3
"""Test chat with clean input"""

import json
from app.main import run_request
from chat import display_plan

user_input = "Plan a trip to Paris in June."
print(f"Testing with: {user_input}\n")

result = run_request(user_input)

print("="*60)
print("RESULT:")
print("="*60)

try:
    plan_data = json.loads(result)
    display_plan(plan_data)
except json.JSONDecodeError as e:
    print(f"JSON Error: {e}")
    print(f"Raw result: {result}")
except Exception as e:
    print(f"Display Error: {e}")
    import traceback
    traceback.print_exc()
