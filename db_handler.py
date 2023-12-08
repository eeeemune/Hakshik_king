import boto3
from dotenv import load_dotenv
import deepl
import os

load_dotenv()


aws_access_key = os.getenv('aws_access_key')
aws_access_private = os.getenv('aws_access_key_private')

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1',
                          aws_access_key_id=aws_access_key, aws_secret_access_key=aws_access_private)

table = dynamodb.Table('hakshik_table')

# table.put_item(Item=data)


def new_id():
    response = table.scan(Select="COUNT")
    print(response)
    return response.get("Count", 0) + 1


def new_food(name, name_eng, recipe, url, chiken, beef, fork, egg, seafood):
    item_id = new_id()
    res = table.put_item(
        Item={
            "menuID": item_id, "name": name, "name_eng": name_eng,  "recipe": recipe, "url": url, "chiken": chiken, "beef": beef, "fork": fork, "egg": egg, "seafood": seafood
        }
    )
    print(res)


def new_date(menuID, date, category, where, when):
    pass


new_food("대도닭강정", "chiken love",
         "[닭, 기름]", "www.naver.com", "True", "False", "False", "True", "False")
