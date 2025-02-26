import discord
import asyncio
import datetime
import os
import pytz

from dotenv import load_dotenv

load_dotenv(".env") 

TOKEN = os.getenv("KAMAR_BOT_TOKEN")
CHANNEL_ID = 1306015879141785682 

poland_tz = pytz.timezone("Europe/Warsaw")

class MyBot(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")
        
        channel = self.get_channel(CHANNEL_ID)
        now = datetime.datetime.now(poland_tz)
        formatted_date = now.strftime("%d.%m.%Y")

        if channel:
            message = await channel.send(
                f"<@&1051182697231425568> {formatted_date} react if you want to save a spot. After (20:40 game time), I recruit randoms if you don't react."
            )
            #await message.add_reaction("👍") 
            await self.close() 

bot = MyBot(intents=discord.Intents.default())
bot.run(TOKEN)
