import asyncio
from random import choice
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from config import config
from keyboards.reply import rsp_keyboard

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start_command(message: Message):
    await message.answer("Привет")

@dp.message()
async def handle_rgs_game(message: Message):
    variants = ('Камень', 'Ножницы', 'Бумага')
    user_choice = message.text
    if user_choice in variants:
        bots_choice = choice(variants)
        if (bots_choice == 'Бумага' and user_choice == 'Камень' or
            bots_choice == 'Ножницы' and user_choice == 'Бумага' or
            bots_choice == 'Камень' and user_choice == 'Ножницы'):
                await message.answer('Вы проиграли')
        elif bots_choice == user_choice:
            await message.answer('Ничья')
        else:
            await message.answer('Вы выиграли')
    else:
        await message.answer('Вы написали кринж')



async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')