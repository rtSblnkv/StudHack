import sqlite3
import database

''' cathedras
(
    cathedra_id PRIMARY KEY NOT NULL,
    name TEXT NOT NULL
)'''
def insert_cathedra(cathedra_id,name):
    try:
        sqlite_connection = database.create_connection()
        cursor = sqlite_connection.cursor()
        cursor.execute('''INSERT INTO cathedras VALUES (?,?)''',(cathedra_id,name))
        sqlite_connection.commit()
    except Exception as exp:
        print(exp)
    finally:
        database.close_connection(sqlite_connection)

''' teachers
(id INTEGER PRIMARY KEY NOT NULL, 
name TEXT,
cathedra_id INTEGER,
location TEXT,
mail TEXT NOT NULL,
FOREIGN KEY (cathedra_id) REFERENCES cathedras(cathedra_id))'''

def insert_teacher(id,name,cathedra_id,location,mail):
    try:
        sqlite_connection = database.create_connection()
        cursor = sqlite_connection.cursor()
        cursor.execute('''INSERT INTO teachers VALUES (?,?,?,?,?)''',(id,name,cathedra_id,location,mail))
        sqlite_connection.commit()
    except Exception as exp:
        print(exp)
    finally:
        database.close_connection(sqlite_connection)
  
''' students
(chatid INTEGER PRIMARY KEY NOT NULL,
 surname TEXT NOT NULL,
 group_number INTEGER)'''
def insert_student(id,name,group_number):
    try:
        sqlite_connection = database.create_connection()
        cursor = sqlite_connection.cursor()
        cursor.execute('''INSERT INTO students VALUES(?,?,?)''',(id,name,group_number))
        sqlite_connection.commit()
    except Exception as exp:
        print(exp)
    finally:
        database.close_connection(sqlite_connection)

'''science_works 
(work_id INTEGER PRIMARY KEY NOT NULL,
 work_name TEXT,
 teacher_id INTEGER NOT NULL,
 FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
)'''
def insert_scienceWork(work_id,work_name,teacher_id):
    try:
        sqlite_connection = database.create_connection()
        cursor = sqlite_connection.cursor()
        cursor.execute('''INSERT INTO science_works VALUES (?,?,?)''',(work_id,work_name,teacher_id))
        sqlite_connection.commit()
    except Exception as exp:
        print(exp)
    finally:
        database.close_connection(sqlite_connection)







