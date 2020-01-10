from flask import Flask, render_template, url_for, redirect, request, jsonify
from pymongo import MongoClient
from data import find_pro, count, subs_find, filter_book, data_auto, data_search, data_love

app = Flask(__name__)
myclient = MongoClient("mongodb://localhost:27017/")

db = myclient["Website"]
# print("sucess")

@app.route('/loginmanage', methods=['GET', 'POST'])
def loginmanage():
    col = db["Admin"]
    error = None
    if request.method == 'POST':
    	# print(request.form['username'])
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
    lbres = data_love()
    # print(lbres)
    try:
        flname = res[0]['fname'] + " " + res[0]['lname']
    except:
        flname = ""
        user = None
    if user == "None" or user is None or len(res) == 0:
        return render_template('index.html',user="None", lbres=lbres)
    else:
        return render_template('index.html', user=user,flname=flname, lbres=lbres)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
  if request.method == 'GET':
    admin = request.args.get('admin')
    count1 = count("Reader")
    count2 = count("Book")
    count3 = count("Admin")
    lb = subs_find("Love")
    nlb = []
    for i in lb:
        if i['id'] not in nlb:
            nlb.append(i['id'])
    count4 = len(nlb)
    col = db["Admin"]
    if (admin is None) or (admin =="None") or (len(list(col.find({"name":str(admin)}))) == 0):
      return render_template('loginmanage.html', error="Please Login")
    else:
      return render_template('dashboard.html', admin = admin, count1= count1, count2=count2,count3=count3, count4 = count4)

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
        if user == "None" or user is None or len(res) == 0:
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
        if user == "None" or user is None or len(res) == 0:
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
        if user == "None" or user is None or len(res) == 0:
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
        if user == "None" or user is None or len(res) == 0:
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
        if user == "None" or user is None or len(res) == 0:
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
        if user == "None" or user is None or len(res) == 0:
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
        # print(mon)
        subs = filter_book(mon,thoihan,language)
        # print(subs)
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

@app.route('/single_product', methods=['GET', 'POST'])
def single_product():
  if request.method == 'GET':
    # book = str(request.args.get('book')).strip()
    user = str(request.args.get('user')).strip()
    col = db["Book"]
    book = user.split("?")[1]
    book = book.split("=")[1]
    subs = list(col.find({'id': book}))
    user = user.split("?")[0]
    col2 = db["Reader"]
    res = list(col2.find({"email": user}))
    try:
        flname = res[0]['fname'] + " " + res[0]['lname']
    except:
        flname = ""
        user = None
    if user == "None" or user is None or len(res) == 0:
        return render_template('single_product.html', subs=subs, user="None")
    else:
        return render_template('single_product.html', subs=subs, user=user, flname=flname)


