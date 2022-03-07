from pymongo import MongoClient as mongo
from datetime import datetime

# 1단계 - mongodb 접속
conn = mongo('mongodb://mydb:1234@192.168.56.101:27017')

# 2단계 - DB 선택
db = conn.get_database('test')

# 3단계 - Collection 선택
coll = db.get_collection('Member')

# 4단계 - 쿼리실행
coll.insert_one({'uid':'p101', 'name':'김유신','hp':'010-1010-1111', 'pos': '사원', 'dep': 101, 'rdate': datetime.now()})

# 5단계 - MongoDB 종료
conn.close()

print('insert 완료...')