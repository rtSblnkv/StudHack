from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

butonTK=KeyboardButton("Кафедра технической кибернетики")

greetKB=ReplyKeyboardMarkup()
greetKB.add(butonTK)

butonNW = KeyboardButton("Нейронные сети")

greetCategory = ReplyKeyboardMarkup()
greetKB.add(butonNW)