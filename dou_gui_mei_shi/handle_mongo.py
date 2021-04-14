
import pymongo
from pymongo.collection import Collection
from pymongo import MongoClient


# 数据入库mongodb
class Connect_mongo(object):
    def __init__(self):
        # 连接mongodb数据库， host是本电脑的ip地址,
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        # 创建一个数据库的名字
        self.db_data = self.client['dou_guo_mei_shi']

    # 插入数据，用item的方式
    def insert_item(self, item):
        # 定义一下数据表叫什么,Collection中先写什么数据库，再写数据库中的表名是什么，这里叫dou_guo_mei_shi_item
        db_collection = Collection(self.db_data, 'dou_guo_mei_shi_item')
        # 在这里就可以插入数据了
        db_collection.insert(item)


# 创建一个类的实例
mongo_info = Connect_mongo()










