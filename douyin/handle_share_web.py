
import requests
from lxml import etree
import json
from douyin.handle_db import handle_get_task
import time

def handle_douyin_web_share(task):
    share_web_url = "https://www.iesdouyin.com/web/api/v2/user/info/?sec_uid={}".format(task['share_id'])
    share_web_header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 Edg/80.0.361.111"
    }

    share_web_response = requests.get(url=share_web_url, headers=share_web_header)
    # print(share_web_response.text)
    # share_web_html = etree.HTML(share_web_response.text)
    # print(json_data)
    user_info = {}
    # user_info['uid']

    # 因为数据是在json下，所以要loads，把它变成一个字典对象
    json_data = json.loads(share_web_response.text)

    # 在这里取出想要的数据

    # 用户昵称
    user_info['user_name'] = json_data["user_info"]["nickname"]

    # 抖音ID
    user_info['douyin_id'] = json_data["user_info"]["short_id"]

    # 粉丝量
    user_info['fans_num'] = json_data["user_info"]["follower_count"]

    # 点赞量
    user_info['fav_num'] = json_data["user_info"]["total_favorited"]

    # 描述
    user_info['describe'] = json_data["user_info"]["signature"]

    # 被关注量
    user_info['follow'] = json_data["user_info"]["following_count"]

    # 工作类型
    user_info['job'] = json_data["user_info"]["custom_verify"]

    print(user_info)


while True:
    task = handle_get_task()
    handle_douyin_web_share(task)
    time.sleep(1)














