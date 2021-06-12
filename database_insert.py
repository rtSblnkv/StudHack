import sqlite3


sqlite_connection=sqlite3.connect('science_works.db')
cursor = sqlite_connection.cursor()

''' students
(chatid INTEGER PRIMARY KEY NOT NULL,
 surname TEXT NOT NULL,
 group_number INTEGER)'''
''' cathedras
(
    cathedra_id PRIMARY KEY NOT NULL,
    name TEXT NOT NULL
)'''
''' teachers
(id INTEGER PRIMARY KEY NOT NULL, 
name TEXT,
cathedra_id INTEGER,
location TEXT,
mail TEXT NOT NULL,
FOREIGN KEY (cathedra_id) REFERENCES cathedras(cathedra_id))'''

'''science_works 
(work_id INTEGER PRIMARY KEY NOT NULL,
 work_name TEXT,
 teacher_id INTEGER NOT NULL,
 FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
)'''

cursor.execute('''INSERT INTO cathedras VALUES 
  (1,"Кафедра программных систем"),
  (2,"Сюда вставляй  ")''')
cursor.execute('''INSERT INTO teachers VALUES
  (1,"Додонова Наталья Леонидовна",1,"Кафедра ПС","dodonova@ssau.ru"),
  (2,"ФИО",1,"АДРЕС","ПОЧТА")''')
cursor.execute('''INSERT INTO students VALUES
  (1,"Черепанова Валерия"),
  (2,"Сабельников Артем")''')
cursor.execute('''INSERT INTO science_works VALUES
  (1,"Кластеризация сверхчисел",1),
  (2,"Название",1)''')

cursor.execute("SELECT * FROM cathedras,teachers,students,science_works")
with sqlite_connection:
    print(cursor.fetchall())


