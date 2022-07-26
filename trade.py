import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('mycredentials.json',scope)
client = gspread.authorize(creds)
test = client.open("yab").sheet1


class trade(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(help = "some trade thing idk this raptor")
    @has_permissions(kick_members=True)
    async def trade(self, ctx, team1, team2):
        embed = discord.Embed(title="**Trade Alert**")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/868576031626383420/982148487883943956/mbltransparent.png")
        await ctx.send("What players and or picks are being traded from {} to {}".format(team1, team2))

        def check(msg):
            return msg.author == ctx.author and msg.channel
        
        msg = await self.bot.wait_for("message", check=check)
        if msg == msg:
            def Convert(string):
                li = list(string.split(" "))
                return li
            team1players = Convert(msg.content.lower())
            await ctx.send("What players and or picks are being traded from {} to {}".format(team2, team1))

            def check2(msg):
                return msg.author == ctx.author and msg.channel
            
            msg2 = await self.bot.wait_for("message", check=check2)
            if msg2 == msg2:
                string1 = ""
                string2 = ""
                team2players = Convert(msg2.content.lower())
                for p in team1players:
                    string1 += p.capitalize()
                    string1 +=" "
                embed.add_field(name="{} Trade:".format(team1), value=string1)

                for e in team2players:
                    string2 += e.capitalize()
                    string2 += " "
                embed.add_field(name="{} Trade:".format(team2), value=string2)
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(trade(bot))
