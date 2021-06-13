import database

def del_scienceWorks(work_id):
    print('Deleting science_work')
    try:
        sqlite_connection = database.create_connection()
        cursor = sqlite_connection.cursor()
        cursor.execute(''' DELETE FROM science_works WHERE work_id = ? ''',(work_id,))
    except Exception as exp:
        print(exp)
    finally:
        database.close_connection(sqlite_connection)