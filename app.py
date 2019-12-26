from flask import Flask, render_template, url_for, redirect, request
from pymongo import MongoClient
from data import find_pro, count, subs_find

app = Flask(__name__)
myclient = MongoClient("mongodb://localhost:27017/")

db = myclient["Website"]
print("sucess")

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
  return render_template('index.html')

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
    subs = find_pro("Book","Toan")
    print(subs)
    return render_template('math.html', subs = subs)

@app.route('/physical', methods=['GET', 'POST'])
def physical():
    subs = find_pro("Book", "Ly")
    print(subs)
    return render_template('physical.html', subs = subs)

@app.route('/chemistry', methods=['GET', 'POST'])
def chemistry():
    subs = find_pro("Book", "Hoa")
    print(subs)
    return render_template('chemistry.html',subs = subs)

@app.route('/informatics', methods=['GET', 'POST'])
def informatics():
    subs = find_pro("Book", "Tin")
    print(subs)
    return render_template('informatics.html', subs = subs)

@app.route('/literarys', methods=['GET', 'POST'])
def literarys():
    subs = find_pro("Book", "Van")
    print(subs)
    return render_template('literarys.html',subs = subs)

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
    mon = request.form['select_subs']
    name = request.form['name']
    nxb = request.form['nxb']
    tacgia = request.form['tacgia']
    language = request.form['language']
    link = request.form['link']
    gia = request.form['gia']
    giagiam = request.form['giagiam']
    description = request.form['description']
    thoihan = request.form['thoihan']
    col = db["Book"]
    col.insert({"mon": mon, "name": name, "tacgia": tacgia, "gia": gia, "nxb": nxb, "giagiam" : giagiam, "language":language, "link":link, "thoihan":thoihan,"description":description})
    alert = "abcdsdsd"
    return render_template('form-common.html',admin=admin,alert=alert)

@app.route('/subjects', methods=['GET', 'POST'])
def subjects():
    subs = subs_find("Book")
    # print(subs)
    return render_template('subjects.html',subs=subs)

@app.route('/shop', methods=['GET', 'POST'])
def shop():
  subs = subs_find("Book")
  return render_template('shop.html',subs = subs)

@app.route('/single_product', methods=['GET', 'POST'])
def single_product():
  if request.method == 'GET':
    book = str(request.args.get('book')).strip()
    print(book)
    col = db["Book"]
    subs = list(col.find({'name': {'$regex':str(book)}} ))
    print(subs)

  return render_template('single_product.html',subs=subs)

@app.route('/payment', methods=['GET', 'POST'])
def payment():
  return render_template('payment.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  col = db['Reader']
  error = None
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
  return render_template('login.html',error =error)

@app.route('/about', methods=['GET', 'POST'])
def about():
  return render_template('about.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['Search']
        query1 = query.lower()
        col = db['Book']
        subs = list(col.find({'name': {'$regex': query1}} ))
        query2 = query1.capitalize()
        subs1 = list(col.find({'name': {'$regex': query2}} ))
        for i in subs1:
          subs.append(i)
        print(subs)
    return render_template('search.html', subs=subs, query=query)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
  return render_template('checkout.html')

@app.route('/law', methods=['GET', 'POST'])
def law():
  return render_template('law.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():

    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
