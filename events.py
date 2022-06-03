from discord.ext import commands
import discord


class events(commands.Cog):
  def __init__(self, bot):
      self.bot = bot
  
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
      if isinstance(error, commands.MissingPermissions):
          text = "Sorry {}, you do not have permissions to do that lol".format(
              ctx.message.author.mention)
          await ctx.channel.send(text)
      if isinstance(error, commands.CommandNotFound):
          await ctx.channel.send("not even a real command bruh")

def setup(bot):
    bot.add_cog(events(bot))