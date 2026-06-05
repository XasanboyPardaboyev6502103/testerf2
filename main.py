import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

from pyrogram import Client, filters




API_ID = 33243686
API_HASH = "0b4532fb6f2ac9dd03b0038f1a7b75e3"

KATTA = "@gruh01"
KICHIK = "@yoshlikdagiEngZurEskiMultfilmla"

KALIT_SUZ=[
    "zakaz","taksi kerak","taksi"
]

app = Client("mening_sessiyam", api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.chat(KATTA))
async def forward_handler(client, message):
    txt=message.text.lower()
    for t in KALIT_SUZ:
        if txt in t:
            await message.forward(KICHIK)
            await message.delete()
            print("belgilangan xabar uchirildi!")
            
    
    print("Yuborildi")

app.run()