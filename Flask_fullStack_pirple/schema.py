import psycopg2

connection = psycopg2.connect(database="sawibrah", user="sawibrah", password="sawibrah") #, host="localhost", port="5432"

print("Database opened successfully")
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE users(
        user_id serial PRIMARY KEY,
        firsname varchar(32),
        lastname varchar(32),
        username VARCHAR(32),
        password VARCHAR(32),
        email VARCHAR(32)
    );"""
)

print("Table created successfully")

connection.commit()
cursor.close()
connection.close()


