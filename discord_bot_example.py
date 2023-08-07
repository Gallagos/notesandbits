import os
import discord
from discord import client
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)
#client = discord.Client(command_prefix="/", intents=intents)
#intents = discord.Intents.default()
#intents.members = True
intents = discord.Intents(messages=True, guilds=False)

client = discord.Client(command_prefix='-', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
