import sqlite3 as sql

DB_NAME = "Inventario.db"

def get_connetion():
    conn = sql.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn
