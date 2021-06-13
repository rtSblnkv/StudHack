from typing import List
from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
import logging
import config
import sqlite3
import keyBoard
import texts
import database_select


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


cafedres= list()
cafedres.append("Кафедра технической кибернетики")
cafedres.append("кафедра физики")

@dp.message_handler(commands=['start'])
async def send_hello_answer(message:types.Message):
    await message.answer(texts.start_text,reply_markup=keyBoard.greetKB)
    


@dp.message_handler(lambda message: message.text == "Я студент")
async def TK(message: types.Message):
    await message.answer("Выбери кафедру")
    i=0
    mes=""
    while i<len(cafedres) :
        i+=1
        mes = mes+ str(i) + ". " + cafedres[i-1] +'\n'

    await message.answer(mes)

paswordCheckActivate = False

Themse = list()

@dp.message_handler(lambda message: message.text == "Я преподаватель")
async def TK(message: types.Message):
    if(True):#проверка ИД преподавателя
        await message.answer("Добро пожаловать", reply_markup=keyBoard.greetTeacher)
        #здесь нужно подгрузить из бд в Themes темы преподователя
    else:
        await message.answer("Введите пароль")
        paswordCheckActivate = True

addTheme = False

@dp.message_handler(lambda message: message.text == "Добавить")
async def TK(message: types.Message):
    await message.answer("введите название в формате [Добавить [Тема]]")
    addTheme = True

@dp.message_handler(lambda message: message.text == "Добавить"+str(b))
async def addThemeF(message: types.Message):
    #theam = ""
    await message.answer("добавление произведено")
    #theam = message.text
    #addTheme = False
    #здесь должно быть добавление темы через бд


delTheme = False

@dp.message_handler(lambda message: message.text == "Удалить")
async def TK(message: types.Message):
    await message.answer("выберете номер и введите в формате [Удалить [номер]]")
    #delTheme = True

@dp.message_handler(lambda message: message.text[:7]=="Удалить" and message.text[9:end])
async def DelTheme(message: types.Message):
    number = int(await message.text)
    await message.answer("удаление произведено")
    #await delTheme=False
    #здесь должно быть удаление темы через бд


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

