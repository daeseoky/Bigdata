from pymongo import MongoClient as mongo
from datetime import datetime

# 1단계 - mongodb 접속
conn = mongo('mongodb://mydb:1234@192.168.56.101:27017')

# 2단계 - DB 선택
db = conn.get_database('test')

# 3단계 - Collection 선택
collection = db.get_collection('Member')

# 4단계 - 쿼리실행
rs = collection.find()

for row in rs:
    print(f"{row['uid']},{row['name']},{row['hp']},{row['pos']},{row['dep']},{row['rdate']}")

# 5단계 - MongoDB 종료
conn.close()

print('insert 완료...')