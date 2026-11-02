
import random # Import the random module from Python's standard library, that provides functions to generate random numbers
import json
import datetime
import os
from pathlib import Path
import requests
from dotenv import load_dotenv
from fastmcp import FastMCP # Import the FastMCP class from the fastmcp package that is a higher-level abstraction (wrapper) for building MCP servers quickly and easily
from fastmcp.resources import TextResource # For text/plain and application/json content



# Load environment variables (API keys, etc.) from the course's keys/.env file.
# The path is built from this file's own location (Notebooks/mcp_demo_server/main.py -> keys/.env),
# so it also works when Claude Desktop starts the server from a different working directory.
# Variables passed in Claude Desktop's config ("env") are not overridden.
load_dotenv(Path(__file__).resolve().parents[2] / "keys" / ".env")
# Read WeatherAPI key from environment
weather_api_key = os.getenv("WEATHER_API_KEY")

# Create the server instance, giving it a name/identifier
mcp = FastMCP(name="Demo-server")


# -------------------------------------------------------------------------------------------------
# Define tools: to mark a function as a tool, we use the decorator @mcp.tool(), that is provided by FastMCP.
# Instead of writing JSON manually, You define tools using decorators.
# MCP automatically generates:
        # Tool name
        # Description (from docstring)
        # Input schema (from type hints)
        # Output schema
        # Metadata
# This becomes part of MCP’s tool registry, which the model can discover and invoke dynamically.
# --------------------------------------------------------------------------------------------------

@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together and returns their sum."""
    return a+b

@mcp.tool()
def roll_dice(n_dice: int = 1) -> list[int]:
    """Roll n_dice 6-sided dice and return the result"""
    return [random.randint(1,6) for _ in range(n_dice)] #generates a random integer between 1 and 6 (inclusive).

@mcp.tool()
def get_datetime() -> str:
    """Return the current date and time as a string."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@mcp.tool()
def fahrenheit_to_celsius(temp_f: float) -> float:
    """Convert a temperature from Fahrenheit to Celsius."""
    return (temp_f - 32) * 5.0 / 9.0

@mcp.tool()
def reverse_string(text: str) -> str:
    """Reverse the given text string."""
    return text[::-1]

@mcp.tool()
def count_words(text: str) -> int:
    """Count the number of words in a given text string."""
    return len(text.split())

@mcp.tool()
def get_weather(city:str = "Lahore") -> dict:
    """Fetch current weather info for a given city using WeatherAPI.com"""
    if not weather_api_key:
        return {"error": "Weather API key not set in .env file"}
    try:
        url = "https://api.weatherapi.com/v1/current.json"   # https, so the API key is not sent in plain text
        response = requests.get(url, params={"key": weather_api_key, "q": city}, timeout=5)
        response.raise_for_status()
        data = response.json()
        # Return structured info
        return {
            "Country": data['location']['country'],
            "City": data['location']['name'],
            "Latitude": data['location']['lat'],
            "Longitude": data['location']['lon'],
            "Temperature (C)": data['current']['temp_c'],
            "Temperature (F)": data['current']['temp_f'],
            "Condition": data['current']['condition']['text'],
            "Humidity (%)": data['current']['humidity'],
            "Wind (km/h)": data['current']['wind_kph'],
            "Feels Like (C)": data['current']['feelslike_c'],
            "Last Updated": data['current']['last_updated'],
        }
    except Exception as e:
        return {"error": str(e)}

# ---------------------------------------------------------------------
# Define Resources (static or retrievable data for MCP clients)
# ---------------------------------------------------------------------

# Static Resource 1: A static greeting message
mcp.add_resource(
    TextResource(
        uri="local://greeting",          # A unique identifier or address for the resource.
        name="greeting",                 # A human-readable name for the resource.
        description="A simple greeting message",     # Short explanation of what the resource is.
        text="Hello from your local MCP server! 🎉"  # The actual content of the resource (the text that clients will get).
    )
)

# Static Resource 2: Sample JSON data
sample_json_data = {"students": ["Hadeed", "Yashal", "Zalaid", "Miraal"], "class": "AI Basics"}
mcp.add_resource(
    TextResource(
        uri="local://sample-data",
        name="sample-data",
        description="Sample student data",
        text=json.dumps(sample_json_data, indent=2)
    )
)



# ---------------------------------------------------------------------
# Define Prompts: reusable prompt templates that the user can pick in the client
# ---------------------------------------------------------------------

@mcp.prompt()
def weather_report(city: str = "Lahore") -> str:
    """Write a short, friendly weather report for a city."""
    return f"Use the get_weather tool to fetch the current weather in {city}, then write a friendly three-sentence weather report."


if __name__ == "__main__":
    mcp.run()
