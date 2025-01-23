import json
import urllib.request
import Flask
from slack_sdk import WebClient
import datetime
import json
from pytz import timezone


url = {
    'student': 'https://www.inha.ac.kr/kr/1072/subview.do',
    'professor': 'https://www.inha.ac.kr/kr/1073/subview.do',
    'dormitory': 'https://dorm.inha.ac.kr/dorm/10136/subview.do'
}



channels_to_send = [token_slack]


def lambda_handler(event, context):
    week_json = get_from_api()
    today_message = parse_json_to_message(week_json)
    for token in channels_to_send:
        send_message_to_channel(token, today_message)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


def get_from_api(where=""):
    url = os.env["api_server"]

    response = urllib.request.urlopen(url) 
    data = response.read().decode("utf-8")
    data = data.replace("'", '"')
    data = json.loads(data)
    response.close()
    return data


def this_weekday():
    return datetime.datetime.now(timezone('Asia/Seoul')).strftime("%A")


def today():
    return datetime.datetime.now(timezone('Asia/Seoul')).strftime("%Y년 %m월 %d일")


def parse_json_to_message(json_data):
    today_of_week = this_weekday()
    today_hak = json_data['hak'].get(today_of_week)
    today_gyo = json_data['gyo'].get(today_of_week)
    today_gi = json_data['gi'].get(today_of_week)

    if (today_hak != ''):
        hak = {"breakfast": today_hak["breakfast"],
               "lunch": today_hak["lunch"], "dinner": today_hak["breakfast"]}
    else:
        hak = {"breakfast": "식사를 제공하지 않는 날입니다.",
               "lunch": "식사를 제공하지 않는 날입니다.", "dinner": "식사를 제공하지 않는 날입니다."}
    if (today_gyo != ''):
        today_gyo = today_gyo.get('breakfast').replace("\t\t", "").split('\n')
        today_gyo = [item for item in today_gyo if item != ""]
        gyo = {"breakfast": today_gyo[0]+"\n"+today_gyo[1], "lunch": today_gyo[2]+"\n" +
               "\n(백반)\n"+today_gyo[3]+"\n(특식)\n"+today_gyo[5], "dinner": today_gyo[6]+"\n"+today_gyo[7]}
    else:
        gyo = {"breakfast": "식사를 제공하지 않는 날입니다.",
               "lunch": "식사를 제공하지 않는 날입니다.", "dinner": "식사를 제공하지 않는 날입니다."}
    if (today_gi != ''):
        gi = today_gi.get('lunch').replace('라면/ 쌀밥/ 김치', "")
        gi = gi.replace("일품식", "<일품식>\n")
        gi = gi.replace("한  식", "<한식>\n")
        gi = {"breakfast": today_gi["breakfast"], "lunch": today_gi["lunch"],
              "dinner": today_gi["breakfast"], "easy_meal": today_gi["easy_meal"]}
    else:
        gi = {"breakfast": "식사를 제공하지 않는 날입니다.", "lunch": "식사를 제공하지 않는 날입니다.",
              "dinner": "식사를 제공하지 않는 날입니다.", "easy_meal": "식사를 제공하지 않는 날입니다."}

    return f'✉ 학식왕 김인하 - {today()} 식단 ✉\n\n\n✨ 조식 ✨\n\n*학생식당*\n{hak["breakfast"]}\n\n*교직원식당*\n{gyo["breakfast"]}\n\n*생활관식당*\n{gi["breakfast"]}\n\n\n☀ 중식 ☀\n\n*학생식당*\n{hak["lunch"]}\n\n*교직원식당*\n{gyo["lunch"]}\n\n*생활관식당*\n{gi["lunch"]}\n\n\n🌙 석식 🌙\n\n*학생식당*\n{hak["dinner"]}\n\n*교직원식당*\n{gyo["dinner"]}\n\n*생활관식당*\n{gi["dinner"]}\n\n\n🌭 간편식 🌭\n\n*생활관식당*\n{gi["easy_meal"]}\n\n\n\n식사 맛있게 하세요!'


def send_message_to_channel(token_json, message):
    slack_client = WebClient(token=token_json['bot_token'])
    slack_client.chat_postMessage(
        channel=token_json['channel_id'],
        text=message
    )
