from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

butonTK=KeyboardButton('Я студент')
greetKB=ReplyKeyboardMarkup()
greetKB.add(butonTK)

butonNW = KeyboardButton('Я преподаватель')
greetCategory = ReplyKeyboardMarkup()
greetKB.add(butonNW)

butonNW = KeyboardButton('Помощь')
greetCategory = ReplyKeyboardMarkup()
greetKB.add(butonNW)

