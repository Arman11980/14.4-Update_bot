import sqlite3
import asyncio
connection = sqlite3.connect('products.db')
cursor= connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    '''),
    connection.commit()

initiate_db()

def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    products=cursor.execute('SELECT * FROM Products').fetchall()
    connection.commit()
    return products


connection.commit()
connection.close()