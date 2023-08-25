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
        if ctx.author.guild_permissions.administrator or any(role.name == "testie" for role in ctx.author.roles):
            channel = discord.utils.get(ctx.guild.channels, id = 1039997170025234512)
            html_color = "#56A0D3"
            embed = discord.Embed(title="SSU Vote", 
                                description=f"> Do you want to launch an SSU? React below 3-4+ to host an SSU \n `Lets have a great roleplay session!`\n \n **Command Sent By:** {ctx.author.mention}",
                                colour=discord.Colour(int(html_color[1:], 16)))
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1093371346517495858/1136474512293113937/Denver_City_PNG.png?width=655&height=655")
            embed_Sent = channel.send(content = "@everyon", embed=embed)
            message = await ctx.reply(content=f"{ctx.author.mention}, \n You've succesfully commited a ssupoll.")
            await message.delete(delay=5)
            await ctx.message.delete(delay=5)
            cursor.execute("UPDATE ssustatus SET ssu_poll_message = ? WHERE id = ?", (embed_Sent.id, 1))
            conn.commit()

async def setup(client):
    await client.add_cog(ssupoll(client))