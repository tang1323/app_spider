import requests


# 120.239.73.200
url = 'http://ip.hahado.cn/ip'

proxy = {'http':'http://通行证书:通行密钥@网址:端口号'}
response = requests.get(url=url, proxies=proxy)
print(response.text)