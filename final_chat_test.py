#!/usr/bin/env python3
"""Final test of chat display with all fixes"""

import json
from app.main import run_request
from chat import display_plan

print("Testing chat display with: 'Plan a trip to Paris in June.'\n")

result = run_request("Plan a trip to Paris in June.")

try:
    plan_data = json.loads(result)
    display_plan(plan_data)
    print("\n✅ Chat display test PASSED")
except Exception as e:
    print(f"\n❌ Chat display test FAILED: {e}")
    import traceback
    traceback.print_exc()
