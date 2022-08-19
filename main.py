# https://proglib.io/p/kak-podruzhit-python-i-bazy-dannyh-sql-podrobnoe-rukovodstvo-2020-02-27
import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
    except Error as e:
        print(f'The error {e} ocurred')
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f'The error {e} occurred')
    return cursor


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


connection = create_connection('db.sqlite')
create_division_table = """
CREATE TABLE IF NOT EXISTS division (
id_division INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
count TEXT NOT NULL,
type TEXT NOT NULL
);
"""
execute_query(connection, create_division_table)
create_doctor_table = """
CREATE TABLE IF NOT EXISTS doctor(
id_doctor INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
post TEXT NOT NULL,
work_exp TEXT NOT NULL
);
"""
execute_query(connection, create_doctor_table)
create_client_table = """
CREATE TABLE IF NOT EXISTS client(
id_client INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age TEXT NOT NULL,
diagnosis TEXT NOT NULL,
id_division INTEGER NOT NULL,
id_doctor INTEGER NOT NULL,
FOREIGN KEY (id_division) REFERENCES division (id_division),
FOREIGN KEY (id_doctor) REFERENCES doctor (id_doctor)
);
"""
execute_query(connection, create_client_table)


