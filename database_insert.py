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

def select_from(table):
    try:
        sqlite_connection = database.create_connection()
        cursor = sqlite_connection.cursor()
        cursor.execute('''SELECT * FROM {0}'''.format(table))
        with sqlite_connection:
            print(cursor.fetchall())
    except Exception as exp:
        print(exp)
    finally:
        database.close_connection(sqlite_connection)

def select_all():
    select_from('cathedras')
    select_from('students')
    select_from('teachers')
    select_from('science_works')

#def insert_cathedra(cathedra_id,name):
#def insert_teacher(id,name,cathedra_id,location,mail):
#def insert_scienceWork(work_id,work_name,teacher_id)
#def insert_student(id,name,group_number)

def insert():
    insert_student(1,'Черепанова Валерия',6207)
    insert_student(2,'Сабельников Артем',6314)
    insert_student(3,'Кузнецов Ярослав',6208)
    insert_student(4,'Прасолов Данила',6207)
#заполнение кафедр
    insert_cathedra(2,'Кафедра технической кибернетики')
    insert_cathedra(3,'Кафедра суперкомпьютеров и общей информатики')
    insert_cathedra(4,'Кафедра геоинформатики и информационной безопасности')
    insert_cathedra(5,'Кафедра информатики и вычислительной математики')
    insert_cathedra(6,'Кафедра алгебры и геометрии')
    insert_cathedra(7,'Кафедра прикладных математики и физики')
    insert_cathedra(8,'Кафедра математического моделирования в механике')
    insert_cathedra(9,'Кафедра дифференциальных уравнений и теории управления')
#кафедра технической кибернетики
    insert_teacher(1, 'Куприянов Александр Викторович', 2, '1 корпус, 401 к. или 335 к.', 'sau.yap@gmail.com')
    insert_teacher(2, 'Белоусов Александр Александрович', 2, '1 корпус, 334 к.', 'adark@narod.ru')
    insert_teacher(3, 'Савельев Дмитрий Андреевич', 2, '1 корпус, 404 к.', 'dmitrey.savelyev@yandex.ru')
    insert_teacher(4, 'Логанова Лилия Викторовна', 2, '1 корпус, 334 к.', 'lloganova@yandex.ru')
    insert_teacher(5, 'Хонина Светлана Николаевна', 2, '1 корпус, 401 к.', 'khonina.s.n@gmail.com')
    insert_teacher(6, 'Козлова Елена Сергеевна', 2, '1 корпус, 234а к.', 'kozlova.elena.s@gmail.com')
#кафедра суперкомпьютеров и общей информатики
    insert_teacher(7, 'Фурсов Владимир Алексеевич', 3, '15 корпус, 118 к.', 'fursov@ssau.ru')
    insert_teacher(8, 'Никоноров Артём Владимирович', 3, '15 корпус, 118 к. или 218 к.', 'artniko@gmail.com')
    insert_teacher(9, 'Гошин Егор Вячеславович', 3, '15 корпус, 119 к.', 'goshine@ssau.ru')
#кафедра геоинформатики и информационной безопасности
    insert_teacher(10, 'Сергеев Владислав Викторович', 4, '18 корпус, 615 к.', 'vserg@geosamara.ru')
    insert_teacher(11, 'Мясников Владислав Валерьевич', 4, '18 корпус, 605 к.', 'vmyas@geosamara.ru')
    insert_teacher(12, 'Кузнецов Андрей Владимирович', 4, '18 корпус, 605 к.', 'kuznetsoff.andrey@gmail.com')
#кафедра информатики и вычислительной математики
    insert_teacher(13, 'Семёнова Ирина Владимировна', 5, '22 корпус, 303 к.', 'semenirina@list.ru')
    insert_teacher(14, 'Русакова Маргарита Сергеевна', 5, '22 корпус, 303 к.', 'r.margarita@gmail.com')
    insert_teacher(15, 'Рубцова Татьяна Павловна', 5, '22 корпус, 303 к.', 'tr_2004@bk.ru')
    insert_teacher(16, 'Сироченко Владимир Прохорович', 5, '22 корпус, 303 к.', 'sirochenko.vp@ssau.ru')
