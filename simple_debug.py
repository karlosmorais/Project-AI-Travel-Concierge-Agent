#!/usr/bin/env python3
"""Simple debug script to see JSON structure"""

import json
from app.main import run_request

user_input = "Plan a trip to Paris in June."
result = run_request(user_input)

# Save to file to avoid encoding issues
with open("debug_output.json", "w", encoding="utf-8") as f:
    f.write(result)

print("Result saved to debug_output.json")

# Try to parse and show structure
try:
    data = json.loads(result)
    print("\nTop-level keys:", list(data.keys()))
    if "plan" in data:
        print("Plan keys:", list(data["plan"].keys()))
        if "trip" in data["plan"]:
            print("Trip keys:", list(data["plan"]["trip"].keys()))
except Exception as e:
    print(f"Error: {e}")
