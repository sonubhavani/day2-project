from pymongo import MongoClient

client=MongoClient('127.0.0.1',27017)
db=client['kits']
c=db['ml']

k=input('enter msg')
dummy={'msg':k}
c.insert_one(dummy)
for i in  c.find():
	pass
else:
	print(i['msg'])

