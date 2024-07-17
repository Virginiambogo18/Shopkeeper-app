import sqlite3

def create_connection():
    conn = sqlite3.connect('shopkeeper.db')
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT,
                      password TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                      price REAL,
                      quantity INTEGER)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS sales (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      product_id INTEGER,
                      quantity INTEGER,
                      total REAL,
                      date TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                      email TEXT,
                      phone TEXT)''')
    conn.commit()
    conn.close()
