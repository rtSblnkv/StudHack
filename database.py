import sqlite3


'''try:
    
except sqlite3.Error as error:
    print('Error!',error)
finally:
    if(sqlite_connection):
        sqlite_connection.close()
        print('Close connection')'''

sqlite_connection=sqlite3.connect('science_works.db')
cursor = sqlite_connection.cursor()

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
cursor.execute('''CREATE TABLE science_works 
(work_id INTEGER PRIMARY KEY NOT NULL,
 work_name TEXT,
 teacher_id INTEGER NOT NULL,
 FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
)''')




