from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
rock = KeyboardButton(text='Камень')
scissors = KeyboardButton(text='Ножницы')
paper = KeyboardButton(text='Бумага')

rsp_keyboard = ReplyKeyboardMarkup(keyboard=[
    [rock, paper, scissors]
], resize_keyboard=True)