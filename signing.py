import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord.ext import commands
import itertools
import sys
from io import StringIO

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('mycredentials.json',scope)
client = gspread.authorize(creds)
test = client.open("MBLS").sheet1



class signing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot





def setup(bot):
  bot.add_cog(signing(bot))