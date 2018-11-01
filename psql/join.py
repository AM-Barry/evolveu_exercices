#SQL practice exercice with Python

import psycopg2

database = 'evolveu'

#class functions 
def get_client_tuple(conn):
    cur = conn.cursor()
    clients = []
    cur.execute("SELECT name, credits, month from clients c join credits d on c.client_id= d.client_id")
    for name, credits, month in cur.fetchall() :
        clients.append([name, credits, month])
    return clients

# All clients function:
def get_all_clients( conn ) :
    cur = conn.cursor()

    clients = []
    cur.execute( "SELECT name FROM clients" )
    for name in cur.fetchall():
    	clients.append(name)

    return clients
   
# myConnection = psycopg2.connect(dbname=database )
# get_all_clients( myConnection )
# myConnection.close()

# #Clients with July credits function
def client_july( conn ) :
    cur = conn.cursor()

    julyCredits = []

    cur.execute( "SELECT name, credits, month from clients c full join credits d on c.client_id= d.client_id where d.month='2018-07'" )
    for name, credits, month in cur.fetchall() :
        julyCredits.append([name, credits, month])

    return julyCredits


# myConnection = psycopg2.connect(dbname=database )
# print(client_july( myConnection ))
# myConnection.close()


#Clients with no credits
def client_nocredits( conn ) :
    cur = conn.cursor()

    noCredits = []
    cur.execute( "SELECT name, credits, month from clients c full join credits d on c.client_id= d.client_id where d.credits is Null" )
    for name, credits, month in cur.fetchall() :
        noCredits.append([name, credits, month])

    return noCredits
   
# myConnection = psycopg2.connect(dbname=database )
# print(client_nocredits( myConnection ))
# myConnection.close()

# #Credits with no clients functions
def credits_noclients( conn ):
	cur = conn.cursor()
	noClients = []
	cur.execute( "SELECT name, credits, month from clients c full join credits d on c.client_id= d.client_id where c.name is Null" )
	for name, credits, month in cur.fetchall():
		noClients.append([name, credits, month])
	return noClients
# myConnection = psycopg2.connect(dbname=database )
# print(credits_noclients( myConnection ))
# myConnection.close()
