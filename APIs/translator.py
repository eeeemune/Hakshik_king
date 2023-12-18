import json
import os
# from urllib import request
import requests
# from dotenv import load_dotenv


# def food_teller(_menu):
#     url = 'https://api.openai.com/v1/chat/completions'

#     data = {
#         "model": "gpt-3.5-turbo",
#         "messages": [
#             {"role": "system", "content": "You are a registered dietitian of university. Make some short description of each food."},
#             {"role": "user", "content": _menu},
#             {"role": "assistant",
#                 "content": "Provide a short description(in 100 letters, Korean) of the menu item."},
#         ]
#     }

#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {TOKEN}',
#     }

#     data = json.dumps(data).encode('utf-8')

#     req = request.Request(url, data=data, headers=headers, method='POST')

#     try:
#         with request.urlopen(req) as response:
#             result = json.loads(response.read().decode('utf-8'))
#             assistant_reply = result['choices'][0]['message']['content']
#             return assistant_reply
#     except Exception as e:
#         return "ERROR"


class Translator:
    def __init__(self):
        self.DEEPL_TOKEN = os.environ['deepl_token']
        self.DEEPL_TOKEN = "669a03d3-019e-326b-7a20-5eed142dfc5c:fx"
        self.DEEPL_URL = "http://api-free.deepl.com/v2/translate"

    def eng(self, korean_word):
        # headers = {
        #     "Authorization": f"{self.DEEPL_TOKEN}"
        # }
        # print(headers)
        data = {"auth_key": self.DEEPL_TOKEN, "text": korean_word, "target_lang": "EN",
                "context": "food name, romanization.", "source_lang": "KO"}
        # data = json.dumps(data).encode('utf-8')
        # req = request.Request(self.DEEPL_URL,
        #                       data=data, method='POST')
        res = requests.post(self.DEEPL_URL, data=data, verify=True)
        try:
            print(res.json())
        except Exception as e:
            print(e)
            return e


print(Translator().eng("뚝배기김치찌개"))
