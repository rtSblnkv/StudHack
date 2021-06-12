from aiogram import Bot,Dispatcher,executor,types
import logging

commands_ ={
    'start': 'Привет,студент! Этот бот поможет тебе найти научрука!',
    'help':'Доступные команды ',
}



TOKEN = '1760229546:AAEHaPDUy7YBkHIfMvV2_8gTzp6pOPD1QrU'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


user = dp.get_me()

print(user)

@dp.message_handler(commands=['start'])
async def send_hello_answer(message:types.Message):
    await message.answer("Hi bitch!")


@dp.message_handler(commands=['help'])
async def send_help_titles(message:types.Message):
    msg = text(bold('Доступные команды'),commands_.keys(),sep=('\n'))
    await message.answer(msg)

if __name__ = '__main__':
    executor.start_polling(dp,skip_updates=True)