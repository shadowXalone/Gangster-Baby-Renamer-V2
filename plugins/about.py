import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"✇ Oᴜʀ Nᴇᴛᴡᴏʀᴋ ✇', url=f'http://t.me/Team_XDs'>Xᴛʀᴀ Dᴇᴄᴇɴᴛꜱ</a>\n〄 Dᴇᴠ/Cʀᴇᴀᴛᴏʀ', url=f't.me/Shadow_XD_ChatBot'>ꕶʜᴀᴅᴏꪝ</a>\nLanguage :- Python3\nLibrary :- Pyrogram 2.0\nServer :- Rnder\nTotal Renamed File :- {total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} \n\n <a>Bᴏᴛꜱ Uᴘᴅᴀᴛᴇꜱ', url=f'https://t.me/Arsenal_Bots_Updates</a>\n\n❤️ With Love <a href='https://t.me/Arsenal_Bots_Updates'>**Aʀꜱᴇɴᴀʟ Bᴏᴛᴢ**</a> ❤️",quote=True)
