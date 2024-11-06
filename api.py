import requests, uuid

from typing import Dict, List


def get_translation(
    url: str, key: str, location: str, params: Dict, text: str
) -> List[Dict]:
    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Ocp-Apim-Subscription-Region": location,
        "Content-type": "application/json",
        "X-ClientTraceId": str(uuid.uuid4()),
    }

    body = [{"text": text}]

    request = requests.post(url, params=params, headers=headers, json=body)
    response = request.json()

    return response
