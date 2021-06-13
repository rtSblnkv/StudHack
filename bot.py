from typing import List
from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, message
import logging
import config
import sqlite3
import keyBoard
import texts
import re
import database_select as ds
import database_insert as di
import database_delete as dd



bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
themes = list()
paswordCheckActivate = False
addTheme = False
registration = False

@dp.message_handler(commands=['start'])
async def send_hello_answer(message:types.Message):
    await message.answer(texts.start_text,reply_markup=keyBoard.greetKB)

@dp.message_handler(lambda message: message.text == "Помощь")
async def send_help_titles(message:types.Message):
    await message.answer(texts.help_text)


@dp.message_handler(commands=['help'])
async def send_help_titles(message:types.Message):
    await message.answer(texts.help_text)


#(1, 'Кафедра программных систем')
@dp.message_handler(lambda message: message.text == "Я студент")
async def I_student(message: types.Message):
    cathedras = ds.get_cathedras()
    await message.answer("Выбери кафедру")
    mes = ' '
    for cathedra in cathedras:
        mes += str(cathedra[0]) +'. '+ str(cathedra[1]) + '\n'
    await message.answer(mes)

@dp.message_handler(lambda message: re.match(r'Кафедра ',message.text))
async def TK(message: types.Message):
    themes = ds.get_themes(message.text)
    mes = ' '
    for theme in themes:
        mes += str(theme[1]) +'. '+ str(theme[0]) + '\n'
    print(mes)
    await message.answer(mes)

#work_name,work_id,teachers.id
def get_info(work_id):
    for theme in themes:
        if theme[1] == work_id:
            return theme[2]

#(1, 'Куприянов Александр Викторович', 2, '1 корпус, 401 к. или 335 к.', 'sau.yap@gmail.com')
@dp.message_handler(lambda message:  message.text.isdigit())
async def getContact(message: types.Message):
    print('Темы после',themes)
    teacher_id = get_info(int(message.text))
    teacher = ds.get_teacher(teacher_id)
    print(teacher)
    print(teacher_id)
    print(message.text)
    mes = ''' Преподаватель: {0}\n Адрес: {1}\n Контакты: {2}'''.format(teacher[1],teacher[3],teacher[4])
    await message.answer(mes)


@dp.message_handler(lambda message: message.text == "Я преподаватель")
async def I_teacher(message: types.Message):
    if not (message.from_user.id in ds.get_teachers_ids()):#проверка ИД преподавателя
        await message.answer("Добро пожаловать", reply_markup=keyBoard.greetTeacher)
        teacher_themes = ds.get_teacher_themes(message.from_user.id)
        mes = ' '
        for teacher_theme in teacher_themes:
            mes += ' ' + str(teacher_theme[0]) +'. '+ str(teacher_theme[1]) + '\n'
        print(mes)
        await message.answer(mes)
    else:
        await message.answer("Введите пароль")
        paswordCheckActivate = True


@dp.message_handler(lambda message: message.text == "Добавить")
async def Add_ThemeStart(message: types.Message):
    if not (message.from_user.id in ds.get_teachers_ids()):#проверка ИД преподавателя
        await message.answer("введите название в формате [Создать [Тема]]")
        addTheme = True
    else:
        await message.answer("Авторизация не пройдена!", reply_markup=keyBoard.greetKB)

@dp.message_handler(lambda message: re.match(r'Создать ',message.text))
async def addThemeF(message: types.Message):
    if not (message.from_user.id in ds.get_teachers_ids()):#проверка ИД преподавателя
    
        teacher_themes = ds.get_teacher_themes(message.from_user.id)
        b=message.text
        b[8:]#обрезание строки до темы + пробел
        await message.answer("Добавление произведено")
        di.insert_scienceWork(message.user_from.id + teacher_themes.count(),b[8:],message.user_from.id)
    else:
        await message.answer("Авторизация не пройдена!", reply_markup=keyBoard.greetKB)

delTheme = False


@dp.message_handler(lambda message: message.text == "Удалить")
async def delThemeF(message: types.Message):
    await message.answer("Выберете номер и введите в формате [Убрать [номер]]")
    
@dp.message_handler(lambda message: re.match(r'Убрать ',message.text))
async def DelTheme(message: types.Message):
    if not (message.from_user.id in ds.get_teachers_ids()):#проверка ИД преподавателя
        b=message.text
        b[8:]#обрезание строки до темы + пробел
        number = int(await message.text)
        dd.del_scienceWorks(number)
        await message.answer(" Удаление произведено")
        #здесь должно быть удаление темы через бд
    else:
        await message.answer("Авторизация не пройдена!", reply_markup=keyBoard.greetKB)


@dp.message_handler(lambda: paswordCheckActivate==True)
async def CheckPassword(message: types.Message):
    if(message.Text==config.Password):
        await message.answer("Пароль верен. Введите свои данные в следющем порядке:\n Фамилия, Имя, Отчество. Ваш электронный адрес и где вас можно обычно найти.")
        registration = True
    else:
        await message.answer("Пароль не верен")
        paswordCheckActivate = False
        await message.answer("Кто вы?",reply_markup=keyBoard.greetKB)
        
@dp.message_handler(lambda: registration==True)
async def Registration(message: types.Message):
    date = await message.text
    registration=False


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)











