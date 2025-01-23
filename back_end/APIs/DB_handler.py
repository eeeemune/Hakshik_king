import boto3
import os


class DB:
    def __init__(self):
        aws_access_key = os.getenv('aws_access_key')
        aws_access_private = os.getenv('aws_access_key_private')

        dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1',
                                  aws_access_key_id=aws_access_key, aws_secret_access_key=aws_access_private)
        self.table = dynamodb.Table('hakshikking')

    def save(self, name, date,  location, when, category="", name_eng="", recipe="", url="", chicken="", beef="", fork="", egg="", seafood="", dscrpt="", dscrpt_eng=""):
        res = self.table.put_item(
            Item={
                "name": name, "date": f"{date}#{when}", "category": category, "location": location, "category": category, "name_eng": str(name_eng), "recipe": recipe, "url": url, "chicken": chicken, "beef": beef, "fork": fork, "egg": egg, "seafood": seafood, "dscrpt": str(dscrpt), "dscrpt_eng": str(dscrpt_eng)
            }
        )
        return res

    def find(self, name):
        res = self.table.query(
            KeyConditionExpression=Key('name').eq(
                name)
        )
        return res.get('Items')
