import discord
from discord.ext import commands
from discord import app_commands

class ssupy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ssu(self, ctx):
        if ctx.author.guild_permissions.administrator or any(role.name == "testie" for role in ctx.author.roles):
            channel = discord.utils.get(ctx.guild.channels, id=1039997170025234512)
            embed = discord.Embed(
                title="Server SSU!",
                description="> Denver city has started a ssu, for a quick entry click the link above.",
                colour=discord.Colour.green()
            )
            await channel.send(embed=embed)
            await ctx.send(content="SSU successfully started!", ephemeral=True, delete_after=5)
            await ctx.message.delete()
        else:
            await ctx.send(content="You do not have the permissions to run this command.", ephemeral=True, delete_after=5)
            await ctx.message.delete()
