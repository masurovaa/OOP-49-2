import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE  IF NOT EXISTS users(
fio VARCHAR (100) NOT NULL,
age INTEGER NOT NULL,
hobby TEXT
)
""")

#Cursor.execute("""
#CREATE TABLE  IF NOT EXISTS users(
#fio VARCHAR (100) NOT NULL, - 100 МАХ СИМВОЛОВ,  НЕ МОЖЕТ БЫТЬ ПУСТЫМ
#age INTEGER NOT NULL, - ...  НЕ МОЖЕТ БЫТЬ ПУСТЫМ
# #hobby TEXT - БЕЗ ОГРАНИЧЕНИЯ
#)
#""")

connect.commit()

#CRUD - create, Reade, Update, Delete

def add_user(fio, age, hobby=""):
    cursor.execute('INSERT INTO users(fio, age, hobby) VALUES (?, ?, ?)', (fio, age, hobby))
    connect.commit()
    print(f'Пользователь {fio} добавлен(а)')

#add_user('Масурова Алтынай', 28, 'РИСОВАТЬ')



def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if users:
        print(f'Список всех пользователей:')
        for user in users:
            print(f'FIO: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}')
    else:
        print(f'Список ползователей пустой')

get_all_users()

connect.close()



















