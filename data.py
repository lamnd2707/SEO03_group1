from pymongo import MongoClient

myclients = MongoClient("mongodb://localhost:27017/")
db= myclients["Website"]
def find_pro(col, sub):
	# myclient = MongoClient("mongodb://10.14.0.152:27017/")
	print("success")
	cols = db["Book"]
	print("success")
	res = list(cols.find({"mon":"Toan"}))
	print(res, "success")
	return res