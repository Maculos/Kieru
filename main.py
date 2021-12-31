#and now the 6 ratchet murderesses of crenshaw county jail in their rendition of the cell black django
import os
from os import listdir
import random
from platform import python_version
from discord import __version__ as discord_version
import discord
from discord import Activity, ActivityType
from discord.ext.commands import Bot
import logging
import asyncio

#get dem secrets
from dotenv import load_dotenv
load_dotenv()
logging.basicConfig(level=logging.WARNING)
bot = Bot(command_prefix=os.environ.get("BOT_PREFIX"), intents=discord.Intents.all())
# Load cogs
for cog in os.listdir("modules"):
	if cog.endswith(".py") and not cog.startswith("__"):
		try:
			bot.load_extension(f"modules.{cog[:-3]}")
			print(f"Loaded {cog[0:-3]}")
		except Exception as exception:
			print(f"Failed to load {cog[0:-3]}")
			print(exception)
#------------------The Anti-Headache Machine------------------#
#a status machine that does major magic (it is 3am)
async def status():
	await bot.wait_until_ready()
	statuses = [
		discord.Game(name='Global Thermonuclear War'),
		discord.Activity(name=f"{len(bot.guilds)} server{'s' if len(bot.guilds) > 1 else ''}! | k!", type=discord.ActivityType.watching),
		discord.Game(name="with the fate of the universe")
	]
	while not bot.is_closed():
		await bot.change_presence(activity=random.choice(statuses), status=discord.Status.idle)
		await asyncio.sleep(15)
bot.loop.create_task(status())

@bot.event
async def on_ready():
	print("(hacker noises) I'm in. (connected as " + bot.user.name + ") \n")

#The classic "something went wrong and I *really* dont care to fix it" machine
@bot.event
async def on_command_error(ctx, error):
			embed = discord.Embed(title="Command Error.", color=int(os.getenv('COLOR_FAIL'), 16), description= f"{str(error)}")
			embed.set_thumbnail(url = os.getenv('BOT_ICON_ERROR'))
			await ctx.reply(embed=embed)
#-----------------End of Anti-Headache Machine----------------#
bot.run(os.getenv('TOKEN'))