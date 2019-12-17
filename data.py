from pymongo import MongoClient

myclients = MongoClient("mongodb://localhost:27017/")
db= myclients["Website"]
def find_pro(col, sub):
	# myclient = MongoClient("mongodb://10.14.0.152:27017/")
	print("success")
	cols = db["Book"]
	print("success")
	res = list(cols.find({"mon":sub}))
	print(res, "success")
	return res

def count(col):
	cols = db[col]
	res = len(list(cols.find()))
	return res

def subs_find(col):
	cols = db[col]
	res = list(cols.find())
	return res