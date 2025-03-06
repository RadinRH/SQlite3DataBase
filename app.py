import sqlite3

def db_manager_single(q):
    connection = sqlite3.connect('myshop.db')
    cursor = connection.cursor()
    cursor.execute(q)
    connection.commit()
    connection.close()

def db_manager_many(q, data):
    connection = sqlite3.connect('myshop.db')
    cursor = connection.cursor()
    cursor.executemany(q, data)
    connection.commit()
    connection.close()


# create user database
q = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT NOT NULL UNIQUE,
        full_name TEXT NOT NULL,    
        password TEXT NOT NULL
    )
'''
# db_manager_single(q)


# Insert into users
q = '''
    INSERT INTO users (user_name, full_name, password)
    VALUES ("jondo", "john doe", "123")
'''

q = '''
    INSERT INTO users (user_name, full_name, password)
    VALUES ("radin", "hedayati", "321")
'''
# db_manager_single(q)


# Insert multiple value to user table
data = [
    ("ali@gmail.com", "Ali Akbari", "123"),
    ("sara@gmail.com", "Sara Ahadi", "321"),
    ("ben@gmail.com", "Ben Mira", "333"),
    ("saeed@gmail.com", "Saeed Sobhan", "4444"),
    ("maryam@gmail.com", "Maryam Imani", "1111"),
]

q = '''
    INSERT INTO users (user_name, full_name, password)
    VALUES(?, ?, ?)
'''
db_manager_many(q, data)

























