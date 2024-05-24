from config import TELEGRAM_TOKEN
from aiogram import Dispatcher, Bot, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)




keyboard1 = InlineKeyboardMarkup(row_width=1)
button1 = InlineKeyboardButton('покажись за тм', callback_data='click_1')
button22 = InlineKeyboardButton('Покажи героя рядом с которым неприятно', callback_data='click_2')
button69 = InlineKeyboardButton('Перейти на 2 клавиатуре', callback_data='click_3')
keyboard1.add(button1, button22, button69)

keyboard2 = InlineKeyboardMarkup(row_width=1)
button59 = InlineKeyboardButton('Покажись за св', callback_data='click_4')
button33 = InlineKeyboardButton('Покажи героя с которым приятно находиться рядом', callback_data='click_5')
button2 = InlineKeyboardButton('Переключиться на клаву 1', callback_data='click_6')
keyboard2.add(button59, button33, button2)


async def set_commands(bot: Bot):
     commands = [
         types.BotCommand(command= '/start', description='Команда для начала'),
         types.BotCommand(command='/help', description='Помощь'),
         types.BotCommand(command='/tp', description='как нажать тп'),
         types.BotCommand(command='/w', description='тут на мышке ходят')
     ]
     await bot.set_my_commands(commands)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Ты на 1 клавиатуре, нажми кнопку, чтобы перейти на 2', reply_markup=keyboard1)

@dp.callback_query_handler(lambda c: c.data == 'click_4')
async def click_4(callback_query: types.callback_query):
    await bot.send_photo(callback_query.from_user.id, photo='https://static.wikia.nocookie.net/dota2_gamepedia/images/2/2b/Tormentor_Pit_Radiant.png/revision/latest?cb=20230515214417', caption= 'так я выгляжу за силы света')

@dp.callback_query_handler(lambda c: c.data == 'click_2')
async def click_1(callback_query: types.callback_query):
     await bot.send_photo(callback_query.from_user.id, photo='https://static.wikia.nocookie.net/dota2_gamepedia/images/2/27/Meepo_Lore.png/revision/latest?cb=20210727215337', caption= 'этот герой неприятен тем что урон от меня наносится раздельно каждому мипарю')

@dp.callback_query_handler(lambda c: c.data == 'click_3')
async def go_to_2(callback_query: types.callback_query):
    await callback_query.message.edit_text('Ты перешел на 2 клавиатуру, нажми на кнопку, чтобы перейти на клавиатуру 1', reply_markup=keyboard2)


# @dp.callback_query_handler(lambda message: message.text == 'перейти на след клаву')
# async def button_1_click(callback_query: types.callback_query):
#     await callback_query.message.edit_text('перейти на след клаву', reply_markup= keyboard2)

@dp.callback_query_handler(lambda c: c.data == 'click_1')
async def click_1(callback_query: types.callback_query):
    await bot.send_photo(callback_query.from_user.id,  photo='https://static.wikia.nocookie.net/dota2_gamepedia/images/3/32/Tormentor_Pit_Dire.png/revision/latest?cb=20230515214418', caption= 'а так я выгляжу за силы тьмы')

@dp.callback_query_handler(lambda c: c.data == 'click_5')
async def button_55_click(callback_query: types.callback_query):
    await bot.send_photo(callback_query.from_user.id, photo='https://dota2.ru/img/heroes/morphling/portrait.jpg', caption= 'Этого героя приятно ловить на перекачке, но если умелый игрок то тоже супер неприятно')

@dp.callback_query_handler(lambda c: c.data == 'click_6')
async def button_4_click(callback_query: types.callback_query):
    await callback_query.message.edit_text('вернуться на 1 клаву', reply_markup= keyboard1)
#
# @dp.message_handler(commands='help')
# async def help(message: types.Message):
#     await message.reply('Я могу помочь тебе с выбором героев для фарма торментора')
#
# @dp.message_handler(commands= 'tp')
# async def tp(message: types.Message):
#     await message.answer('Нажми тп аут(кнопка t на клавиатуре)')
#
# @dp.message_handler(commands= 'w')
# async def w(message: types.Message):
#     await message.answer('тут на мышке ходят')
#
# @dp.message_handler()
# async  def echo(message: types.Message):
#     await message.answer(message.text)

async def on_commands(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_commands)