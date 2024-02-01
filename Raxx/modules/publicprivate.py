from pyrogram import Client, filters
import requests
from config import OWNER_ID
from Raxx import Raxx as bot
import config


# Replace 'YOUR_GITHUB_TOKEN' with your GitHub token
github_token = config.GIT_TOKEN

@bot.on_message(filters.command(["gitprivate", "gitpublic"]))
def change_repo_visibility(client, message):
    try:
        # Ensure that only the owner can use these commands
        if message.from_user.id != OWNER_ID:
            message.reply_text("Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ")
            return

        # Extracting GitHub repository URL from the command
        url = message.text.split(" ", 1)[1].strip()

        # Assuming the URL is in the format 'https://github.com/user/repo'
        parts = url.split("/")
        username, repo_name = parts[-2], parts[-1]

        # Replace 'YOUR_GITHUB_TOKEN' with your GitHub token
        headers = {"Authorization": f"token {github_token}"}

        # Determine whether to set the repository to private or public
        is_private = True if message.command[0] == "gitprivate" else False

        # Change repository visibility using GitHub API
        response = requests.patch(f"https://api.github.com/repos/{username}/{repo_name}", json={"private": is_private}, headers=headers)

        if response.status_code == 200:
            visibility_status = "private" if is_private else "public"
            message.reply_text(f"Repository {username}/{repo_name} set to {visibility_status}.")
        else:
            message.reply_text(f"Fᴀɪʟᴇᴅ ᴛᴏ sᴇᴛ ʀᴇᴘᴏsɪᴛᴏʀʏ ᴠɪsɪʙɪʟɪᴛʏ. Sᴛᴀᴛᴜs ᴄᴏᴅᴇ: {response.status_code}")

    except IndexError:
        message.reply_text(f"Pʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ URL ᴀғᴛᴇʀ ᴛʜᴇ /{message.command[0]} command.")
    except Exception as e:
        message.reply_text(f"An error occurred: {str(e)}")
