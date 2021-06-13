from typing import List
from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
import logging
import config
import sqlite3
import keyBoard
import texts
import database_select as ds
import database_insert as di
import database_delete as dd



bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
themes = []

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
async def TK(message: types.Message):
    cathedras = ds.get_cathedras()
    await message.answer("Выбери кафедру")
    mes = ' '
    for cathedra in cathedras:
        mes += str(cathedra[0]) +'. '+ str(cathedra[1]) + '\n'
    print(mes)
    await message.answer(mes)

paswordCheckActivate = False


@dp.message_handler(lambda message: message.text == "Я преподаватель")
async def TK(message: types.Message):
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

addTheme = False

@dp.message_handler(lambda message: message.text == "Добавить")
async def TK(message: types.Message):
    if not (message.from_user.id in ds.get_teachers_ids()):#проверка ИД преподавателя
        await message.answer("введите название в формате [Создать [Тема]]")
        addTheme = True
    else:
        await message.answer("Авторизация не пройдена!", reply_markup=keyBoard.greetKB)

@dp.message_handler(lambda message: re.match(r'Создать ',message.text))
async def addThemeF(message: types.Message):
    teacher_themes = ds.get_teacher_themes(message.from_user.id)
    b=message.text
    b[8:]#обрезание строки до темы + пробел
    #theam = ""
    await message.answer("Добавление произведено")
    di.insert_scienceWork(message.user_from.id + teacher_themes.count(),b[8:],message.user_from.id)
    

delTheme = False


@dp.message_handler(lambda message: message.text == "Удалить")
async def TK(message: types.Message):
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

registration = False

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


async def TK(message: types.Message):
    themes = ds.get_themes(message.Text)
    mes = ' '
    for theme in themes:
        mes += str(theme[1]) +'. '+ str(theme[0]) + '\n'
    print(mes)
    await message.answer(mes)


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)

#work_name,work_id,teachers.id
def get_info(theme_):
    for theme in themes:
        if theme[0] == theme_:
            return theme[2]










