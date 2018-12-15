import psycopg2

def connect():
    return psycopg2.connect(user= 'postgres', password= 'sharon96', database= 'zap-shoes', host= 'localhost')