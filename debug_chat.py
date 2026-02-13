#!/usr/bin/env python3
"""Debug script to see what chat.py receives"""

import json
from app.main import run_request

user_input = "Plan a trip to Paris in June."
result = run_request(user_input)

print("="*60)
print("RAW RESULT:")
print("="*60)
print(result)
print()

print("="*60)
print("PARSED JSON:")
print("="*60)
try:
    data = json.loads(result)
    print(json.dumps(data, indent=2))
    
    if "plan" in data:
        print("\n✅ 'plan' key found")
        print(f"Plan keys: {list(data['plan'].keys())}")
    else:
        print("\n❌ 'plan' key NOT found")
        print(f"Top-level keys: {list(data.keys())}")
except json.JSONDecodeError as e:
    print(f"❌ JSON decode error: {e}")
