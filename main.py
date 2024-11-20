from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, BotCommand, \
    ReplyKeyboardRemove

from services.service import Service

# Объект бота
bot = Bot(token="7853081917:AAEjEVw_zSdNFCFGlUytJ6aUk2wcb9G5QTQ")
# Диспетчер
dp = Dispatcher(bot)

# Создаем кнопки
get_image_button = KeyboardButton("Генерация изображения")
get_sound_button = KeyboardButton("Найти звук")
home_button = KeyboardButton("Домой")

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(get_image_button, get_sound_button)
return_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(home_button)

service = Service


# Установка команд для бота
async def on_startup(dp):
    # Устанавливаем список команд
    commands = [
        BotCommand(command='/home', description='Главная информация о боте'),
        BotCommand(command='/image', description='Отправить изображение (promt)'),
        BotCommand(command='/sound', description='Отправить звук (name)'),
        BotCommand(command='/git_hub', description='Ссылка на репозиторий'),
    ]
    await bot.set_my_commands(commands)


@dp.message_handler(lambda message: message.text == 'Домой' or message.text.lower() == '/home')
async def process_start_command(message: types.Message):
    await message.answer("""
/image Отправить изображение (promt)
/sound Отправить звук (name)
/git_hub Ссылка на репозиторий
    """, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['image'])
async def send_image(message: types.Message):
    await message.answer("Генерация изображения...", reply_markup=return_keyboard)
    s = service(message.from_user.id)
    result = await s.get_image(message.text.replace("/image ", "").replace("/image", ""))
    if result is None:
        await message.answer("Попробуйте позже ещё раз", reply_markup=return_keyboard)
    else:
        with open(result, 'rb') as photo:
            await message.answer_photo(photo, caption="Вот ваше изображение!", reply_markup=return_keyboard)


@dp.message_handler(commands=['sound'])
async def send_image(message: types.Message):
    await message.answer("Поиск звука...", reply_markup=return_keyboard)
    s = service(message.from_user.id)
    result = await s.get_sound(message.text.replace("/sound ", "").replace("/sound", ""))
    if result is None:
        await message.answer("Попробуйте позже ещё раз", reply_markup=return_keyboard)
    else:
        with open(result, 'rb') as audio:
            await message.answer_audio(audio, caption="Вот ваш звук!", reply_markup=return_keyboard)


@dp.message_handler(commands=['git_hub'])
async def send_link(message: types.Message):
    await message.answer("https://github.com/kakigrat12/TelegramBot_1", reply_markup=return_keyboard)

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
