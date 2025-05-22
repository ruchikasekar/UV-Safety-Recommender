import requests #used for HTTP requests to API
import os #access to environment variables like API
from dotenv import load_dotenv #reads + loads .env file

load_dotenv()
APIKEY = os.getenv("OPENWEATHER_API")

def uv_index(city): 
  '''
  Get the UV index for the given city using OpenWeather API
  '''
coordinates_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={APIKEY}"
coordinates_response = requests.get(coordinates_url) #Requests API info
coordinates = coordinates_response.json() # parses JSON

if not coordinates:
  return None #IF there were no results from the API

lat = coordinates[0]['lat'], geo[0]['lon']


  def calculate_safe_minutes(skin_type, spf, uv_index):
    """
    Calculates a safe sun exposure time (in minutes) based on:
    - Skin type (Fitzpatrick I-VI)
    - SPF value
    - UV index from OpenWeather
    """

    # Step 1: Define base time (in minutes) for each skin type at UV Index = 1, no sunscreen
    base_minutes = {
        "I": 10,
        "II": 15,
        "III": 20,
        "IV": 25,
        "V": 30,
        "VI": 35
    }

    # Get the base time for the given skin type
    base = base_minutes[skin_type]

    # Step 2: Adjust for current UV index (higher UV = lower safe time)
    if uv_index > 0:
        adjusted = base / uv_index
    else:
        adjusted = base

    # Step 3: Adjust for sunscreen SPF (SPF 15 ≈ 2x, SPF 30 ≈ 3x)
    if spf > 0:
        adjusted *= (spf / 15)

    # Return rounded result
    return round(adjusted)
  
