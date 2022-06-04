import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import datetime


class embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(help = "test embed")
    @has_permissions(kick_members=True)
    async def testembed(self, ctx):
        time = datetime.datetime.utcnow()
        embed = discord.Embed(title="Test Embed", color=0x0a278b, timestamp=time)
        embed.add_field(name="Hello", value="0")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/868576031626383420/982148487883943956/mbltransparent.png")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(embed(bot))