from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery

from config import bot, supabase
from src.handlers.events import error_bot
from src.keyboards.user_keyboard import i_go_maker
from src.phrases import TEXT

user_router = Router()


@user_router.message(CommandStart())
async def start(message: Message):
    try:
        chat_id = message.from_user.id
        try:
            response = supabase.table('UserData').select('*').eq('chat_id', chat_id).execute()
            if not response.data:
                supabase.table('UserData').insert(
                    {'chat_id': chat_id, 'username': '@' + message.from_user.username}).execute()
        except:
            pass
        await bot.send_photo(
            chat_id=message.from_user.id,
            photo=FSInputFile('./src/photo/start.jpg'),
            caption=TEXT,
            reply_markup=i_go_maker()
        )
    except Exception as e:
        await error_bot(def_name='start', message=message, error=str(e))


@user_router.callback_query(F.data == 'i_go')
async def i_go_func(callback: CallbackQuery):
    try:
        chat_id = callback.from_user.id
        try:
            try:
                response = supabase.table('Check').select('*').eq('chat_id', chat_id).execute()
                if not response.data:
                    supabase.table('Check').insert(
                        {'chat_id': chat_id, 'username': '@' + callback.from_user.username}).execute()
            except:
                pass
            await bot.edit_message_caption(
                chat_id=callback.from_user.id,
                message_id=callback.message.message_id,
                caption=TEXT,
                reply_markup=None
            )
            await bot.send_photo(
                chat_id=callback.from_user.id,
                photo=FSInputFile('./src/photo/i_go.jpg'),
                caption="До скорой встречи, дорогой зритель!🤍"
            )
        except:
            await bot.send_message(
                chat_id=callback.from_user.id,
                text=f'Произошла ошибка, попробуйте позже'
            )
    except Exception as e:
        await error_bot(def_name='i_go_func', message=callback.message, error=str(e))


@user_router.message(Command('spam'), F.from_user.id == 820176381)
async def spam_attack(message: Message):
    response = supabase.table('UserData').select('*').execute()
    data = response.data
    counter = 0
    for userdata in data:
        try:
            counter += 1
            await bot.send_photo(
                chat_id=userdata['chat_id'],
                photo=FSInputFile('./src/photo/start.jpg'),
                caption=TEXT,
                reply_markup=i_go_maker()
            )
        except Exception as e:
            print(counter, userdata['chat_id'], ' - Не отправлено\n', e)
        finally:
            await bot.send_message(
                chat_id=message.from_user.id,
                text=f'Отправлено {counter} пользователей'
            )
