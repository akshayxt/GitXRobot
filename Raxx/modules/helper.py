from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Raxx import Raxx as app
from Raxx.modules.start import *



# ----------------------------------------------------------------

glink = 'https://t.me/team_x_t'

# --------------------------------------------------------------
@app.on_callback_query(filters.regex("^close_data"))
async def close_callback(_, query):
    chat_id = query.message.chat.id
    await query.message.delete()



# ------------------------------------------------------------




@app.on_message(filters.private & filters.command('help'))
def help_handler(client, message):
    help_text = """๏ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.
ᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ [sᴜᴘᴘᴏʀᴛ]{(glink)}

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ๏ : /"""
    
    buttons = [
        [
            InlineKeyboardButton("๏ɢɪᴛʜᴜʙ๏", callback_data="githelp"),
            InlineKeyboardButton("๏ᴀɪ๏", callback_data="aihelp"),
            InlineKeyboardButton("๏ʜᴇʀᴏᴋᴜ๏", callback_data="herokuhelp")
        ],
        [
            InlineKeyboardButton("๏ᴛᴏᴏʟs๏", callback_data="toolhelp"),
            InlineKeyboardButton("๏ɪɴғᴏ๏", callback_data="infohelp"),
            InlineKeyboardButton("๏ᴅᴇᴠ ᴛᴏᴏʟs๏", callback_data="devhelp")
        ],
        
        [
            InlineKeyboardButton("๏ʙᴀᴄᴋ๏", callback_data="backhelp")
        ]
    ]
  
    reply_markup = InlineKeyboardMarkup(buttons)
   
    message.reply_text(help_text, reply_markup=reply_markup)



@app.on_callback_query()
def callback_query_handler(client, query):
    if query.data == 'githelp':
        ghelp_text = (
            "๏ ɢɪᴛʜᴜʙ & ʜᴇʀᴏᴋᴜ ᴄᴏɴᴛʀᴏʟ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs ๏\n"
            "➪/start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ \n"
            "➪/help -  Dɪsᴘʟᴀʏ ᴛʜɪs ʜᴇʟᴘ ᴍᴇssᴀɢᴇ\n"
            "➪/allrepo - Lɪsᴛ ʏᴏᴜʀ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀɪᴇs ᴜsᴇ /allrepo daxxteam\n\n"
            "➪/create_repo - Cʀᴇᴀᴛᴇ ᴀ ɴᴇᴡ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ\n"
            "➪/delrepo - Dᴇʟᴇᴛᴇ ᴀ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ\n"
            "➪/add_collaborator - Aᴅᴅ ᴀ ᴄᴏʟʟᴀʙᴏʀᴀᴛᴏʀ ᴛᴏ ᴀ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ\n"
            "➪/remove_collaborator - Rᴇᴍᴏᴠᴇ ᴀ ᴄᴏʟʟᴀʙᴏʀᴀᴛᴏʀ ғʀᴏᴍ ᴀ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ "
        )

        
        buttons = [
            [
                InlineKeyboardButton("๏ʙᴀᴄᴋ๏", callback_data="_")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)

        
        query.message.edit_text(ghelp_text, reply_markup=reply_markup)
        
