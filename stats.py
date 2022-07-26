import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import commands
import discord

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('mycredentials.json',scope)
client = gspread.authorize(creds)
test = client.open("yab").sheet1


class stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(help = "Check team rosters")
    async def stats(self,ctx,user=None):
        cell = test.find(user)

        data = test.row_values(cell.row)
        data2 = test.row_values(2)


        c = dict(zip(data2, data))
        c = str(c)
        c = c.replace("'","")
        c = c.replace(",","\n")
        c = c.replace("{","")
        c = c.replace("}","")
        embed = discord.Embed(title=user + "'s stats: ", description=c)
        print(test)
        await ctx.send(embed=embed)
        #await ctx.send(c)



def setup(bot):
  bot.add_cog(stats(bot))