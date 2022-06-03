import discord
from discord.ext import commands


bot = commands.Bot(command_prefix=";", intents=discord.Intents.all())

bot.remove_command('help')

@bot.event
async def on_ready():
  print("Hello")
  await bot.change_presence(activity=discord.Game(name="MBL"))


initial_extensions = (
    'commands',
    'events',
    'embed',
    'sheet',
    'trade'
)

for extension in initial_extensions:
  try:
    bot.load_extension(extension)
  except Exception as e:
    print(f'Failed to load extension {extension}.')


bot.run("")
