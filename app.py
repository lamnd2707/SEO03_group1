from flask import Flask, render_template, url_for, redirect, request, jsonify
from pymongo import MongoClient
from data import find_pro, count, subs_find, filter_book

app = Flask(__name__)
myclient = MongoClient("mongodb://localhost:27017/")

db = myclient["Website"]
# print("sucess")

@app.route('/loginmanage', methods=['GET', 'POST'])
def loginmanage():
    col = db["Admin"]
    error = None
    if request.method == 'POST':
    	print(request.form['username'])
    	if len(list(col.find({"name":str(request.form['username']), "pass":str(request.form['pass'])}))) == 0:
        	error = "Invalid user, please try again!"
    	else:
    		a = list(col.find({"name":str(request.form['username']), "pass":str(request.form['pass'])}))
    		print(a)
    		return redirect(url_for('dashboard',admin=request.form['username'] ))
    return render_template('loginmanage.html', error=error)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    user = request.args.get('user')
    # print(user)
    col = db["Reader"]
    res = list(col.find({"email":user}))
    try:
        flname = res[0]['fname'] + " " + res[0]['lname']
    except:
        flname = ""
        user = None
    if user == "None" or user is None:
        return render_template('index.html',user="None")
    else:
        return render_template('index.html', user=user,flname=flname)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
  if request.method == 'GET':
    admin = request.args.get('admin')
    count1 = count("Reader")
    count2 = count("Book")
    count3 = count("Admin")
    col = db["Admin"]
    if (admin is None) or (admin =="None") or (len(list(col.find({"name":str(admin)}))) == 0):
      return render_template('loginmanage.html', error="Please Login")
    else:
      return render_template('dashboard.html', admin = admin, count1= count1, count2=count2,count3=count3)

@app.route('/math', methods=['GET', 'POST'])
def math():
    if request.method == 'GET':
        user = request.args.get('user')
        # print(user)
        subs = find_pro("Book","Toan")
        # print(subs)
        col = db["Reader"]
        res = list(col.find({"email": user}))
        try:
            flname = res[0]['fname'] + " " + res[0]['lname']
        except:
            flname = ""
            user = None
        if user == "None" or user is None:
            return render_template('math.html', subs = subs, user="None")
        else:
            return render_template('math.html', subs = subs, user=user,flname=flname)

@app.route('/physical', methods=['GET', 'POST'])
def physical():
    if request.method == 'GET':
        user = request.args.get('user')
        # print(user)
        subs = find_pro("Book", "Ly")
        # print(subs)
        col = db["Reader"]
        res = list(col.find({"email": user}))
        try:
            flname = res[0]['fname'] + " " + res[0]['lname']
        except:
            flname = ""
            user = None
        if user == "None" or user is None:
            return render_template('physical.html', subs = subs, user="None")
        else:
            return render_template('physical.html', subs = subs,user=user,flname=flname)

@app.route('/chemistry', methods=['GET', 'POST'])
def chemistry():
    if request.method == 'GET':
        user = request.args.get('user')
        # print(user)
        subs = find_pro("Book", "Hoa")
        # print(subs)
        col = db["Reader"]
        res = list(col.find({"email": user}))
        try:
            flname = res[0]['fname'] + " " + res[0]['lname']
        except:
            flname = ""
            user = None
        if user == "None" or user is None:
            return render_template('chemistry.html', subs=subs, user="None")
        else:
            return render_template('chemistry.html',subs = subs,user=user,flname=flname)

@app.route('/informatics', methods=['GET', 'POST'])
def informatics():
    if request.method == 'GET':
        user = request.args.get('user')
        # print(user)
        subs = find_pro("Book", "Tin")
        # print(subs)
        col = db["Reader"]
        res = list(col.find({"email": user}))
        try:
            flname = res[0]['fname'] + " " + res[0]['lname']
        except:
            flname = ""
            user = None
        if user == "None" or user is None:
            return render_template('informatics.html', subs=subs, user="None")
        else:
            return render_template('informatics.html', subs = subs,user=user,flname=flname)

