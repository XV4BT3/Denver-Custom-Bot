import discord
from discord.ext import commands
import sqlite3

conn = sqlite3.connect('denver_database.db')
cursor = conn.cursor()

class ssupoll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ssupoll(self, ctx):
        print("Voting for a SSU.")


async def setup(client):
    await client.add_cog(ssupoll(client))