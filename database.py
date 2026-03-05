import sqlite3
import os

os.makedirs("data", exist_ok=True)

def create_db():

    conn = sqlite3.connect("data/products.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price INTEGER,
        rating TEXT,
        link TEXT,
        image TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_product(name, price, rating, link, image):

    conn = sqlite3.connect("data/products.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO products(name,price,rating,link,image)
    VALUES(?,?,?,?,?)
    """,(name,price,rating,link,image))

    conn.commit()
    conn.close()