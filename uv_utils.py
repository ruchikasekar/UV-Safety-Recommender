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


  
  
