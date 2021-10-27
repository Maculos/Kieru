#and now the 6 ratchet murderesses of crenshaw county jail in their rendition of the cell black django
import os
import datetime
from datetime import timezone
import time
import random
from platform import python_version
from discord import __version__ as discord_version
import discord
from discord import Embed, Activity, ActivityType, Guild
from discord.ext.commands import Bot
from discord_slash import SlashCommand, SlashContext

#get dem secrets
from dotenv import load_dotenv
load_dotenv()

bot = Bot(command_prefix=os.environ.get("BOT_PREFIX"), intents=discord.Intents.all())
slash = SlashCommand(bot)

#------------------The Anti-Headache Machine------------------#
@bot.event
async def on_ready():
	current_activity = Activity(name=f"{len(bot.guilds)} server{'s' if len(bot.guilds) > 1 else ''}! | k!", type=ActivityType.watching)
	await bot.change_presence(activity=current_activity, status=discord.Status.idle)
	print("ITS ALIVEEEEEEEEEEEEEE!")
	print("(hacker noises) I'm in. (connected as " + bot.user.name + ")")
	print("")
bot.remove_command('help')
start_time=time.time() #aaaaaaaaaaaaaaaaaaaaaaaaa why
utc=datetime.datetime.now(timezone.utc)
timestamp = utc.timestamp()
#The classic "something went wrong and I *really* dont care to fix it" machine
@bot.event
async def on_command_error(ctx, error):
			embed = discord.Embed(title="Command Error.", color=int(os.getenv('COLOR_FAIL'), 16), description= f"{str(error)}")
			embed.set_thumbnail(url = os.getenv('BOT_ICON_ERROR'))
			await ctx.reply(embed=embed)
#-----------------End of Anti-Headache Machine----------------#


@bot.command()
async def invite(ctx):
	embed = Embed(title=f"Invite {bot.user.name}", color=int(os.getenv('COLOR_DEFAULT'), 16), url=os.getenv('INVITE_URL'))
	embed.set_thumbnail(url=os.getenv('BOT_ICON'))
	await ctx.send(embed=embed)
#a great source of torment
@bot.command()
async def puppet(ctx, msg):
	if ctx.message.author.id == 332287078832537601:
		await ctx.send(msg)
		await ctx.message.delete()
	else:
		await ctx.send("I'm going to steal your fucking organs bitch 😄")
@bot.command()
async def debug(ctx):
	embed=discord.Embed(title="Debug Info", color=int(os.getenv('COLOR_DEFAULT'), 16))
	embed.add_field(name="Ping", value=str(round(bot.latency * 1000)) + "ms")
	embed.add_field(name="Uptime", value=timestamp-start_time)
	embed.add_field(name="Discord.py Version:", value=discord_version, inline=False)
	embed.add_field(name="Python Version:", value=python_version(), inline=True)
	await ctx.send(embed=embed)
#ya gotta greet them in the best way you know. y'a know? y'a know.
@bot.event
async def on_member_join(member):
	guild = member.guild.id
	try:
		embed = Embed(title=f"Welcome to {guild.name}! Please get roles in the roles channel, and enjoy your stay. If you break any of the rules I'll extract your organs through your throat and sell them to a bolivian technocrat.", color=int(os.getenv('COLOR_DEFAULT'), 16))
		embed.set_thumbnail(url=os.getenv('BOT_ICON'))
		await member.send(embed=embed)
	except:
		pass
	if guild.system_channel:
		await guild.system_channel.send(f"Welcome {member.mention} to {guild.name}!")
@bot.event
async def on_guild_join(guild):
	if guild.system_channel:
		await guild.system_channel.send(f"Hiya! Thanks for adding me to {guild.name}! You can unlock a better join message by buying premium starting at $5.99 a month!")
		"""
		embed = Embed(title=f"Hiya! Thanks for adding me to {guild.name}!", color=int(os.getenv('COLOR_DEFAULT'), 16))
		await guild.system_channel.send(embed=embed)
		"""
bot.run(os.getenv('TOKEN'))

