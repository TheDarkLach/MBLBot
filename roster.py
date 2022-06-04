import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import commands
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


test = client.open("MBLS").sheet1

def getData(msg):
    global data, data2
    if msg == "wolves":
        data = test.get('A3:B24')
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
    
    
    stdout_backup = sys.stdout
    sys.stdout = string_buffer = StringIO()
    my_function()  # <-- call the function, sys.stdout is redirected now

    sys.stdout = stdout_backup  # restore old sys.stdout

    #have to get the data from a print because i cant do data = *iterable for some dumbass reason
    string_buffer.seek(0)
    data = string_buffer.read()

    data = data.split(",")

    #replace every second comma with a \n
    data2 = "\n".join(["".join(data[i:i+2]) for i in range(0,len(data),2)])




def my_function():
    print(*itertools.chain.from_iterable(data),sep=',')




class roster(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(help = "Check team rosters")
    async def roster(self,ctx,msg=None):
        getData(msg)
        await ctx.send(msg.capitalize() + "'s roster:" + "\n" + data2)
    
    @commands.command(help="add member to roster (this ones hard)")
    async def rosteradd(self,ctx):
        await ctx.send("hey lol")



def setup(bot):
  bot.add_cog(roster(bot))