import discord
from discord.ext import commands
from discord.ext.commands import has_permissions


class commands(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command(help = "check bot ping") 
  async def ping(self, ctx):
    await ctx.send(f'Bruh: {round(self.bot.latency * 1000)} ms')

"""  @commands.command()
  @has_permissions(kick_members=True)
  async def help(self, ctx):
    embed = discord.Embed(title="**__Help__**")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/868576031626383420/982148487883943956/mbltransparent.png")
    embed.add_field(name="**General commands**", value=";ping \n ;testembed \n ;roster")
    embed.set_footer(text="Created by Lach and Raptor")
    await ctx.send(embed=embed)"""

def setup(bot):
  bot.add_cog(commands(bot))