
#SQL practice exercice with Python

import psycopg2

database = 'evolveu'

# Simple routine to run a query on a database and print the results:
def client( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT name, email, city, birth_year FROM clients" )
    rows = cur.fetchall()
    # for name, email, city, birth_year in cur.fetchall() :
    #     print (name,' ', email,' ', city,' ', birth_year)
    print(rows[1])


myConnection = psycopg2.connect(dbname=database )
client( myConnection )
myConnection.close()