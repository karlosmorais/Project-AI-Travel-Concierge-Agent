from semantic_kernel.functions import kernel_function
import requests
import json
from typing import Dict, Any

class WeatherTools:
    @kernel_function(name="get_weather", description="Get weather forecast for a location.")
    def get_weather(self, lat: float, lon: float) -> str:
        """
        Get weather forecast for given coordinates using Open-Meteo API.
        Returns a JSON string with daily max/min temps and weather codes.
        """
        from app.utils.logger import get_logger
        logger = get_logger("travel_agent")
        logger.debug(f"WeatherTools: Requesting weather for lat={lat}, lon={lon}")
        try:
            url = "https://api.open-meteo.com/v1/forecast"
            params = {
                "latitude": lat,
                "longitude": lon,
                "daily": "weathercode,temperature_2m_max,temperature_2m_min",
                "timezone": "UTC",
                "forecast_days": 10
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Simplified result for the agent
            daily = data.get("daily", {})
            result = {
                "daily_forecast": [
                    {
                        "date": date,
                        "max_temp": str(daily["temperature_2m_max"][i]),
                        "min_temp": str(daily["temperature_2m_min"][i]),
                        "code": str(daily["weathercode"][i])
                    }
                    for i, date in enumerate(daily.get("time", []))
                ]
            }
            return json.dumps(result)
            
        except Exception as e:
            return json.dumps({"error": str(e)})