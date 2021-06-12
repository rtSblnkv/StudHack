from aiogram import Bot,Dispatcher,executor,types
import logging
import config
import sqlite3



commands_ ={
    'start': 'Привет,студент! Этот бот поможет тебе найти научрука!',
    'help':'Доступные команды ',
}


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_hello_answer(message:types.Message):
    await message.answer("Hi bitch!")


@dp.message_handler(commands=['help'])
async def send_help_titles(message:types.Message):
    msg = text(bold('Доступные команды'),commands_.keys(),sep=('\n'))
    await message.answer(msg)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)