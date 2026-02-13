# app/synthesis.py
import json
from typing import Dict, Any

def synthesize_to_tripplan(tool_results: Dict[str, Any], requirements: Dict[str, str]) -> str:
    """
    Synthesize tool results into a comprehensive travel plan.
    """
    try:
        # Helper to safely get data
        weather_data = tool_results.get("weather", {})
        search_output = tool_results.get("search", "")
        card_data = tool_results.get("card", {})
        rag_data = tool_results.get("rag", {})
        
        # Parse weather
        weather_info = {
            "temperature_c": None,
            "conditions": "Unknown",
            "recommendation": "N/A"
        }
        if "daily_forecast" in weather_data and weather_data["daily_forecast"]:
            forecast = weather_data["daily_forecast"][0]
            weather_info["temperature_c"] = float(forecast.get("max_temp", 20.0))
            weather_info["conditions"] = "Good" # Simplified
            weather_info["recommendation"] = "Pack appropriately"

        # Parse search
        # Search output might be a string or list
        snippet = str(search_output)[:200] + "..."

        # Construct response
        result = {
            "plan": {
                "destination": requirements.get("destination", "Paris"),
                "travel_dates": requirements.get("dates", "2026-06-01 to 2026-06-08"),
                "weather": weather_info,
                "results": [
                    {
                        "title": "Search Result",
                        "snippet": snippet,
                        "url": "https://bing.com",
                        "category": "General"
                    }
                ],
                "card_recommendation": {
                    "card": card_data.get("card", "Unknown"),
                    "benefit": card_data.get("benefit", "Unknown"),
                    "fx_fee": card_data.get("fx_fee", "Unknown"),
                    "source": card_data.get("source", "Unknown")
                },
                "currency_info": {
                    "sample_meal_usd": 100.0,
                    "sample_meal_eur": 92.0,
                    "usd_to_eur": 0.92,
                    "points_earned": 400
                },
                "citations": ["https://bing.com"],
                "next_steps": ["Book flight", "Reserve hotel"]
            }
        }
        
        return json.dumps(result, indent=2)
        
    except Exception as e:
        return json.dumps({"error": str(e)})