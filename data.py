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

def filter_book(mon,thoihan,language):
	col = db["Book"]
	if mon == "":
		if thoihan == "":
			if language == "":
				res = list(col.find())
			else:
				res = list(col.find({"language":language}))
		else:
			if language == "":
				res = list(col.find({"thoihan":thoihan}))
			else:
				res = list(col.find({"language":language, "thoihan":thoihan}))
	else:
		if thoihan == "":
			if language == "":
				res = list(col.find({"mon":mon}))
			else:
				res = list(col.find({"language":language, "mon":mon}))
		else:
			if language == "":
				res = list(col.find({"thoihan":thoihan, "mon":mon}))
			else:
				res = list(col.find({"language":language, "thoihan":thoihan, "mon":mon}))
	return res