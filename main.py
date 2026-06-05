# from aiogram import Bot,Dispatcher
from aiogram import F
from asyncio import run
from aiogram.filters import Command
from aiogram.types import Message,FSInputFile
from funksiyalarim import ovoz_yarat,keyboard_btn
import os

TOKEN="5813418126:AAEzkw5uxtjZFg6Hdrsu_BNe8cqLFG_ZzzE"

bot=Bot(TOKEN)
dp=Dispatcher()


@dp.message(Command("start"))
async def start(message:Message):
    await bot.send_message(chat_id="@gruh01",text="salomlar gruppadoshlar")
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}",reply_markup=keyboard_btn)



@dp.message(F.contact)
async def nomer(msg:Message):
    phone=msg.contact.phone_number
    await msg.answer(f"sizning nomeringiz {phone}")

# msg.answer("salom")
# msg.repl("salom")
# bot.send(52345324,"salom")

@dp.message(F.location)
async def nomer(msg:Message):
    lat=msg.location.latitude
    lon=msg.location.longitude
    await msg.answer(f"sizning joylashuvingiz long: {lon}, lat: {lat}")

@dp.message()
async def others(message:Message):
    text=message.text
    if text=="salom":
        await message.answer("Va alaykum salom")
    elif text=="Ikki":
        await message.answer("sen ikkini bosding")
    else:
        fayl_nomi=f"{message.from_user.username}_{message.text}.mp3"
        await ovoz_yarat(message.text,fayl_nomi)
        ovozim=FSInputFile(fayl_nomi)
        await message.answer_audio(audio=ovozim,caption=message.text)
        if os.path.exists(fayl_nomi):
            os.remove(fayl_nomi)


async def main():
    await dp.start_polling(bot)


run(main())