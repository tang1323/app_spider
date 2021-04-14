import requests


# 一定得是response
def response(flow):
    # 如果粉丝url带有以下的url，那就进行分析
    if 'aweme/v1/user/follower/list' in flow.request.url:
        with open('D:/Py-Project/app-spider/douyin/user.txt', 'w') as f:
            f.write(flow.response.text)














