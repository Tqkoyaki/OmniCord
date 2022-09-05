import discord
import dotenv
import os

# loads the .env file
dotenv.load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# prepares intents
intents = discord.Intents.default()
intents.message_content = True

# initializes the bot object
bot = discord.Client(intents=intents)

# setup code for omnicord once bot is ready
@bot.event
async def on_ready():
    print("Bot is ready")

# message handler (handles the traffic)
@bot.event
async def on_message(message):
    if message.content == "Hello" and message.author != bot.user:
        await message.channel.send("Hello World!")
        
# runs the bot
bot.run(BOT_TOKEN)