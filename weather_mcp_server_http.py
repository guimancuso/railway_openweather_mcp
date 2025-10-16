import os
from dotenv import load_dotenv
import requests
from fastmcp import FastMCP

mcp = FastMCP("OpenWeatherMCP")

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_KEY")
if not OPENWEATHER_API_KEY:
    raise ValueError("OPENWEATHER_KEY environment variable is required")

OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/"

@mcp.tool()
async def get_current_temperature(city: str) -> dict:
    """Get current temperature and weather data for a city.

    Args:
        city: Name of the city to get weather for

    Returns:
        Dictionary with current weather data including temperature, humidity, etc.
    """
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    response = requests.get(url=f"{OPENWEATHER_URL}weather", params=params)
    response.raise_for_status()
    return response.json()

@mcp.tool()
async def get_weather_forecast(city: str) -> dict:
    """Get 5-day weather forecast for a city.

    Args:
        city: Name of the city to get forecast for

    Returns:
        Dictionary with weather forecast data for the next 5 days
    """
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    response = requests.get(url=f"{OPENWEATHER_URL}forecast", params=params)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    # Dynamic port for Railway or 8000 locally
    port = int(os.getenv("PORT", 8000))
    mcp.run(transport="http", port=port, host="0.0.0.0")