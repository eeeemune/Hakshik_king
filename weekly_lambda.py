import json
import urllib.request
from slack_sdk import WebClient
import datetime


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
    url = "http://52.192.177.197:5000/init"

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
