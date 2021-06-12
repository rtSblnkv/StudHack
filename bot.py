from typing import List
from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
import logging
import config
import keyBoard

commands_ ={
    'start': 'Привет,студент! Этот бот поможет тебе найти научрука!',
    'help':'Доступные команды ',

}



bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

cafedres= list()
cafedres.append("Кафедра технической кибернетики")
cafedres.append("кафедра физики")

@dp.message_handler(commands=['start'])
async def send_hello_answer(message:types.Message):
    await message.answer("Кто вы?\nЯ студент\nЯ преподаватель\nПомощь",reply_markup=keyBoard.greetKB)
    


@dp.message_handler(lambda message: message.text == "Я студент")
async def TK(message: types.Message):
    await message.answer("Выберите кафедру")
    i=0
    mes=""
    while i<len(cafedres) :
        i+=1
        mes = mes+ str(i) + ". " + cafedres[i-1] +'\n'
        
    await message.answer(mes)

@dp.message_handler(lambda message: message.text == "Я преподаватель")
async def TK(message: types.Message):
    await message.answer("in progress")

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
    msg = text(bold('Доступные команды'),commands_.keys(),sep=('\n'))
    await message.answer(msg)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)