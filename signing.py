from io import BytesIO
import shutil
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import commands
import discord
import json
import requests

global data,data2

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('mycredentials.json',scope)

client = gspread.authorize(creds)

test = client.open("yab").sheet1

next_row = next_available_row(test)

def getData(msg):
    global data
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

class signing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userid(self,ctx,user):
        await ctx.send(user)
        print(str(user.content.lower()))

    @commands.command(help=";sign Raptor Boom 2")
    async def sign(self, ctx, player, team, rating):
        
        embed = discord.Embed(title="**New Signing**")

        url = "https://api.mojang.com/users/profiles/minecraft/" + player[1:]
        response = requests.get(url)
        result = json.loads(response.text)
        uuid = result['id']

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
        }
        uuid = uuid.strip()
        url = "https://crafatar.com/renders/head/" + uuid + "?size=512&default=MHF_Steve&overlay=true.png"

        response = requests.get(url,headers=headers,stream=True)
        response.raw.decode_content = True
        if response.status_code == 200:
            with open("mc.png", 'wb') as f:
                shutil.copyfileobj(BytesIO(response.content), f)
        else:
            await ctx.send("Who?")
            print('Image Couldn\'t be retrieved')
        with open('mc.png', "rb") as fh:
            f = discord.File(fh, filename='mc.png')

        embed.set_thumbnail(url=url)
        
        global stars
        
        if rating == "1":
            stars = "⭐"
        elif rating == "2":
            stars = "⭐⭐"
        elif rating == "3":
            stars = "⭐⭐⭐"
        elif rating == "4":
            stars = "⭐⭐⭐⭐"
        elif rating == "5":
            stars = "⭐⭐⭐⭐⭐"
        
        embed.add_field(name="**{} Sign:**".format(team.capitalize()), value="{} {}".format(player, stars))

        await ctx.send('@' + player)
        await ctx.send(embed=embed)
        

            

def setup(bot):
  bot.add_cog(signing(bot))