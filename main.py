import discord
import os
from discord.ext import commands

from keep_alive import keep_alive

bot = commands.Bot(command_prefix=";", intents=discord.Intents.all())

bot.remove_command('help')

@bot.event
async def on_ready():
  print("Hello")


initial_extensions = (
    'commands',
    'events',
)


for extension in initial_extensions:
  try:
    bot.load_extension(extension)
  except Exception as e:
    print(f'Failed to load extension {extension}.')


keep_alive()
token = os.environ.get("DISCORD_KEY")
bot.run(token)