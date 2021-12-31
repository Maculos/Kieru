import os, sys
import discord
from discord.ext import commands
from discord.ext.commands import Cog, command
from discord import Embed, Color
from platform import python_version
from discord import __version__ as discord_version
import datetime
from datetime import timezone
import time
from discord.ext.commands.cog import Cog
from mcstatus import MinecraftServer
import requests

# Path corrector, very magical isn't it?
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#uptime logic
start_time=time.time()
utc=datetime.datetime.now()

class Utils(Cog):
	def __init__(self, bot):
		self.bot = bot
		bot.remove_command("help")

	@commands.command(name='help', aliases=['cmds', 'cmd'], help="Shows all commands.")
	async def cmds(self, ctx, index : int = 1):
		embed = Embed(title="Help", colour=Color.from_rgb(0, 200, 0))
		pages = []
		for cogname in self.bot.cogs:
			cog : Cog = self.bot.get_cog(cogname)
			for command in cog.get_commands():
				if len(pages) != 0 and len(pages[len(pages) - 1]) < 5:
					pages[len(pages) - 1].append(command)
				else:
					pages.append([command])
		if index <= len(pages) and index > 0:
			for command in pages[index-1]:
				embed.add_field(name=command.name, value=f"{command.help} -{command.cog_name}", inline=False)
			embed.add_field(name=f"Displaying page {index} out of {len(pages)} pages", value=f"Type {f'{ctx.prefix}`' if ctx.prefix.count('<@!') > 0 else f'`{ctx.prefix}'}cmds <page>` to display a different page.", inline=False)
			embed.set_thumbnail(url=os.environ.get("BOT_ICON"))
			await ctx.send(embed=embed)
		else:
			embed.add_field(name=f"Page {index} does not exist!", value=f"Type {f'{ctx.prefix}`' if ctx.prefix.count('<@!') > 0 else f'`{ctx.prefix}'}help <page>` to display a different page.", inline=False)
			embed.set_thumbnail(url=os.environ.get("BOT_ICON_WARNING"))
			await ctx.send(embed=embed)

	@commands.command(name='debug', help='Shows debug information.')
	async def debug(self, ctx):
		current_time=time.time()
		diff = int(round(current_time - start_time))
		embed=discord.Embed(title="Debug Info", color=int(os.getenv('COLOR_DEFAULT'), 16))
		embed.add_field(name="Ping", value=f"{round(self.bot.latency * 1000)}ms")
		embed.add_field(name="Uptime", value=str(datetime.timedelta(seconds=diff)))
		embed.add_field(name="Discord.py Version:", value=discord_version, inline=False)
		embed.add_field(name="Python Version:", value=python_version(), inline=True)
		await ctx.send(embed=embed)

	@commands.command(name='status', aliases=['services', 'online'], help="Gets the status of the services Kieru relies on")
	async def status(self, ctx):
		#if working
		#	embed=discord.Embed(title="Operational", color=int(os.getenv('COLOR_SUCCESS'), 16))
		#if partial failure
		#	embed=discord.Embed(title="Degraded Performance", color=int(os.getenv('COLOR_WARNING'), 16))
		#if full failure:
		#	embed=discord.Embed(title="Offline", color=int(os.getenv('COLOR_FAIL'), 16))
		embed=discord.Embed(title="Status", color=int(os.getenv('COLOR_SUCCESS'), 16))
		if ctx.guild.id == 801180663122100234:
			try:
				server = MinecraftServer("waitwhat.maculos.dev", 25565)
				status = server.status()
				embed.add_field(name="Minecraft", value=f"✅ Operational ({status.latency} ms)", inline=False)
			except:
				embed.add_field(name="Minecraft", value="❌ Offline", inline=False)
		r = requests.get("https://maculos.dev")
		if str(r) == '<Response [200]>':
			embed.add_field(name="Maculos.dev", value="✅ Operational", inline=False)
		else:
			embed.add_field(name="Maculos.dev", value=f"❌ Offline ({r})", inline=False)
		await ctx.send(embed=embed)

	@commands.command(name='invite', help="Invite {bot.user.name} to your server.")
	async def invite(self, ctx):
		embed = Embed(title=f"Invite {self.bot.user.name}", color=int(os.getenv('COLOR_DEFAULT'), 16), url=os.getenv('INVITE_URL'))
		await ctx.send(embed=embed)

	@commands.command(name='github', help="Gets a link to github page")
	async def github(self, ctx):
		embed = Embed(title=f"Github", color=int(os.getenv('COLOR_DEFAULT'), 16), url=os.getenv('GITHUB_URL'))
		await ctx.send(embed=embed)

	#ya gotta greet them in the best way you know. y'a know? y'a know.
	@Cog.listener()
	async def on_member_join(self, member):
		guild = member.guild.id
		try:
			await member.send("https://penelopescott.bandcamp.com/album/hazards")
		except:
			pass
		try:
			sys_ch=self.bot.get_channel(guild.system_channel.id)
			await sys_ch.send(f"Welcome {member.mention} to {guild.name}!")
		except:
			pass
	@Cog.listener() #sends a ad to the sys channel if they have one
	async def on_guild_join(self, guild):
		embed = Embed(title=f"Hiya! Thanks for adding me to {guild.name}!", color=int(os.getenv('COLOR_DEFAULT'), 16))
		embed.add_field(name=f"Manage everything about {self.bot.user.name} from here", value="[Dashboard](https://timesoup.gg/dash)", inline=True)
		embed.add_field(name="Commands", value="Use 'k!help' or view the full list [here](https://timesoup.gg/commands)", inline=True)
		embed.add_field(name="d", value="3", inline=True)
		embed.add_field(name="d", value="4", inline=True)
		embed.add_field(name="d", value="5", inline=True)
		#embed.add_field(name=f"Make {self.bot.user.name} even better with premium!", value="[Start a free trial](https://timesoup.gg/premium)", inline=True)
		if guild.system_channel:
			sys_ch=self.bot.get_channel(guild.system_channel.id)
			await sys_ch.send(embed=embed)
		else:
			pass 
	#a great source of torment
	@commands.command()
	async def echo(self, ctx, *args):
		if ctx.message.author.id == 332287078832537601:
			await ctx.send(" ".join(args[0:len(args)]))
			await ctx.message.delete()
	@commands.command()
	async def customdm(self, ctx, member: discord.Member, *args):
		if ctx.message.author.id == 332287078832537601 or ctx.message.author.id == 597205813055979522:
				msg = (" ".join(args[0:len(args)]))
				await member.send(msg)
		else:
			await ctx.send("No. nya~")

def setup(bot):
	bot.add_cog(Utils(bot))
if __name__ == "__main__":
	# Running, running, running, running, oh no it broke!
	import main
	main.main()