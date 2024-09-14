import os
from dotenv import load_dotenv
import openai
import googlemaps

load_dotenv()

primary_api_key = os.getenv("OPENAI_API_KEY")
alternative_api_key = os.getenv("ALTERNATIVE_OPENAI_API_KEY")
gmaps_api_key = os.getenv("GMAPS_API_KEY")

if not primary_api_key:
    raise ValueError("Primary OpenAI API key not found. Please check your .env file.")
if not gmaps_api_key:
    raise ValueError("Google Maps API key not found. Please check your .env file.")

openai.api_key = primary_api_key
gmaps = googlemaps.Client(key=gmaps_api_key)
