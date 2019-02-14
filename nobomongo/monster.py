import pymongo
import pprint
from pymongo import MongoClient
import datetime
connect = MongoClient('192.168.0.46', 27017)
db=connect.testdb
monster=db.monsters
mon=monster.find_one()
print(mon['name'])
pprint.pprint(mon)
for mon in monster.find():
    pprint.pprint(mon)