import psycopg2

connection = psycopg2.connect(database="sawibrah", user="sawibrah", password="sawibrah") #, host="localhost", port="5432"

cursor = connection.cursor()

cursor = connection.cursor()
# user_id serial PRIMARY KEY,
# firsname varchar(32),
# lastname varchar(32),
# username VARCHAR(32),
# password VARCHAR(32),
# email VARCHAR(32)
cursor.execute(
    """INSERT INTO users(
        firsname,
        lastname,
        username,
        password,
        email
    )VALUES(
        'Ndiaye',
        'Khady',
        'Aya',
        'ilovesawadogo',
        'khady@gmail.com'
    );"""
)

cursor.execute(
    """INSERT INTO users(
        firsname,
        lastname,
        username,
        password,
        email
    )VALUES(
        'Yakubu',
        'Khadija',
        'khadi',
        'goodgirl',
        'khady;yakubu@gmail.com'
    );"""
)
print("Data insertion was successfull!")
connection.commit()
cursor.close()
connection.close()