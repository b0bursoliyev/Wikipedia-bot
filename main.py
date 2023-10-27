
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

    await message.reply(" Welcome to Wiki Bot! ")


# 2-handler
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):

    await message.answer("This bot provides you with information from Wikipedia!")

# 3-handler
@dp.message_handler()
async def echo(message: types.Message):

    text = message.text
    #if matn==int:
    #    answer="You sent a number"
    try:
        answer = wikipedia.summary(text)
        await message.answer(answer)
    except:
        await message.answer("No articles were found for this topic.\nTry again!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
