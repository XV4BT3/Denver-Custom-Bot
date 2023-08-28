import discord
from discord.ext import commands
import sqlite3

conn = sqlite3.connect("denver_database.db")
cursor = conn.cursor()

class endssu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def endssu(self, ctx):
        if ctx.author.guild_permissions.administrator or any(role.name == "testie" for role in ctx.author.roles):
            cursor.execute("SELECT message_id FROM ssustatus")
            message_Id = cursor.fetchone()
            channel = discord.utils.get(ctx.guild.channels, id=1039997170025234512)
            message_fetched = await channel.fetch_message(message_Id[0])
            await message_fetched.delete()
            await ctx.message.delete()
            cursor.execute("UPDATE ssustatus SET message_id = NULL WHERE id = ?", (1,))
            conn.commit()
            conn.close()

async def setup(client):
    await client.add_cog(endssu(client))