import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get('GOOGLE_API_KEY') 

url = 'https://places.googleapis.com/v1/places:searchText'

payload = {
    'textQuery': 'Gyms with swimming pool in Dayton, OH'
}

headers = {
    'Content-Type': 'application/json',
    'X-Goog-Api-Key': api_key,
    'X-Goog-FieldMask': 'places.displayName,places.formattedAddress'
}

response = requests.post(url, json=payload, headers = headers)

print(response.text)