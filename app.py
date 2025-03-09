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

def db_manager_read(q):
    connection = sqlite3.connect('myshop.db')
    cursor = connection.cursor()
    cursor.execute(q)
    return cursor.fetchall()

# region create user database
q = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT NOT NULL UNIQUE,
        full_name TEXT NOT NULL,    
        password TEXT NOT NULL
    )
'''
# db_manager_single(q)

# endregion

# region Insert into users
q = '''
    INSERT INTO users (user_name, full_name, password)
    VALUES ("jondo", "john doe", "123")
'''

q = '''
    INSERT INTO users (user_name, full_name, password)
    VALUES ("radin", "hedayati", "321")
'''
# db_manager_single(q)

# endregion

# region Insert multiple value to user table
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
# db_manager_many(q, data)

# endregion

# region product database
q = '''
    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price TEXT NOT NULL,    
        description TEXT NULL default '',
        is_exist BOOLEAN NOT NULL default TRUE
    )
'''
# db_manager_single(q)

# endregion

# region insert data product

data = [
    ("tuna", 103),
    ("rice", 205),
    ("chips", 18),
    ("bread", 10),
    ("water", 7)
]

q = '''
    INSERT INTO product (name, price)
    VALUES (?, ?)
'''
# db_manager_many(q, data)


# endregion

# region creat invoice table

q = '''
    CREATE TABLE IF NOT EXISTS invoice (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product_id INTEGER,
        total REAL NOT NULL,    
        created_at TEXT NOT NULL DEFAULT current_timestamp,
        updated_at TEXT NOT NULL DEFAULT current_timestamp,
        FOREIGN KEY(user_id) REFERENCES user(id),
        FOREIGN KEY(product_id) REFERENCES product(id)
    )
'''
db_manager_single(q)

# endregion

# region insert multiple value in invoice table

data = [
    (1, 1, 300),
    (1, 3, 200),
    (2, 2, 100),
    (2, 3, 250),
    (4, 4, 220),
    (6, 2, 210),
    (6, 4, 280),
]

q = '''
    INSERT INTO invoice (user_id, product_id, total)
    VALUES (?, ?, ?)
'''
# db_manager_many(q,data)

# endregion

# region read from user table 

# q = "SELECT full_name FROM users"
# data = db_manager_read(q)

# for item in data :
#     print(item)

# endregion
    
# region read from product invoice table 
    
# q = "SELECT product_id, user_id FROM invoice"
# data = db_manager_read(q)

# for item in data:
#     print(item)

# endregion
    
# region join product, invoice  

# q = '''
#     SELECT users.full_name, product.name
#     FROM users
#     INNER JOIN invoice on invoice.user_id = users.id
#     INNER JOIN product on invoice.product_id = product.id
# '''

# data = db_manager_read(q)

# for item in data:
#     print(item)

# endregion

# region insert product_id from user_name (1)

# q = '''
#     SELECT users.full_name, product.name
#     FROM users
#     INNER JOIN invoice on invoice.user_id = users.id
#     INNER JOIN product on invoice.product_id = product.id
#     WHERE users.id = 1
# '''

# data = db_manager_read(q)

# for item in data:
#     print(item)

# endregion

# region update user_name
    
# data = db_manager_read(q)
# for item in data:
#     print(item)

q = '''
    UPDATE users 
    SET full_name = 'John Coe'
    WHERE id = 1
'''

# db_manager_single(q)

# endregion















