from flask import Flask, render_template, url_for, redirect, request
from pymongo import MongoClient

app = Flask(__name__)
myclient = MongoClient("mongodb://localhost:27017/")

db = myclient["Website"]
col = db["Admin"]
print("sucess")

@app.route('/loginmanage', methods=['GET', 'POST'])
def loginmanage():
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
    app.debug = True