import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import commands
import discord
from io import StringIO

global data2
global data

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('mycredentials.json',scope)

client = gspread.authorize(creds)


test = client.open("yab").sheet1


def getData(msg):
    global data, data2
    if msg == "wolves":
        data = test.get('B3:C16')
    elif msg == "evokers":
        data = test.get('B27:C49')
    elif msg == "boom":
        data = test.get('B52:C73')
    elif msg == "embers":
        data = test.get('B76:C97')
    elif msg == "villagers":
        data = test.get('B100:C121')
    elif msg == "voodoo":
        data = test.get('B124:C145')
    elif msg == "parrots":
        data = test.get('B148:C169')
    elif msg == "surf":
        data = test.get('B172:C193')
    else:
        print("wtf")


def getCap():
    global count
    count = 0
    num2 = 0
    for i in data:
        num = float(i[0])
        num2 = num2 + num
    count = num2


class roster(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(help = "Check team rosters")
    async def roster(self,ctx,msg=None):
        getData(msg)
        message = ''
        for i in data:
            message = message + '\n'
            for x in i:
                message = message + x + ' '

        message = message.replace('_','\_')
        
        getCap()
        embed = discord.Embed(title=msg.capitalize() + "'s roster: ", description=message)
        embed.set_footer(text=f'cap: {count} / 35')
        await ctx.send(embed=embed)
        
    



def setup(bot):
  bot.add_cog(roster(bot))