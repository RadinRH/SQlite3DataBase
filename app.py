import sqlite3

def db_manager(q):
    connection = sqlite3.connect('myshop.db')
    cursor = connection.cursor()
    cursor.execute(q)
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
db_manager(q)



# Insert into users
q = '''
    INSERT INTO users (user_name, full_name, password)
    VALUES ("jondo", "john doe", "123")
'''


q = '''
    INSERT INTO users (user_name, full_name, password)
    VALUES ("radin", "hedayati", "321")
'''
db_manager(q)


























