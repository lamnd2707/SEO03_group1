from pymongo import MongoClient

myclient = MongoClient("mongodb://10.14.0.152:27017/")

def find_pro(col, sub):
	db = myclient[str(col)]
	print("success")
	res = list(db.find("mon":sub))
	print(res, "success")
	return res