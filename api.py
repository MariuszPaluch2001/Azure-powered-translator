import requests, uuid

import os
from dotenv import load_dotenv
from typing import Dict, List

load_dotenv()

def get_translation(url: str, key: str, location: str, params: Dict, text: str) -> List[Dict]:
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{ 'text': text }]

    request = requests.post(url, params=params, headers=headers, json=body)
    response = request.json()
    
    return response

key = os.getenv('KEY')
endpoint = os.getenv('ENDPOINT')
location = os.getenv('LOCATION')
path = os.getenv('PATH_ENDPOINT')

constructed_url = endpoint + path

params = {
    'api-version': '3.0', 
    'from': 'en', 
    'to': 'pl'
}

res = get_translation(constructed_url, key, location, params, 'I would really like to drive your car around the block a few times!')
print(res)