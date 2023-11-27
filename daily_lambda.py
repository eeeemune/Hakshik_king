import json
import urllib.request
import Flask
from slack_sdk import WebClient
import datetime
import json
from pytz import timezone


url={
    'student':'https://www.inha.ac.kr/kr/1072/subview.do',
    'professor': 'https://www.inha.ac.kr/kr/1073/subview.do',
    'dormitory':'https://dorm.inha.ac.kr/dorm/10136/subview.do'
}

token_eemune = {'channel_id' : 'C05FV3HCTHT',
'app_token': 'xapp-1-A0638MTUASH-6126305421777-a39d6b35596daa9380e9b0d65026667bbc75c57c084991aed487c9e0984e7c56',
'bot_token' : 'xoxb-5565757234368-6126325981553-qURGNulzVPQayReIHrH3qs2I'
}
token_start_aws = {'channel_id' : 'C064S1WFG9F',
'app_token': 'xapp-1-A064DALRDFD-6264570540225-0869e3811dfed1b6b8624d28a25ba3b135b63f050efae9c38102e6d71a56d43b',
'bot_token' : 'xoxb-4997656156160-6146545663637-EJp0IwIzD25Mn7415piEjKci'
}
token_hakshikking = {'channel_id' : 'C06444PDSMU',
'app_token': 'xapp-1-A064ZPC4YGY-6251867029347-78759ce0ad26f76355c5b512b2c4a7c8dc3da5a8576e52449280c2bac878f7ce',
'bot_token' : 'xoxb-6159436936209-6143884905333-Z9nvXf8e1KwUVf9CrAbHcAOk'
}
token_hakshikking_admin = {'channel_id' : 'C0647S9P8S1',
'app_token': 'xapp-1-A064ZPC4YGY-6251867029347-78759ce0ad26f76355c5b512b2c4a7c8dc3da5a8576e52449280c2bac878f7ce',
'bot_token' : 'xoxb-6159436936209-6143884905333-Z9nvXf8e1KwUVf9CrAbHcAOk'
}

channels_to_send = [token_hakshikking, token_start_aws]

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
    url = "http://52.192.177.197:5000///get?where={where}"

    response = urllib.request.urlopen(url)  # URL을 엽니다. # 응답 데이터를 읽습니다.
    data = response.read().decode("utf-8")
    data = data.replace("'", '"')
    print(data)
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

    if(today_hak != ''):
        hak = {"breakfast": today_hak["breakfast"], "lunch": today_hak["lunch"], "dinner":today_hak["breakfast"]}
    else:
        hak ={"breakfast": "식사를 제공하지 않는 날입니다.", "lunch": "식사를 제공하지 않는 날입니다.", "dinner":"식사를 제공하지 않는 날입니다."}
    if(today_gyo != ''):
        today_gyo = today_gyo.get('breakfast').replace("\t\t", "").split('\n')
        today_gyo = [item for item in today_gyo if item != ""]
        gyo = {"breakfast": today_gyo[0]+"\n"+today_gyo[1], "lunch": today_gyo[2]+"\n"+"\n(백반)\n"+today_gyo[3]+"\n(특식)\n"+today_gyo[5], "dinner":today_gyo[6]+"\n"+today_gyo[7]}
    else:
        gyo ={"breakfast": "식사를 제공하지 않는 날입니다.", "lunch": "식사를 제공하지 않는 날입니다.", "dinner":"식사를 제공하지 않는 날입니다."}
    if(today_gi != ''):
        gi = today_gi.get('lunch').replace('라면/ 쌀밥/ 김치', "")
        gi = gi.replace("일품식", "<일품식>\n")
        gi = gi.replace("한  식", "<한식>\n")
        gi = {"breakfast": today_gi["breakfast"], "lunch": today_gi["lunch"], "dinner":today_gi["breakfast"], "easy_meal":today_gi["easy_meal"]}
    else:
        gi ={"breakfast": "식사를 제공하지 않는 날입니다.", "lunch": "식사를 제공하지 않는 날입니다.", "dinner":"식사를 제공하지 않는 날입니다.", "easy_meal":"식사를 제공하지 않는 날입니다."}
    
    
    # if(today_hak != ''):
    #     hak_message = f'*학생식당*\n\n✨ 조식 ✨\n{today_hak["breakfast"]}\n\n☀ 중식 ☀\n{today_hak["lunch"]}\n\n🌙 석식 🌙\n{today_hak["dinner"]}\n\n\n'
    # else:
    #     hak_message = f'*학생식당*\n식사를 제공하지 않는 날입니다.\n'
    # if(today_gyo != ''):
    #     today_gyo = today_gyo.get('breakfast').replace("\t\t", "").split('\n')
    #     today_gyo = [item for item in today_gyo if item != ""]
    #     gyo_message = f'*교직원식당*\n\n✨ 조식 ✨\n{today_gyo[0]}\n{today_gyo[1]}\n\n☀ 중식 ☀\n{today_gyo[2]}\n(백반)\n{today_gyo[3]}\n\n(특식)\n{today_gyo[5]}\n\n\n🌙 석식 🌙\n{today_gyo[6]}\n{today_gyo[7]}\n\n\n'
    # else:
    #     gyo_message = f'*교직원식당*\n식사를 제공하지 않는 날입니다.\n'
    # if(today_gi != ''):
    #     gi_message = f'*생활관식당*\n\n✨ 조식 ✨\n{today_gi["breakfast"]}\n\n☀ 중식 ☀\n{today_gi["lunch"]}\n\n🌙 석식 🌙\n{today_gi["dinner"]}\n\n🌭 간편식 🌭\n{today_gi["easy_meal"]}\n\n\n'
    # else:
    #     gi_message = f'*생활관식당*\n식사를 제공하지 않는 날입니다.\n'


    return f'✉ 학식왕 김인하 - {today()} 식단 ✉\n\n\n✨ 조식 ✨\n\n*학생식당*\n{hak["breakfast"]}\n\n*교직원식당*\n{gyo["breakfast"]}\n\n*생활관식당*\n{gi["breakfast"]}\n\n\n☀ 중식 ☀\n\n*학생식당*\n{hak["lunch"]}\n\n*교직원식당*\n{gyo["lunch"]}\n\n*생활관식당*\n{gi["lunch"]}\n\n\n🌙 석식 🌙\n\n*학생식당*\n{hak["dinner"]}\n\n*교직원식당*\n{gyo["dinner"]}\n\n*생활관식당*\n{gi["dinner"]}\n\n\n🌭 간편식 🌭\n\n*생활관식당*\n{gi["easy_meal"]}\n\n\n\n식사 맛있게 하세요!'



def send_message_to_channel(token_json, message):
    slack_client = WebClient(token=token_json['bot_token'])
    slack_client.chat_postMessage(
        channel=token_json['channel_id'],
        text=message
    )

