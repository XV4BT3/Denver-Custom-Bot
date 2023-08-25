import discord
from discord.ext import commands
import asyncio
import os

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())
token = os.environ.get('DISCORD_TOKEN')

@client.event
async def on_ready():
    print("Hello Storm, your bot is successfully logged in!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$help"))

async def load_cogs():
    for root, dirs, files in os.walk('./cogs'):
        for file in files:
            if file.endswith('.py'):
                cog_name = file[:-3]
                cog_path = os.path.relpath(os.path.join(root, cog_name), './cogs').replace(os.path.sep, '.')
                try:
                    await client.load_extension(f'cogs.{cog_path}')
                    print(f'{cog_name} is successfully loaded!')
                except Exception as e:
                    print(f'Failed to load {cog_name}: {e}')

async def main():
    async with client:
        await load_cogs()
        await client.start(token)

asyncio.run(main())
