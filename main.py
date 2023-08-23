import discord
from discord.ext import commands
import asyncio
import os

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Hello Storm, your bot is succesfully logged in!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$help"))

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
            print(f'{filename} is succesfully loaded!')

async def main():
    async with client:
        await load()
        await client.start("MTEzOTk5ODYxMzQ5NDMwMDcyNA.Gq2vdG.rT85Aq-RLxfcbBH8DzgGFT0KSa8mGqHkjxNU8k")

asyncio.run(main())
