from flask import Flask, render_template, url_for, redirect, request
from pymongo import MongoClient

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
    		return redirect(url_for('dashboard'))
    return render_template('loginmanage.html', error=error)

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
  return render_template('dashboard.html')

@app.route('/math', methods=['GET', 'POST'])
def math():
  return render_template('math.html')

@app.route('/physical', methods=['GET', 'POST'])
def physical():
  return render_template('physical.html')

@app.route('/chemistry', methods=['GET', 'POST'])
def chemistry():
  return render_template('chemistry.html')

@app.route('/informatics', methods=['GET', 'POST'])
def informatics():
  return render_template('informatics.html')

@app.route('/literarys', methods=['GET', 'POST'])
def literarys():
  return render_template('literarys.html')

@app.route('/tables', methods=['GET', 'POST'])
def tables():
  return render_template('tables.html')

@app.route('/form-common', methods=['GET', 'POST'])
def form_common():
  return render_template('form-common.html')

@app.route('/charts', methods=['GET', 'POST'])
def charts():
  return render_template('charts.html')

@app.route('/calendar', methods=['GET', 'POST'])
def calendar():
  return render_template('calendar.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
  return render_template('chat.html')

@app.route('/shop', methods=['GET', 'POST'])
def shop():
  return render_template('shop.html')

@app.route('/single_product', methods=['GET', 'POST'])
def single_product():
  return render_template('single_product.html')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
  return render_template('payment.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  return render_template('login.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
  return render_template('about.html')

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
  return render_template('checkout.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    # col = db["book"]
    # a = list(col.find())
    col = db["book"]
    # i = ''
    a= list(col.find({}, {"_id": 0, "name": 1}))
    sug = []
    for i in a:
        sug.append(i['name'])
        # i = a
    return render_template('Test.html', a=a, sug = sug)

if __name__ == "__main__":
    app.run()
    app.debug = True