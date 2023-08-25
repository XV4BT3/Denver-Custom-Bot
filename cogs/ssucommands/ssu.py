import discord
from discord.ext import commands
import sqlite3

conn = sqlite3.connect("denver_database.db")
cursor = conn.cursor()

class ssucommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ssu(self, ctx):
        if ctx.author.guild_permissions.administrator or any(role.name == "testie" for role in ctx.author.roles):
            channel = discord.utils.get(ctx.guild.channels, id=1039997170025234512)
            html_color = "#56A0D3"
            embed = discord.Embed(
                title="Server Start Up",
                description=f"> A server start up has started make sure to join if you reacted or get warned for not attending!  \n \n ➡ **Server Owner:** `02_xboxplayer` \n ➡ **Code:** `DENver` \n ➡ **Paste this in your browser for easier access!:** \n roblox://placeId=2534724415&launchData=%7B%22psCode%22%3A%22Denverp%22%7D \n \n **Hosted by:**  {ctx.author.mention}",
                colour=discord.Colour(int(html_color[1:], 16)),
            )
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1093371346517495858/1136474512293113937/Denver_City_PNG.png?width=655&height=655")
            embed_Sent = await channel.send(content = "@everyon", embed=embed)
            try:
                cursor.execute("UPDATE ssustatus SET message_id = ? WHERE id = ?", (embed_Sent.id, 1))
                conn.commit()
            except sqlite3.Error as e:
                print("An error occurred:", e)

            message = await ctx.reply(content=f"{ctx.author.mention}, \n You've succesfully started a ssu.")
            await message.delete(delay=5)
            await ctx.message.delete(delay=5)
        else:
            message = await ctx.reply(content=f"{ctx.author.mention}, \n You've succesfully started a ssu.")
            await message.delete(delay=5)
            await ctx.message.delete(delay=5)
            
async def setup(client):
    await client.add_cog(ssucommands(client))