#кафедра алгебры и геометрии
    insert_teacher(17, 'Севостьянова Виктория Владимировна', 6, '22 корпус, 406 к.', 'berlua@mail.ru')
#кафедра прикладных математики и физики
    insert_teacher(18, 'Головашкин Димитрий Львович', 7, '1 корпус, 402 к.', 'dimitriy.golovashkin@yandex.ru')
    insert_teacher(19, 'Гоголева Софья Юрьевна', 7, '1 корпус, 305 к.', 'gogoleva_s@mail.ru')
    insert_teacher(20, 'Барова Евгения Анатольевна', 7, '1 корпус, 305 к.', 'barova.ea@mail.ru')
#кафедра математического моделирования в механике
    insert_teacher(21, 'Степанова Лариса Валентиновна', 8, '22 корпус, 414 к.', 'Stepanova.lv@ssau.ru')
#кафедра дифференциальных уравнений и теории управления
    insert_teacher(22, 'Китаева Елена Викторовна', 9, '22 корпус, 415 к.', 'el_kitaeva@mail.ru')   
    insert_scienceWork(1, 'Разработка и исследование алгоритмов машинного обучения с применением нейронных сетей', 1)
    insert_scienceWork(4, 'Исследование и разработка методов извлечения больших данных и их анализа', 2)
    insert_scienceWork(7, 'Исследование алгоритмов обучения нейронных сетей для прогнозирования фондового рынка', 3)
    insert_scienceWork(56, 'Параллельные алгоритмы решения СЛАУ трехдиагонального вида', 4)
    insert_scienceWork(59, 'Моделирование и исследование дифракции на кольцевых фрактальных решётках', 5)
    insert_scienceWork(10, 'Моделирование фокусировки лазерного излучения многослойными цилиндрами', 6)
    insert_scienceWork(13, 'Разработка и исследование адаптивных технологий визуальной одометрии по последовательности кадров изображений в мобильных системах технического зрения', 7)
    insert_scienceWork(15, 'Создание платформы для мобильного гиперспектрометра', 8)
    insert_scienceWork(18, 'Построение панорамы по последовательности изображений', 9)
    insert_scienceWork(21, 'Исследование методов безызбыточного восстановления сигналов, переданных по каналу с ошибками', 10)
    insert_scienceWork(62, 'Методы подделок мультимедиа и методы их детектирования ', 11)
    insert_scienceWork(24, 'Автоматизированная система обнаружения ДТП на данных видеонаблюдения ', 12)
    insert_scienceWork(27, 'Исследование и реализация алгоритмов планирования движения робота', 13)
    insert_scienceWork(30, 'Распознавание контурных изображений методами оптики спиральных пучков в кардиологии', 14)
    insert_scienceWork(33, 'Применение глубоких каскадных нейронных сетей для решения задач восстановления изображения', 15)
    insert_scienceWork(36, 'Численное решение краевых задач для дифференциальных уравнений в нерегулярных областях', 16)
    insert_scienceWork(39, 'Циклические коды, исправляющие ошибки, в каналах связи с эрозией', 17)
    insert_scienceWork(42, 'Разработка параллельных, векторных и блочных алгоритмов решения сеточных уравнений', 18)
    insert_scienceWork(44, 'Решение плохо обусловленных задач наименьших квадратов с разреженными матрицами большой размерности', 19)
    insert_scienceWork(47, 'Задача Дирихле для уравнения смешанного типа со специальными условиями сопряжения', 20)
    insert_scienceWork(50, 'Определение материальных свойств с помощью многопоточного глубокого обучения на основе молекулярно-динамического моделирования', 21)
    insert_scienceWork(53, 'Разработка алгоритмов сплайн-аппроксимации функций с точечными особенностями', 22)

#insert_scienceWork(1,'Кластеризация данных',1)

select_all()





