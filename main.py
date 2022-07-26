import discord
from discord.ext import commands
from pretty_help import DefaultMenu, PrettyHelp


bot = commands.Bot(command_prefix=";", intents=discord.Intents.all(),help_command=PrettyHelp())


@bot.event
async def on_ready():
  print("Hello")
  await bot.change_presence(activity=discord.Game(name="MBL"))


initial_extensions = (
    'commands',
    'events',
    'embed',
    'roster',
    'trade',
    'signing',
    'stats',
)
@bot.command()
async def r(ctx):
  message = "```diff\n"
  for extension in initial_extensions:
    try:
      bot.unload_extension(extension)
      bot.load_extension(extension)
      message = message + "+ Reloaded " + extension + ".py\n"
    except Exception as e:
      message = message + "- Failed to reload " + extension + ".py\n"
  message = message + "```"
  await ctx.send(message)

for extension in initial_extensions:
  try:
    bot.load_extension(extension)
  except Exception as e:
    print(f'Failed to load extension {extension}.')


menu = DefaultMenu('◀️', '▶️', '❌') # You can copy-paste any icons you want.
bot.help_command = PrettyHelp(navigation=menu, color=discord.Colour.blue(),no_category="Main",show_index=False) 


bot.run("")
