from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import jsonify
from ConfigParser import SafeConfigParser
import MySQLdb

app = Flask(__name__)
parser = SafeConfigParser()
user = None
password = None
db = None
host = None

try:
    parser.read("config.ini")
    user = parser.get('database', 'username')
    password = parser.get('database', 'password')
    db = parser.get('database', 'name')
    host = parser.get('database', 'host')
    
except:
    print "ERROR WITH DATABASE CALL"
    
@app.route("/")
def hello1():
    return render_template("index.html")

@app.route("/login/")
def hello2():
    return render_template("login.html")
    
@app.route("/chat/")
def hello3():
    return render_template("chat.html")

@app.route("/_confirm", methods = ['POST'])
def checkEmailFlightId():
	email = request.form["email"]
	flightId = request.form["flightId"]
	database = MySQLdb.connect(host, user, password, db)
	database.query("SELECT * FROM flightdata")
	r = database.store_result()
	numRows = r.num_rows()
	result = "False"
	for i in range(0, numRows):
		currEmail, currFlightId = r.fetch_row()[0][0:2]
		if email == currEmail and flightId == currFlightId:
			result = "True"
	print result
	return result

if __name__ == "__main__":
    app.run()
