import pymongo
import pprint
from pymongo import MongoClient
import datetime
connection = MongoClient('192.168.0.46',27017)
db = connection.korea
emp=db.employees #mongodb는 테이블이 없으면 생성
emp.insert_many(
    [
        {"name": "Mike","date": datetime.datetime(2017, 9, 23, 11, 14)},
        {"name": "Eliot","date": datetime.datetime(2017, 9, 23, 10, 45)}
    ]
)
item = emp.find_one()
print(item['name'])
pprint.pprint(item)
for employee in emp.find():
    pprint.pprint(employee)