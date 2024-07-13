
#!/bin/usr/python3

import sqlite3
from contextlib import contextmanager


"""
Day 6 - Code challenge 

Create a custom context manager for a simple 
database connection simulation.
"""

CREATE_TABLE_SQL = '''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL
    )
'''

INSERT_BOOKS_SQL = '''
    INSERT INTO books (title, author) VALUES 
    (?, ?),
    (?, ?)
'''

SELECT_ALL_BOOKS_SQL = 'SELECT * FROM books'

@contextmanager
def database_connection(path: str):
    connection = sqlite3.connect(path)
    try:
        yield connection
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()

def create_table(connection):
    with connection:
        connection.execute(CREATE_TABLE_SQL)

def insert_books(connection, books):
    with connection:
        connection.executemany(INSERT_BOOKS_SQL, books)

def fetch_all_books(connection):
    with connection:
        return connection.execute(SELECT_ALL_BOOKS_SQL).fetchall()

def main():
    books_to_insert = [
        ('If Tomorrow Comes', 'Sidney Sheldon'),
        ('The Lincoln Lawyer', 'Michael Connelly')
    ]

    with database_connection(':memory:') as conn:
        create_table(conn)
        insert_books(conn, books_to_insert)
        all_books = fetch_all_books(conn)
        
        for book in all_books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}")

if __name__ == '__main__':
    main()
