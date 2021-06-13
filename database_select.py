import database

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

def get_cathedras():
    try:
        print('Get cathedras')
        sqlite_connection = database.create_connection()
        cursor = sqlite_connection.cursor()
        cursor.execute('''  SELECT * FROM cathedras''')
        with sqlite_connection:
            data = cursor.fetchall()
    except Exception as exp:
        print(exp)
    finally:
        database.close_connection(sqlite_connection)
        return data
  

def get_themes(cathedra_name):
    print ('Get Themes')
    try:
        sqlite_connection = database.create_connection()
        cursor = sqlite_connection.cursor()
        cursor.execute('''SELECT 
        work_name,work_id,teachers.id
        FROM science_works INNER JOIN teachers 
        ON science_works.teacher_id = teachers.id 
        WHERE teachers.cathedra_id = ?''',(get_cathedra_id(cathedra_name),))
        with sqlite_connection:
            data = cursor.fetchall()
            print(data)
    except Exception as exp:
        print(exp)
    finally:
        database.close_connection(sqlite_connection)
        return data

def get_cathedra_id(cathedra_name):
    try:
        sqlite_connection = database.create_connection()
        cursor = sqlite_connection.cursor()
        cursor.execute('''SELECT cathedra_id FROM cathedras where name = ? ''',(cathedra_name,))
        with sqlite_connection:
            data = cursor.fetchone()
    except Exception as exp:
        print(exp)
    finally:
        database.close_connection(sqlite_connection)
        return data[0]


def get_teacher_themes(teacherId):
    print ('Getting teacher Themes')
    try:
        sqlite_connection = database.create_connection()
        cursor = sqlite_connection.cursor()
        cursor.execute('''SELECT * FROM science_works WHERE teacher_id = ?''',(teacherId,))
        with sqlite_connection:
            data = cursor.fetchone()
    except Exception as exp:
        print(exp)
    finally:
        database.close_connection(sqlite_connection)
        return data

def get_teacher(teacher_id):
    print ('Getting teacher')
    try:
        sqlite_connection = database.create_connection()
        cursor = sqlite_connection.cursor()
        cursor.execute(''' SELECT * FROM teachers WHERE id = ?''',(teacher_id, ))
        with sqlite_connection:
            data = cursor.fetchone()
        print(data)
    except Exception as exp:
        print(exp)
    finally:
        database.close_connection(sqlite_connection)
        return data

def get_teachers_ids():
    print ('Getting teacher_ids')
    result = list()
    try:
        sqlite_connection = database.create_connection()
        cursor = sqlite_connection.cursor()
        cursor.execute(''' SELECT id FROM teachers ''')
        with sqlite_connection:
            data = cursor.fetchall()
        for item in data:
            result.append(item[0])
    except Exception as exp:
        print(exp)
    finally:
        database.close_connection(sqlite_connection)
        return result

get_themes('Кафедра технической кибернетики')