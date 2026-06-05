import edge_tts
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,WebAppInfo


keyboard_btn=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Bir",request_contact=True),KeyboardButton(text="Ikki",request_location=True)],
        [KeyboardButton(text="Tort",web_app=WebAppInfo(url="https://kun.uz/"))]
    ],
    resize_keyboard=True
)












async def ovoz_yarat(matn:str,manzil:str):
    ovoz=edge_tts.Communicate(text=matn,voice="uz-UZ-MadinaNeural")
    await ovoz.save(manzil)











def qoshish(a:int,b:int):
    print(a+b)

