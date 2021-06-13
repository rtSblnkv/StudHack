from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

butonNW=KeyboardButton('Я студент')
greetKB=ReplyKeyboardMarkup()
greetKB.add(butonNW)

butonNW = KeyboardButton('Я преподаватель')
greetCategory = ReplyKeyboardMarkup()
greetKB.add(butonNW)

butonNW = KeyboardButton('Помощь')
greetCategory = ReplyKeyboardMarkup()
greetKB.add(butonNW)




greetTeacher=ReplyKeyboardMarkup()
butonNW = KeyboardButton('Добавить')
greetCategory = ReplyKeyboardMarkup()
greetTeacher.add(butonNW)

butonNW = KeyboardButton('Удалить')
greetCategory = ReplyKeyboardMarkup()
greetTeacher.add(butonNW)