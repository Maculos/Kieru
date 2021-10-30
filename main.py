#and now the 6 ratchet murderesses of crenshaw county jail in their rendition of the cell black django
import os
from os import listdir
import random
from platform import python_version
from discord import __version__ as discord_version
import discord
from discord import Embed, Activity, ActivityType, Guild
from discord.ext.commands import Bot
from mcstatus import MinecraftServer
from discord import Embed, Color

#get dem secrets
from dotenv import load_dotenv
load_dotenv()

bot = Bot(command_prefix=os.environ.get("BOT_PREFIX"), intents=discord.Intents.all())
server = MinecraftServer("192.168.254.24", 25565)

# Load cogs
for cog in os.listdir("modules"):
	if cog.endswith(".py") and not cog.startswith("__"):
		try:
			bot.load_extension(f"modules.{cog[:-3]}")
			print(f"Loaded {cog}")
		except Exception as exception:
			print(f"Failed to load {cog}")
			print(exception)
#------------------The Anti-Headache Machine------------------#
@bot.event
async def on_ready():
	current_activity = Activity(name=f"{len(bot.guilds)} server{'s' if len(bot.guilds) > 1 else ''}! | k!", type=ActivityType.watching)
	await bot.change_presence(activity=current_activity, status=discord.Status.idle)
	print("ITS ALIVEEEEEEEEEEEEEE!")
	print("(hacker noises) I'm in. (connected as " + bot.user.name + ")")
	print("")
bot.remove_command('help')
#The classic "something went wrong and I *really* dont care to fix it" machine
@bot.event
async def on_command_error(ctx, error):
			embed = discord.Embed(title="Command Error.", color=int(os.getenv('COLOR_FAIL'), 16), description= f"{str(error)}")
			embed.set_thumbnail(url = os.getenv('BOT_ICON_ERROR'))
			await ctx.reply(embed=embed)
#-----------------End of Anti-Headache Machine----------------#
bot.run(os.getenv('TOKEN'))