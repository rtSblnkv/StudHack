from typing import List
from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
import logging
import config
import sqlite3
import keyBoard
import texts
import database_select as ds


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_hello_answer(message:types.Message):
    await message.answer(texts.start_text,reply_markup=keyBoard.greetKB)
    
#(1, 'Кафедра программных систем')
@dp.message_handler(lambda message: message.text == "Я студент")
async def TK(message: types.Message):
    cathedras = ds.get_cathedras()
    await message.answer("Выбери кафедру")
    mes = ' '
    for cathedra in cathedras:
        mes += ' ' + str(cathedra[0]) +'. '+ str(cathedra[1]) + '\n'
    print(mes)
    await message.answer(mes)

paswordCheckActivate = False

Themse = list()

@dp.message_handler(lambda message: message.text == "Я преподаватель")
async def TK(message: types.Message):
    if not (message.from_user.id in ds.get_teachers_ids()):#проверка ИД преподавателя
        await message.answer("Добро пожаловать", reply_markup=keyBoard.greetTeacher)
        teacher_themes = ds.get_teacher_themes(message.from_user.id)
    else:
        await message.answer("Введите пароль")
        paswordCheckActivate = True

addTheme = False

@dp.message_handler(lambda message: message.text == "Добавить")
async def TK(message: types.Message):
<<<<<<< HEAD
#if преподаватель
    await message.answer("введите название в формате [Создать [Тема]]")
=======
    await message.answer("Введите название в формате [Добавить [Тема]]")
>>>>>>> c7d36eb17719e5980dd63e78f2dc434f9e0faa46
    addTheme = True
#else ученик
@dp.message_handler(lambda message: message.text == "Создать")
async def addThemeF(message: types.Message):
    b=message.text
    b[8:]#обрезание строки до темы + пробел
    #theam = ""
    await message.answer("Добавление произведено")
    #theam = message.text
    #addTheme = False
    #здесь должно быть добавление темы через бд


delTheme = False

@dp.message_handler(lambda message: message.text == "Удалить")
async def TK(message: types.Message):
    await message.answer("Выберете номер и введите в формате [Удалить [номер]]")
    #delTheme = True

<<<<<<< HEAD
@dp.message_handler(lambda message: message.text[:7]=="Удалить")
=======
@dp.message_handler(lambda message: message.text[:7]==" Удалить" and message.text[9:end])
>>>>>>> c7d36eb17719e5980dd63e78f2dc434f9e0faa46
async def DelTheme(message: types.Message):
    #if препод
    b=message.text
    b[8:]#обрезание строки до темы + пробел
    number = int(await message.text)
    await message.answer(" Удаление произведено")
    #await delTheme=False
    #здесь должно быть удаление темы через бд
    #else ученик

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


works = list()
works.append("абра кадабра")
works.append("ахалай махалай")
works.append("сяськи масяськи")


@dp.message_handler(lambda message: message.text == "Кафедра технической кибернетики")
async def TK(message: types.Message):
    i=0
    mes=""
    while i<len(works) :
        i+=1
        mes = mes+ str(i) + ". " + works[i-1] +'\n'
        
    await message.answer(mes)


@dp.message_handler(commands=['help'])
async def send_help_titles(message:types.Message):
    await message.answer(texts.help_text)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)

