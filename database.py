import sqlite3

def create_connection():
    try:       
        sqlite_connection = sqlite3.connect('science_works.db')
        print('Connection opened')
    except sqlite3.Error as error:
        print('Error!',error)
    finally:
        return sqlite_connection


def close_connection(sqlite_connection):
    if(sqlite_connection):
        sqlite_connection.close()
        print('Connection closed')


def create_tables():
    sql_connection = create_connection()
    cursor = sql_connection.cursor()
    cursor.execute(''' CREATE TABLE students
    (chatid INTEGER PRIMARY KEY NOT NULL,
    surname TEXT NOT NULL,
    group_number INTEGER)''')
    cursor.execute(''' CREATE TABLE cathedras
    (
        cathedra_id PRIMARY KEY NOT NULL,
        name TEXT NOT NULL
    )''')
    cursor.execute(''' CREATE TABLE teachers
    (id INTEGER PRIMARY KEY NOT NULL, 
    name TEXT,
    cathedra_id INTEGER,
    location TEXT,
    mail TEXT NOT NULL,
    FOREIGN KEY (cathedra_id) REFERENCES cathedras(cathedra_id))''')
    sql_connection.commit()
    close_connection(sql_connection)



    


