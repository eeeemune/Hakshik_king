import json
import os
# from urllib import request
import requests

class Translator:
    def __init__(self):
        self.DEEPL_TOKEN = os.environ['deepl_token']
        self.DEEPL_URL = "http://api-free.deepl.com/v2/translate"

    def eng(self, korean_word):
        headers = {
            "Authorization": f"{self.DEEPL_TOKEN}"
        }

        data = {"auth_key": self.DEEPL_TOKEN, "text": korean_word, "target_lang": "EN",
                "context": "food name, romanization.", "source_lang": "KO"}
        data = json.dumps(data).encode('utf-8')
        req = request.Request(self.DEEPL_URL,
                              data=data, method='POST')
        res = requests.post(self.DEEPL_URL, data=data, verify=True)
        try:
            print(res.json())
        except Exception as e:
            print(e)
            return e