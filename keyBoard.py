from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

butonNW=KeyboardButton('Я студент')
greetKB=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
greetKB.add(butonNW)

butonNW = KeyboardButton('Я преподаватель')
greetCategory = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
greetKB.add(butonNW)

butonNW = KeyboardButton('Помощь')
greetCategory = ReplyKeyboardMarkup(resize_keyboard=True)
greetKB.add(butonNW)




greetTeacher=ReplyKeyboardMarkup()
butonNW = KeyboardButton('Добавить')
greetCategory = ReplyKeyboardMarkup(resize_keyboard=True)
greetTeacher.add(butonNW)

butonNW = KeyboardButton('Удалить')
greetCategory = ReplyKeyboardMarkup(resize_keyboard=True)
greetTeacher.add(butonNW)