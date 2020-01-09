from pymongo import MongoClient
from collections import Counter

myclients = MongoClient("mongodb://localhost:27017/")
db= myclients["Website"]
def find_pro(col, sub):
	cols = db["Book"]
	res = list(cols.find({"mon":sub}))
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
def data_auto(query):
    query1 = query.lower()
    col = db['Book']
    subs = list(col.find({'name': {'$regex': query1}},{'_id':False} ))
    subs2 = list(col.find({'tacgia': {'$regex': query1}},{'_id':False} ))
    query2 = query1.capitalize()
    subs1 = list(col.find({'name': {'$regex': query2}},{'_id':False}  ))
    subs3 = list(col.find({'tacgia': {'$regex': query2}},{'_id':False} ))
    for i in subs1:
        if i not in subs:
            subs.append(i)
    for i in subs2:
        if i not in subs:
            subs.append(i)
    for i in subs3:
        if i not in subs:
            subs.append(i)
    autosubs =[]
    for i in subs:
        if i['name'].strip() not in autosubs:
            autosubs.append(i['name'].strip())
        if i['tacgia'].strip() not in autosubs:
            autosubs.append(i['tacgia'].strip())
        if i['language'] not in autosubs:
            autosubs.append(i['language'])
    matching1 = [s for s in autosubs if query1 in s]
    matching2 = [s for s in autosubs if query2 in s]
    for i in matching1:
        if i not in matching2:
            matching2.append(i)
    return matching2
def data_search(query):
    query1 = query.lower()
    col = db['Book']
    subs = list(col.find({'name': {'$regex': query1}}))
    subs2 = list(col.find({'tacgia': {'$regex': query1}}))
    query2 = query1.capitalize()
    subs1 = list(col.find({'name': {'$regex': query2}}))
    subs3 = list(col.find({'tacgia': {'$regex': query2}}))
    subs4 = list(col.find({'name': {'$regex': query}}))
    subs5 = list(col.find({'tacgia': {'$regex': query}}))
    for i in subs1:
        if i not in subs:
            subs.append(i)
    for i in subs2:
        if i not in subs:
            subs.append(i)
    for i in subs3:
        if i not in subs:
            subs.append(i)
    for i in subs4:
        if i not in subs:
            subs.append(i)
    for i in subs5:
        if i not in subs:
            subs.append(i)
    return(subs)
def data_love():
    col = db["Love"]
    lbres = list(col.find())
    res = []
    for i in lbres:
        if i['idbook'] not in res:
            res.append(i['idbook'])
    # print(res)
    col = db["Book"]
    lb = []
    for i in res:
        a = list(col.find({"id":i}))
        lb.append(a[0])
    return lb
