import discord
from discord.ext import commands


class commands(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.command() 
  async def ping(self, ctx):
    await ctx.send(f'Bruh: {round(self.bot.latency * 1000)} ms')


def setup(bot):
  bot.add_cog(commands(bot))