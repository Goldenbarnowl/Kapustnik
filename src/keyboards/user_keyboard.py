from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def i_go_maker():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.row(InlineKeyboardButton(text='🎭 Я буду!', callback_data='i_go'))
    return keyboard_builder.as_markup(resize_keyboard=True)