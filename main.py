
import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'Yor token'
wikipedia.set_lang("en")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# 1-handler
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):

    await message.reply(" Wiki botga xush kelibsiz! ")


# 2-handler
@dp.message_handler(commands=['yordam','help'])
async def send_welcome(message: types.Message):

    await message.answer("Bu bot Wikipediadan ma'lumotlarni sizga taqdim etadi!")

# 3-handler
@dp.message_handler()
async def echo(message: types.Message):

    matn =message.text
    #if matn==int:
    #    javob="Siz raqam yubordingiz matn"
    try:
        javob = wikipedia.summary(matn)
        await message.answer(javob)
    except:
        await message.answer("Bu mavzuga doir maqola topilmadi.\nQayta urinib ko'ring!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
