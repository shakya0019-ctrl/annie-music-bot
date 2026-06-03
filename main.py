import os
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH") 
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

app = Client("AnnieBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(_, msg: Message):
    await msg.reply_text("🔥 4 Ghante Ki Tapasya Safal! Bot Chalu Hai Boss 🔥\n\nOwner ID: " + str(OWNER_ID))

@app.on_message(filters.command("id"))
async def id_cmd(_, msg: Message):
    await msg.reply_text(f"Chat ID: {msg.chat.id}\nUser ID: {msg.from_user.id}")

print("Bot Started Successfully...")
app.run()
