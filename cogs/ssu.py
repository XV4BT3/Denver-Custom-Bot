import discord
from discord.ext import commands
from discord import app_commands

class ssupy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ssu(self, ctx):
        if ctx.author.guild_permissions.administrator or any(role.name == "testie" for role in ctx.author.roles):
            channel = discord.utils.get(ctx.guild.channels, id = 1039997170025234512)
            
            
async def setup(client):
    await client.add_cog(ssupy(client))
