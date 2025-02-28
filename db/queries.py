# queries.py

TABLE_registered = """
    CREATE TABLE IF NOT EXISTS registered (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    age TEXT,
    gender TEXT,
    date_age TEXT,
    email TEXT,
    photo TEXT
    )
"""


INSERT_TABLE_registered = """
    INSERT INTO registered (fullname, age, gender, date_age, email, photo)
    VALUES (?, ?, ?, ?, ?, ?)
"""


CREATETABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    size TEXT,
    price TEXT,
    photo TEXT,
    product_id TEXT
    )
"""

INSERT_store = """
    INSERT INTO store (name_product, size, price, photo, product_id)
    VALUES (?, ?, ?, ?, ?)
"""

CREATETABLE_store_detail = """
    CREATE TABLE IF NOT EXISTS store_detail (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id TEXT,
    info_product TEXT,
    category TEXT
    )
"""

INSERT_store_detail = """
    INSERT INTO store_detail (product_id, info_product, category)
    VALUES (?, ?, ?)
"""