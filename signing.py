import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import commands
import discord
import itertools
import sys
from io import StringIO

global data,data2

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('mycredentials.json',scope)

client = gspread.authorize(creds)

test = client.open("yab").sheet1

def getData(team):
    global data

    #have to get the data from a print because i cant do data = *iterable for some dumbass reason

    if team == "wolves":
        data = test.get('A3:B24')
    elif team == "evokers":
        data = test.get('A27:B49')
    elif team == "boom":
        data = test.get('A52:B73')
    elif team == "embers":
        data = test.get('A76:B97')
    elif team == "villagers":
        data = test.get('A100:B121')
    elif team == "voodoo":
        data = test.get('A124:B145')
    elif team == "parrots":
        data = test.get('A148:B169') 
    elif team == "surf":
        data = test.get('A172:B193')

    stdout_backup = sys.stdout
    sys.stdout = string_buffer = StringIO()
    my_function()  # <-- call the function, sys.stdout is redirected now

    sys.stdout = stdout_backup  # restore old sys.stdout
    string_buffer.seek(0)
    data = string_buffer.read()

    

def getCap():
    global count
    count = 0

    for x in data:
        if x == "*":
            count+=0.5
        elif x == "⭐":
            count+=1

    


def my_function():
    global data
    print(*itertools.chain.from_iterable(data),sep=',')


class signing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = "sign a player (;sign TheDarkLach wolves 1.5)")
    async def sign(self,ctx,player,team,stars):
      getData(player,team,stars)
      print(data)
    
    @commands.command(help = "sign a player (;sign TheDarkLach wolves 1.5)")
    async def cap(self,ctx,team):
      getData(team)
      getCap()
      await ctx.send("The cap for {} is {} / 35".format(team, count))
      if count > 35:
        count2 = count - 35
        await ctx.send (":rotating_light:THE {} ARE OVER CAP BY {}!:rotating_light:".format(team.upper(),count2))

    @commands.command()
    async def raw(self,ctx,team):
        getData(team)
        await ctx.send(data)



def setup(bot):
  bot.add_cog(signing(bot))