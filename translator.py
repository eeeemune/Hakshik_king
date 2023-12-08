from dotenv import load_dotenv
import deepl
import os

load_dotenv()


def eng(korean_word):
    deepl_token = os.getenv('deepl_token')
    translator = deepl.Translator(deepl_token)
    return translator.translate_text(korean_word, source_lang="KO", target_lang="EN-US", context="food name/romanize")
