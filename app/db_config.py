import psycopg2
import os

db_url = os.getenv('DATABASE_URL')
print(db_url)

def connection(url):
    connect = psycopg2.connect(url)
    return connect


def init_db():
    connect = connection(db_url)
    return connect


def create_tables():
    conn = init_db()
    cur = conn.cursor()
    queries = tables()

    for query in queries:
        cur.execute(query)
    conn.commit()

def destroy_tables():
	conn = connection(db_url)
	cur = conn.cursor()
	parcels = "DROP TABLE IF EXISTS parcels CASCADE;"
	users = "DROP TABLE IF EXISTS users CASCADE;"
	queries = [parcels, users]
	for query in queries:
		cur.execute(query)
	conn.commit()

def tables():
    
	table1 = """CREATE TABLE IF NOT EXISTS users (
	    user_id SERIAL PRIMARY KEY UNIQUE NOT NULL,
	    user_name varchar (50) NOT NULL,
	    email varchar (50) NOT NULL,
	    role varchar (25) NOT NULL,
	    password varchar (100) NOT NULL,
        date_created timestamp with time zone DEFAULT ('now'::text)::date
	    )"""

	
	table2 = """CREATE TABLE IF NOT EXISTS parcels (
	    parcel_id SERIAL PRIMARY KEY UNIQUE NOT NULL,
	    parcel_name varchar (250) NOT NULL,
		parcel_weight varchar NOT NULL,
		pick_location varchar (150) NOT NULL,
		destination varchar (150) NOT NULL,
		present_location varchar (150) NOT NULL,
		consignee_name varchar (100) NOT NULL,
		consignee_no varchar NOT NULL,
        order_status varchar (25) NOT NULL,
	    cost varchar NOT NULL,
		user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE CASCADE
        )"""

	queries = [table1, table2]
	return queries
