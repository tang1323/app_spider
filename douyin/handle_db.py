
import pymongo
from pymongo.collection import Collection

client = pymongo.MongoClient(host='localhost', port=27017)
# 创建一个数据库的名字叫douyin给db
db = client['douyin']


def handle_init_task():
    # 定义一个表名叫task_id,数据库加表名
    task_id_collection = Collection(db, 'task_id')
    # 循环这个文本，
    with open('D:/Py-Project/app-spider/douyin/douyin_hot_id.txt', 'r') as f_share:
        for f_share_task in f_share.readlines():
            init_task = {}

            # 指明一下字段
            init_task['share_id'] = f_share_task.replace('\n', '')
            # print(init_task)

            # 写进数据库
            task_id_collection.insert(init_task)


# 从数据库里取数据
def handle_get_task():
    task_id_collection = Collection(db, "task_id")
    # find_one只返回一个id
    return task_id_collection.find_one_and_delete({})




# handle_init_task()
handle_get_task()












