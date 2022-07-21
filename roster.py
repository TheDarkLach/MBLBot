import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import commands
import discord
import itertools
import sys
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
        data = test.get('A27:B49')
    elif msg == "boom":
        data = test.get('A52:B73')
    elif msg == "embers":
        data = test.get('A76:B97')
    elif msg == "villagers":
        data = test.get('A100:B121')
    elif msg == "voodoo":
        data = test.get('A124:B145')
    elif msg == "parrots":
        data = test.get('A148:B169')
    elif msg == "surf":
        data = test.get('A172:B193')
    else:
        print("wtf")

def adding(x , y):
    return x + y


def getCap():
    global count
    count = 0

    for i in data:
        num = data[i][0]
        print(num)
        num2 = adding(num2,num)
    count = num2


class roster(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(help = "Check team rosters")
    async def roster(self,ctx,msg=None):
        getData(msg)
        message = ''
        #print(data[0][1])
        for i in data:
            message = message + '\n'
            for x in i:
                message = message + x + ' '
        
        getCap()
        embed = discord.Embed(title=msg.capitalize() + "'s roster: ", description=message)
        embed.set_footer(text=f'cap: {count} / 35')
        await ctx.send(embed=embed)
        
    



def setup(bot):
  bot.add_cog(roster(bot))