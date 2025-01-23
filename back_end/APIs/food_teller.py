import json
from urllib import request
import os

TOKEN = os.environ['TOKEN_OPENAI']


def food_teller(_menu):
    url = 'https://api.openai.com/v1/chat/completions'

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a registered dietitian of university. Make some short description of each food."},
            {"role": "user", "content": _menu},
            {"role": "assistant",
                "content": "Provide a short description(in 100 letters, Korean) of the menu item."},
        ]
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {TOKEN}',
    }

    data = json.dumps(data).encode('utf-8')

    req = request.Request(url, data=data, headers=headers, method='POST')

    try:
        with request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            assistant_reply = result['choices'][0]['message']['content']
            return assistant_reply
    except Exception as e:
        return "ERROR"
