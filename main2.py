from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


TOKEN_API = '6862556982:AAFXfVO5x111mgjU9zv6gXdOByIbK85dzqE'
bot = Bot(token= TOKEN_API)
dp = Dispatcher(bot)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

keyboard1 = InlineKeyboardMarkup(row_width=1)
button1 = InlineKeyboardButton('')
