from flask import Flask, request, jsonify
import os
import boto3
from boto3.dynamodb.conditions import Key, Attr
# from models import DB

app = Flask(__name__)


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

    def get_menu(self, _date, _when, _where):
        res = self.table.scan(
            FilterExpression=Attr('date').eq(
                f"{_date}#{_when}") & Attr('location').eq(_where)
        )
        # res = self.table.query(
        #     KeyConditionExpression=Key('date').eq(
        #         f"{_date}#{_when}")
        # )
        return res.get('Items')


@app.get('/get_menu')
def get_menu():
    date = request.args.get("date")
    when = request.args.get("when")
    where = request.args.get("where")
    print(where)
    if (where == "student"):
        where = "hak"
    if (where == "dormitory"):
        where = "gi"
    if (where == "professor"):
        where = "gyo"
    res = DB().get_menu(_date=date, _when=when, _where=where)

    return (jsonify(res))


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, True)
