from flask import Flask, render_template
import join
from join import database
import psycopg2
 
#database = 'evolveu'

app = Flask(__name__)

@app.route("/")
def home():
   return render_template("home.html")

@app.route("/clients")
def allclients():
	myConnection = psycopg2.connect(dbname=database )
	clients = join.get_all_clients( myConnection )
	myConnection.close()
	return render_template("clients.html", clientslist=clients)

@app.route("/months")
def month_July():
	myConnection = psycopg2.connect(dbname=database )
	july_clients = join.client_july( myConnection )
	myConnection.close()
	return render_template("month.html", clientsjuly=july_clients)

@app.route("/nocredits")
def no_credits():
	myConnection = psycopg2.connect(dbname=database )
	nocredits = join.client_nocredits( myConnection )
	myConnection.close()
	return render_template("nocredit.html",nocredits=nocredits)

@app.route("/noclients")
def no_clients():
	myConnection = psycopg2.connect(dbname=database )
	noclient = join.credits_noclients( myConnection )
	myConnection.close()
	return render_template("noclient.html", noclients=noclient)






if __name__ == '__main__':
	app.run(debug=True)    
	