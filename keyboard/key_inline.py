from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть', url='https://dota2.fandom.com/ru/wiki/%D0%A2%D0%B5%D1%80%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D1%8C')
    but_inline2 = InlineKeyboardButton('Посмотреть', url='https://dota2.fandom.com/ru/wiki/%D0%A2%D0%B5%D1%80%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D1%8C?file=Tormentor_Dire_model.png')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline