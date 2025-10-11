import os
import dotenv
import requests
from fastmcp import FastMCP

mcp = FastMCP("OpenWeatherMCP")

dotenv.load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_KEY")
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/"

@mcp.tool()
async def get_current_temperature(city: str) -> dict:
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    response = requests.get(url=f"{OPENWEATHER_URL}weather", params=params)
    return response.json()

@mcp.tool()
async def get_weather_forecast(city: str) -> dict:
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    response = requests.get(url=f"{OPENWEATHER_URL}forecast", params=params)
    return response.json()

if __name__ == "__main__":
    # Dynamic port for Railway or 8000 locally
    port = int(os.getenv("PORT", 8000))
    mcp.run(transport="http", port=port, host="0.0.0.0")