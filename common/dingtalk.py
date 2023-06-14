import requests
import json
from common.log import logger
from config import conf

# 发送钉钉消息基础方法
def send_dingding_msg(msg):
    ding_token = conf().get('ding_token')     
    logger.info("[dingtalk] send_dingding_msg: ding_token: {}, msg: {}".format(ding_token, msg))
    if not ding_token:
   
        return
    dingtalk_robot_url = f"https://oapi.dingtalk.com/robot/send?access_token={ding_token}"
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    response = requests.post(dingtalk_robot_url, data=json.dumps(msg), headers=headers)
    return response.json()

def send_markdown_msg(msg):

    ding_title = conf().get('ding_title')
    logger.info("[dingtalk] send_markdown_msg: ding_title: {}, msg: {}".format(ding_title, msg))

    if not ding_title:
        return

    message = {
        "msgtype": "markdown",
        "markdown": {
            "title": ding_title,
            "text": msg,
        }
    }
    return send_dingding_msg(message)
