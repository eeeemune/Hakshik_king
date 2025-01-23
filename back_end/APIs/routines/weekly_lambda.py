import json
import urllib.request
from slack_sdk import WebClient
import datetime


url = {
    'student': 'https://www.inha.ac.kr/kr/1072/subview.do',
    'professor': 'https://www.inha.ac.kr/kr/1073/subview.do',
    'dormitory': 'https://dorm.inha.ac.kr/dorm/10136/subview.do'
}

token = token_hakshikking_admin


def lambda_handler(event, context):
    res = gogo_init()
    send_message_to_channel("이번주 학식 업데이트 완료")
    send_message_to_channel(res)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


def gogo_init(where=""):
    url = os.env["api_server"]

    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    data = str(data)
    response.close()
    return data


def send_message_to_channel(message):
    slack_client = WebClient(token=token["bot_token"])
    slack_client.chat_postMessage(
        channel=token["channel_id"],
        text=message
    )