@app.route('/literarys', methods=['GET', 'POST'])
def literarys():
    if request.method == 'GET':
        user = request.args.get('user')
        # print(user)
        subs = find_pro("Book", "Van")
        # print(subs)
        col = db["Reader"]
        res = list(col.find({"email": user}))
        try:
            flname = res[0]['fname'] + " " + res[0]['lname']
        except:
            flname = ""
            user = None
        if user == "None" or user is None:
            return render_template('literarys.html', subs=subs, user="None")
        else:
            return render_template('literarys.html',subs = subs,user=user,flname=flname)

@app.route('/tables', methods=['GET', 'POST'])
def tables():
    if request.method == 'GET':
        admin = request.args.get('admin')
        prod = subs_find("Book")
        col = db["Admin"]
        if (admin is None) or (admin =="None") or (len(list(col.find({"name":str(admin)}))) == 0):
          return render_template('loginmanage.html', error="Please Login")
        else:
          return render_template('tables.html', admin=admin, prod=prod)


@app.route('/form-common', methods=['GET', 'POST'])
def form_common():
  if request.method == 'GET':
    alert = ""
    admin = request.args.get('admin')
    col = db["Admin"]
    if (admin is None) or (admin =="None") or (len(list(col.find({"name":str(admin)}))) == 0):
      return render_template('loginmanage.html', error="Please Login")
    else:
      return render_template('form-common.html',admin=admin,alert=alert)

@app.route('/form-common?admin=<admin>', methods=['GET', 'POST'])
def after_add(admin):
  if request.method == 'POST':
    mon = request.form['select_subs'].strip()
    name = request.form['name'].strip()
    nxb = request.form['nxb'].strip()
    tacgia = request.form['tacgia'].strip()
    language = request.form['language'].strip()
    link = request.form['link'].strip()
    gia = request.form['gia'].strip()
    giagiam = request.form['giagiam'].strip()
    description = request.form['description'].strip()
    thoihan = request.form['thoihan'].strip()
    col = db["Book"]
    a = str(int(col.count()) + 1)
    col.insert({"id": a, "mon": mon, "name": name, "tacgia": tacgia, "gia": gia, "nxb": nxb, "giagiam" : giagiam, "language":language, "link":link, "thoihan":thoihan,"description":description})
    alert = "abcdsdsd"
    return render_template('form-common.html',admin=admin,alert=alert)

@app.route('/subjects', methods=['GET', 'POST'])
def subjects():
    if request.method == 'GET':
        user = request.args.get('user')
        # print(user)
        subs = subs_find("Book")
    # print(subs)
        col = db["Reader"]
        res = list(col.find({"email": user}))
        try:
            flname = res[0]['fname'] + " " + res[0]['lname']
        except:
            flname = ""
            user = None
        if user == "None" or user is None:
            return render_template('subjects.html', subs=subs, user="None")
        else:
            return render_template('subjects.html',subs=subs,user=user,flname=flname)

@app.route('/subjects?user=<user>', methods=['GET', 'POST'])
def filter_subjects(user):
    if request.method == 'POST':
        # print(user)
        try:
            mon = request.form['mon']
        except:
            mon = ""
        try:
            thoihan = request.form['time_limit']
        except:
            thoihan = ""
        try:
            language = request.form['language']
        except:
            language = ""
        print(mon)
        subs = filter_book(mon,thoihan,language)
        print(subs)
        col = db["Reader"]
        res = list(col.find({"email": user}))
        try:
            flname = res[0]['fname'] + " " + res[0]['lname']
        except:
            flname = ""
            user = None
        if user == "None" or user is None or user == "" or len(res)==0:
            return render_template('subjects.html', subs=subs, user="None")
        else:
            return render_template('subjects.html',subs=subs,user=user,flname=flname)

