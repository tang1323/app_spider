
import requests
import json

def handle_douyin_web_share():
    share_web_url = "https://www.iesdouyin.com/share/user/96439419199"
    share_web_header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 Edg/80.0.361.111"
    }

    response = requests.get(url=share_web_url, headers=share_web_header)
    print(response.text)


handle_douyin_web_share()

