from discord.ext import commands
import discord


class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            text = "Sorry {}, you do not have permissions to do that.".format(
                ctx.message.author.mention)
            await ctx.channel.send(text)
        if isinstance(error, commands.CommandNotFound):
            await ctx.channel.send("That is not a real command.")

    @commands.Cog.listener()
    async def on_message(self, message):  
        if self.bot.user.mentioned_in(message) and self.bot.user != message.author:
            await message.reply("Prefix is: `;`")

def setup(bot):
    bot.add_cog(events(bot))