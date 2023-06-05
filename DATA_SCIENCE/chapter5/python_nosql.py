'''
All about NoSql
Key value - Redis
docker run -d --name redis-stack-server -p 6379:6379 redis:latest


Document - mongo

'''

import redis as r
from pymongo import MongoClient
class PythonRedis:
    def redisTest (self):
        redis = r.Redis()
        redis.mset({"emp1": "Maya Silver", "emp2": "John Jamison"})
        redis.set('Emplyee001', 'Sam Mukherjee')
        print(str(redis.get("Emplyee001").lower()))
        print(f'Exmployee name {redis.get("Emplyee001")}')
        print(f'Exmployee name {redis.mget("emp1")[0]}')

        cabDict ={"ID": "cab48", "Driver": "Dan Varsky", "Brand": "Volvo"}
        redis.hmset("cab48", cabDict)
        print(redis.hgetall("cab48"))


    def mongoTest(self):
        client = MongoClient('mongodb://localhost:27017')
        db = client['sampledb']
        emps_collection = db['emps']
        emp = {"empno": 9001, "empname": "Jeff Russell","orders": [2608, 2617, 2620]}
        result = emps_collection.insert_one(emp)
        print(result)
        emp = emps_collection.find({"empno": 9001})
        #{'_id': ObjectId('6470b7f872fb10d2a29fbcbc'), 'empno': 9001, 'empname': 'Jeff Russell', 'orders': [2608, 2617, 2620]}
        for e in emp:
            print(e)

pr = PythonRedis()
#pr.redisTest()
pr.mongoTest()


'''
{'_id': ObjectId('6470b7f872fb10d2a29fbcbc'), 'empno': 9001, 'empname': 'Jeff Russell', 'orders': [2608, 2617, 2620]}
{'_id': ObjectId('6470b97b6f44a31aae86843c'), 'empno': 9001, 'empname': 'Jeff Russell', 'orders': [2608, 2617, 2620]}
{'_id': ObjectId('6470b99fb36086ab82acafed'), 'empno': 9001, 'empname': 'Jeff Russell', 'orders': [2608, 2617, 2620]}
{'_id': ObjectId('6470b9f2f639fe4a610b9c56'), 'empno': 9001, 'empname': 'Jeff Russell', 'orders': [2608, 2617, 2620]}
{'_id': ObjectId('6470ba1a794c43fd5c7259ab'), 'empno': 9001, 'empname': 'Jeff Russell', 'orders': [2608, 2617, 2620]}

'''