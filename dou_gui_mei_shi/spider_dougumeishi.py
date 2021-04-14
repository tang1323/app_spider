import requests
import json
from multiprocessing import Queue
from handle_mongo import mongo_info
# 引入多线程
from concurrent.futures import ThreadPoolExecutor

# 创建一个队列
queue_list = Queue()


# 请求函数,参数要传不一样的，比如每个url都不一栗，data也不一样，
def handel_request(url, data):
    # 只有header是一样的，所以要在这里添加
    # 经过大量实战，有些头信息可以去掉
    header = {

        # "Cookie": "duid=66167473",
        "client": "4",
        "version": "6969.2",
        "device": "MI 9",
        "sdk": "22,5.1.1",
        "channel": "baidu",
        "resolution": "1920*1080",
        "display-resolution": "1920*1080",
        "dpi": "2.0",
        "pseudo-id": "5c882eb277198af6",
        "brand": "Xiaomi",
        "scale": "2.0",
        "timezone": "28800",
        "language": "zh",
        "cns": "0",
        "carrier": "CHINA+MOBILE",
        "imsi": "460072771082235",
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; MI 9 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36",
        "act-code": "1602120664",
        "act-timestamp": "1602120664",
        "uuid": "9d631a79-8916-4ccf-96a1-b7fcb608941e",
        "battery-level": "0.52",
        "battery-state": "1",
        "terms-accepted": "1",
        "newbie": "1",
        "reach": "1",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "Keep-Alive",
        "session-info": "YPxuTjA3CGTDw3+WgTJFqJLKzN8WNd3zrM4sz8BPLv+KJixGe29X0ru5FRE4yo9z+YOpyo0O+opU0SwRMANVBiRnbpm+82OjlBukfvnOfSWCyNIn2HwNeUvsMgpdGpsO",
        "Host": "api.douguo.net",
        # "Content-Length": "132",

    }
    # 现在就拿这些去请求,url都是post请求的，所以用post
    response = requests.post(url=url, headers=header, data=data)
    return response


# 这里要去请求要分析的url
def handle_index():
    url = 'https://api.douguo.net/recipe/flatcatalogs'
    data = {
        "client": "4",
        "_session": "1602146613387863254282308229",
        # "v": "1602148752",
        "_vs": "2305",
        "sign_ran": "3d196304f1c984cc9c5fdcfc1c5c398a",
        "code": "5e0e5ed704657953",
    }

    # 这里可以放代理ip
    # proxy = {'http':'http://通行证书:通行密钥@网址:端口号'}

    # 这是请求一个总的url,如果想添加代理ip，则在参数后面添加proxies=proxy
    response = handel_request(url=url, data=data)
    # print(response.text)

    # 现在要解析具体的美食，比如说士豆，json.loads，返回的是一个列表
    index_response_dict = json.loads(response.text)
    # 循环遍历那些菜谱分类都有哪一些
    for index_item in index_response_dict['result']['cs']:
        for index_item_1 in index_item['cs']:
            for item in index_item_1['cs']:
                # 这个是具体菜的做法，比如士豆
                data_2 ={
                    "client": "4",
                    # "_session": "1602146613387863254282308229",
                    "keyword": item['name'],
                    "order": "3",
                    "_vs": "11104",
                    "type": "0",
                    "auto_play_mode": "2",
                    "sign_ran": "2735479813a2cfe38c335a0c1c66db17",
                    "code": "2086026519803801",
                }
                # 把数据放队列中，用put方法
                queue_list.put(data_2)


# 请求菜谱列表的编码
def handle_caipu_list(data):
    print('当前处理的菜谱：', data['keyword'])
    # 菜谱列表的第一页的url
    caipu_list_url = 'https://api.douguo.net/recipe/v2/search/0/20'

    # 这是返回菜谱列表的数据
    caipu_list_response = handel_request(url=caipu_list_url, data=data)

    # 这样我们就获得了字典数据，然后循环一下,
    caipu_list_response_dict = json.loads(caipu_list_response.text)
    for item in caipu_list_response_dict['result']['list']:
        # 组装好这些数据
        caipu_info = {}
        # 每放一个食材就会产生一些菜谱
        caipu_info['shicai'] = data['keyword']
        # 如果type等于13的话就是我们要的菜谱
        if item['type'] == 13:
            # 取一下发布这个菜谱这个作者的名字，放在
            caipu_info['user_name'] = item['r']['an']

            # 这个是菜谱的id，里面有菜谱的详情做法
            caipu_info['shicai_id'] = item['r']['id']
            # 菜谱的名字
            caipu_info['caipu_name'] = item['r']['n']
            # 内容介绍
            caipu_info['describe'] = item['r']['cookstory'].replace('\n', '').replace(' ', '')
            # 一些材料佐料
            caipu_info['zuoliao_list'] = item['r']['major']
            # 每一个食材菜谱的详情做法，而且每一个id不同，所以前面取的shicai_id就有用了
            detail_url = 'https://api.douguo.net/recipe/v2/detail/'+str(caipu_info['shicai_id'])


            # detail_url是另一个url了，所以要伪造一下请求体
            detail_data = {
                "client": "4",
                # "_session": "1602146613387863254282308229",
                "author_id": "0",
                "_vs": "11104",
                "_ext": '{"query":{"kw":'+caipu_info['shicai']+',"src":"11104","idx":"3","type":"13","id":'+str(caipu_info['shicai_id'])+'}}',
                "is_new_user": "1",
                "sign_ran": "f624461aaaaca2bee762e9b195edac31",
                "code": "d4d3ada51b30e928",
            }
            detail_response = handel_request(url=detail_url, data=detail_data)
            detail_response_dict = json.loads(detail_response.text)

            # 放到caipu_info里面
            # 这是制作内容
            caipu_info['tips'] = detail_response_dict['result']['recipe']['tips']

            # 这是制作步骤
            caipu_info['cook_step'] = detail_response_dict['result']['recipe']['cookstep']

            # print(caipu_info)
            print('当前入库的菜谱是：', caipu_info['caipu_name'])

            # 这里连接了mongo数据库，但是这个函数只获取前20条数据,可以用for range来循环获取多条数据
            mongo_info.insert_item(caipu_info)


        # 因为有广告，所以遇到广告就跳过
        else:
            continue



handle_index()

# 取队列中的数据，用get方法来取
# handle_caipu_list(queue_list.get())
# print(queue_list.qsize())


# 创建一个线程池,有5个
pool = ThreadPoolExecutor(max_workers=5)
# 循环一下和判断一下
while queue_list.qsize() > 0:
    pool.submit(handle_caipu_list, queue_list.get())