@app.route('/add', methods=['GET', 'POST'])
def add():
  if request.method == 'GET':
    # book = str(request.args.get('book')).strip()
    user = str(request.args.get('user')).strip()
    col = db["Book"]
    book = user.split("?")[1]
    book = book.split("=")[1]
    user = user.split("?")[0]
    col2 = db["Reader"]
    res = list(col2.find({"email": user}))
    try:
        flname = res[0]['fname'] + " " + res[0]['lname']
    except:
        flname = ""
        user = None
    if user == "None" or user is None or len(res) == 0:
        return render_template('login.html', user="None")
    else:
        col3 = db["Love"]
        rbook = list(col3.find({"id":res[0]['id']}))
        t = True
        for i in rbook:
            if book == i['idbook']:
                t = False
        if t == True:
            col3.insert({"id":res[0]['id'], "idbook":book})
        subs = list(col.find({"id":book}))
        return render_template('add.html', user=user, flname=flname, subs=subs)

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
              # print(a)
              return redirect(url_for('index', user=request.form['username']))
      except:
          email = request.form['email']
          fname = request.form['firstname']
          lname = request.form['lastname']
          password = request.form['passwd']
          ids = str(int(col.count()) + 1)
          col.insert({"id":ids, "email": email, "fname": fname, "lname": lname, "pass": password})
          # print("sucess")
          error = "Register successful, Please login!"
  return render_template('login.html',error =error,user = user)

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'GET':
        user = request.args.get('user')
        # print(user)
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
        # print(query)
        subs = data_search(query)
        col=db["Reader"]
        res = list(col.find({"email": user}))
        try:
            flname = res[0]['fname'] + " " + res[0]['lname']
        except:
            flname = ""
            user = None
        if user == "None" or user is None or len(res) == 0:
            return render_template('search.html', user="None",subs=subs, query=query)
        else:
            return render_template('search.html',user=user, flname=flname, subs=subs, query=query)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'GET':
        user = request.args.get('user')
        # print(user)
        col = db["Reader"]
        res = list(col.find({"email": user}))
        try:
            flname = res[0]['fname'] + " " + res[0]['lname']
        except:
            flname = ""
            user = None
        if user == "None" or user is None or len(res) == 0:
            return render_template('login.html', user="None", error = "Please login first!")
        else:
            col1 = db["Love"]
            col2 = db["Book"]
            resb = list(col1.find({"id":res[0]['id']}))
            blove = []
            for i in resb:
                blove.append(list(col2.find({"id":i["idbook"]}))[0])
            total = 0
            for i in blove:
                total = total + int(i['gia'].replace(".",""))
            lens = len(blove)
            return render_template('checkout.html',user=user, flname=flname, blove=blove, lens=lens, total=total)
@app.route('/checkout?user=<user>&book=<book>', methods=['GET', 'POST'])
def after_checkout(user,book):
    if request.method == 'POST':
        # print(user)
        col = db["Reader"]
        res = list(col.find({"email": user}))
        try:
            flname = res[0]['fname'] + " " + res[0]['lname']
        except:
            flname = ""
            user = None
        if user == "None" or user is None or len(res) == 0:
            return render_template('login.html', user="None")
        else:
            col1 = db["Love"]
            users = res[0]['id']
            col1.delete_one({'id':users, "idbook":book})
            col2 = db["Book"]
            resb = list(col1.find({"id":res[0]['id']}))
            blove = []
            for i in resb:
                blove.append(list(col2.find({"id":i["idbook"]}))[0])
            total = 0
            for i in blove:
                total = total + int(i['gia'].replace(".",""))
            lens = len(blove)
            print(user)
            return render_template('checkout.html',user=user,flname=flname, blove=blove, lens=lens, total=total)

@app.route('/law', methods=['GET', 'POST'])
def law():
    if request.method == 'GET':
        user = request.args.get('user')
        # print(user)
        col = db["Reader"]
        res = list(col.find({"email": user}))
        try:
            flname = res[0]['fname'] + " " + res[0]['lname']
        except:
            flname = ""
            user = None
        if user == "None" or user is None or len(res) == 0:
            return render_template('law.html', user="None")
        else:
            return render_template('law.html',user=user,flname=flname)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        user = request.args.get('user')
        # print(user)
        col = db["Reader"]
        res = list(col.find({"email": user}))
        try:
            flname = res[0]['fname'] + " " + res[0]['lname']
        except:
            flname = ""
            user = None
        if user == "None" or user is None or len(res) == 0:
            return render_template('contact.html', user="None")
        else:
            return render_template('contact.html',user=user,flname=flname)
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'GET':
        admin = str(request.args.get('admin')).strip()
        # print(admin)
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
    # print(admin,id)
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
        # print(subs[0]['id'])
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
    matching2 = data_auto(datas)
    return jsonify(matching_results=matching2)

# @app.route('/deletebl', methods=['GET','POST'])
# def deletebl():
#     print(book, ids)
#     return jsonify(matching_results=[])


if __name__ == "__main__":
    app.run(debug=True)
