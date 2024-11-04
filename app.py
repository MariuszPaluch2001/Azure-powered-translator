from flask import (
    Flask, 
    jsonify
)
import os
from dotenv import load_dotenv

from api import get_translation

load_dotenv()

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

app = Flask(__name__)

@app.route('/')
def hello_world():
    response = get_translation(constructed_url, key, location, params, 'I would really like to drive your car around the block a few times!')
    text = response[0]["translations"][0]["text"]

    return jsonify({
        "status": "success",
        "message": text
    }) 

if __name__ == '__main__':
    app.run(debug=True)