@app.route('/shop', methods=['GET', 'POST'])
def shop():
  subs = subs_find("Book")
  return render_template('shop.html',subs = subs)

@app.route('/single_product', methods=['GET', 'POST'])
def single_product():
  if request.method == 'GET':
    # book = str(request.args.get('book')).strip()
    user = str(request.args.get('user')).strip()
    col = db["Book"]
    book = user.split("?")[1]
    book = book.split("=")[1]
    subs = list(col.find({'name': {'$regex':str(book)}} ))
    user = user.split("?")[0]
    col2 = db["Reader"]
    res = list(col2.find({"email": user}))
    try:
        flname = res[0]['fname'] + " " + res[0]['lname']
    except:
        flname = ""
        user = None
    if user == "None" or user is None:
        return render_template('single_product.html', subs=subs, user="None")
    else:
        return render_template('single_product.html', subs=subs, user=user, flname=flname)


@app.route('/payment', methods=['GET', 'POST'])
def payment():
  return render_template('payment.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  col = db['Reader']
  error = None
  user = "None"
  if request.method == 'POST':
      # print(request.form['username'])
      try:
          if len(list(col.find({"email": str(request.form['username']), "pass": str(request.form['password'])}))) == 0:
              error = "Invalid user, please try again!"
          else:
              a = list(col.find({"email": str(request.form['username']), "pass": str(request.form['password'])}))
              print(a)
              return redirect(url_for('index', user=request.form['username']))
      except:
          email = request.form['email']
          fname = request.form['firstname']
          lname = request.form['lastname']
          password = request.form['passwd']
          col.insert({"email": email, "fname": fname, "lname": lname, "pass": password})
          print("sucess")
          error = "Register successful, Please login!"
  return render_template('login.html',error =error,user = user)

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'GET':
        user = request.args.get('user')
        print(user)
        col = db["Reader"]
        res = list(col.find({"email": user}))
        try:
            flname = res[0]['fname'] + " " + res[0]['lname']
        except:
            flname = ""
            user = None
        if user == "None" or user is None:
            return render_template('about.html', user="None")
        else:
            return render_template('about.html',user=user,flname=flname)

@app.route('/search?user=<user>', methods=['GET', 'POST'])
def search(user):
    if request.method == 'POST':
        query = request.form['Search'].strip()
        print(query)
        query1 = query.lower()
        col = db['Book']
        subs = list(col.find({'name': {'$regex': query1}}))
        subs2 = list(col.find({'tacgia': {'$regex': query1}}))
        print(subs)
        query2 = query1.capitalize()
        subs1 = list(col.find({'name': {'$regex': query2}}))
        subs3 = list(col.find({'tacgia': {'$regex': query2}}))
        print(query2)
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
        print(subs)
        col=db["Reader"]
        res = list(col.find({"email": user}))
        try:
            flname = res[0]['fname'] + " " + res[0]['lname']
        except:
            flname = ""
            user = None
        if user == "None" or user is None:
            return render_template('search.html', user="None",subs=subs, query=query)
        else:
            return render_template('search.html',user=user, flname=flname, subs=subs, query=query)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'GET':
        user = request.args.get('user')
        print(user)
        col = db["Reader"]
        res = list(col.find({"email": user}))
        try:
            flname = res[0]['fname'] + " " + res[0]['lname']
        except:
            flname = ""
            user = None
        if user == "None" or user is None:
            return render_template('checkout.html', user="None")
        else:
            return render_template('checkout.html',user=user,flname=flname)
    if request.method == 'POST':
        return render_template('checkout.html', user="None")

@app.route('/law', methods=['GET', 'POST'])
def law():
    if request.method == 'GET':
        user = request.args.get('user')
        print(user)
        col = db["Reader"]
        res = list(col.find({"email": user}))
        try:
            flname = res[0]['fname'] + " " + res[0]['lname']
        except:
            flname = ""
            user = None
        if user == "None" or user is None:
            return render_template('law.html', user="None")
        else:
            return render_template('law.html',user=user,flname=flname)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        user = request.args.get('user')
        print(user)
        col = db["Reader"]
        res = list(col.find({"email": user}))
        try:
            flname = res[0]['fname'] + " " + res[0]['lname']
        except:
            flname = ""
            user = None
        if user == "None" or user is None:
            return render_template('contact.html', user="None")
        else:
            return render_template('contact.html',user=user,flname=flname)
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'GET':
        admin = str(request.args.get('admin')).strip()
        print(admin)
        col = db["Book"]
        ids = admin.split("?")[1]
        ids = ids.split("=")[1]
        subs = list(col.find({'id': ids} ))
        admin = admin.split("?")[0]
        col = db['Admin']
        # print(subs[0]['id'])
        if (admin is None) or (admin =="None") or (len(list(col.find({"name":str(admin)}))) == 0):
          return render_template('loginmanage.html', error="Please Login")
        else:
          return render_template('edit.html', admin = admin, subs=subs)

@app.route('/edit?admin=<admin>?id=<id>', methods=['GET', 'POST'])
def after_edit(admin,id):
  if request.method == 'POST':
    mon = request.form['select_subs'].strip()
    name = request.form['name'].strip()
    nxb = request.form['nxb'].strip()
    tacgia = request.form['tacgia'].strip()
    language = request.form['language'].strip()
    link = request.form['link'].strip()
    gia = request.form['gia'].strip()
    giagiam = request.form['giagiam'].strip()
    description = request.form['description'].strip()
    thoihan = request.form['thoihan'].strip()
    col = db["Book"]
    print(admin,id)
    col.update_one({"id": id}, {"$set": {"mon": mon, "name": name, "tacgia": tacgia, "gia": gia, "nxb": nxb, "giagiam" : giagiam, "language":language, "link":link, "thoihan":thoihan,"description":description}})
    # print("sucess")
    alert = "Sucess"
    return render_template('edit.html',admin=admin,alert=alert)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'GET':
        admin = str(request.args.get('admin')).strip()
        # print(admin)
        col = db["Book"]
        ids = admin.split("?")[1]
        ids = ids.split("=")[1]
        subs = list(col.find({'id': str(ids)} ))
        admin = admin.split("?")[0]
        col = db['Admin']
        print(subs[0]['id'])
        if subs[0]['mon'] == "Toan":
            subs[0]['mon'] = "Math"
        elif subs[0]['mon'] == "Tin":
            subs[0]['mon'] = "Informatics"
        elif subs[0]['mon'] == "Ly":
            subs[0]['mon'] = "Physic"
        elif subs[0]['mon'] == "Van":
            subs[0]['mon'] = "Literarys"
        else:
            subs[0]['mon'] = "Chemistry"
        if (admin is None) or (admin =="None") or (len(list(col.find({"name":str(admin)}))) == 0):
          return render_template('loginmanage.html', error="Please Login")
        else:
          return render_template('delete.html', admin = admin, subs=subs)

@app.route('/delete?admin=<admin>?id=<id>', methods=['GET', 'POST'])
def after_delete(admin,id):
  if request.method == 'POST':
    col = db["Book"]
    col.delete_one({'id':id})
    alert = "Sucess"
    return render_template('delete.html',admin=admin,alert=alert)

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    datas = request.args.get('q')
    query1 = datas.lower()
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
            print(i['tacgia'])
            autosubs.append(i['tacgia'].strip())
        if i['language'] not in autosubs:
            autosubs.append(i['language'])
    # print(autosubs)
    matching1 = [s for s in autosubs if query1 in s]
    matching2 = [s for s in autosubs if query2 in s]
    for i in matching1:
        if i not in matching2:
            matching2.append(i)
    # print(matching2)
    return jsonify(matching_results=matching2)

if __name__ == "__main__":
    app.run(debug=True)
