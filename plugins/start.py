from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert ,find_one
from pyrogram.file_id import FileId
CHANNEL = os.environ.get("CAHNNEL", "")

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
	๐๐ฎ๐ต๐ต๐ธ ๐ธ {message.from_user.first_name }
	__๐ธ๐๐ ๐ฐ ๐ต๐๐๐ ๐๐๐๐๐๐๐ ๐ฑ๐๐, ๐ฟ๐๐๐๐๐ ๐๐๐๐ ๐ฐ๐๐ข ๐๐๐๐๐๐๐๐ 
	**๐ฌ แดแดแดแดแดแดษดแด แดส แด ษชแดแดแด ๐ฅ** ๐ฐ๐๐ ๐ด๐๐๐๐ ๐ฝ๐๐  ๐ต๐๐๐๐ฝ๐๐๐ ๐๐ ๐๐๐๐๐๐ ๐ธ๐__
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton("๐๐๐ฟ๐ผ๐๐๐ ๐พ๐๐ผ๐๐๐๐ ๐ฎ๐ณ" ,url="https://t.me/XRoid_BotZ") ], 
	[InlineKeyboardButton("๐๐๐ฝ๐๐พ๐๐๐ฝ๐ ๐๐ ๐พ๐๐ผ๐๐๐๐ ๐ง", url="https://bit.ly/3EFfkJN") ]  ]))



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       update_channel = CHANNEL
       user_id = message.from_user.id
       if update_channel :
       	try:
       		await client.get_chat_member(update_channel, user_id)
       	except UserNotParticipant:
       		await message.reply_text("**__๐จ๐ธ๐พ ๐๐ป๐ฎ ๐๐ธ๐ฝ ๐ข๐พ๐ซ๐ผ๐ฌ๐ป๐พ๐ซ๐ฎ๐ญ ๐๐ ๐๐ฑ๐ช๐ท๐ท๐ฎ๐ต ๐๐ต๐ฎ๐ช๐ผ๐ฎ ๐ข๐พ๐ซ๐ผ๐ฌ๐ป๐ฒ๐ซ๐ฎ__** ",reply_to_message_id = message.message_id, reply_markup = InlineKeyboardMarkup([ [ InlineKeyboardButton("แดแดฉแดแดแดแด๊ฑ แดสแดษดษดแดส ๐ฎ๐ณ" ,url=f"https://t.me/{update_channel}") ]   ]))
       		return
       date = message.date
       _used_date = find_one(user_id)
       used_date = _used_date["date"]      
       c_time = time.time()
       LIMIT = 240
       then = used_date+ LIMIT
       left = round(then - c_time)
       conversion = datetime.timedelta(seconds=left)
       ltime = str(conversion)
       if left > 0:
       	await app.send_chat_action(message.chat.id, "typing")
       	await message.reply_text(f"```๊ฑแดสสy แดแดแดแด แดแด ษดแดแด ๊ฐแดส แด ๐ \n ๊ฐสแดแดแด แดแดษดแดสแดส ษช๊ฑ แดแดแดษชแด แด ๊ฑแด แดฉสแดแด๊ฑแด แดกแดษชแด ๊ฐแดส {ltime}```",reply_to_message_id = message.message_id)
       else:
       	used_date = find(int(message.chat.id))
       	media = await client.get_messages(message.chat.id,message.message_id)
       	file = media.document or media.video or media.audio 
       	dcid = FileId.decode(file.file_id).dc_id
       	filename = file.file_name
       	filesize = humanize.naturalsize(file.file_size)
       	fileid = file.file_id
       	await message.reply_text(f"""__แดกสแดแด แดแด แด แดกแดษดแด แดแด แดสษช๊ฑ ๊ฐษชสแด?__\n**File Name** :- {filename}\n**File Size** :- {filesize}\n**Dc ID** :- {dcid} """,reply_to_message_id = message.message_id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("๐ ๐๐๐ฃ๐๐ข๐ ",callback_data = "rename"),InlineKeyboardButton("๐พ๐๐ฃ๐๐๐ก โ๏ธ",callback_data = "cancel")  ]]))
