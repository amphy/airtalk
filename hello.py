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
    
@app.route("/chat/", methods = ['POST'])
def hello3():
    return render_template("chat.html")

@app.route("/_confirm", methods = ['POST'])
def checkEmailFlightId():
	email = request.form["email"]
	flightId = request.form["flightId"]
	database = MySQLdb.connect(host, user, password, db)
	database.query("""SELECT * FROM flightdata""")
	r = database.store_result()
	numRows = r.num_rows()
	for i in range(0, numRows):
		currEmail = r.fetch_row()[0][0]
		currFlightId = r.fetch_row()[0][1]
		if email == currEmail and flightId == currFlightId:
			return "True"
	return "False"

if __name__ == "__main__":
    app.run()
