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

# Path corrector, very magical isn't it?
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#uptime logic
start_time=time.time()
utc=datetime.datetime.now()

class Utils(Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="template", help="This is a command.")
	async def template(self, ctx):
		embed = Embed(title="This is a title.", description="This is a description.", color=Color.from_rgb(0, 0, 0))
		embed.add_field(name="This is a field.", value="This is a value.")
		embed.set_thumbnail(url=os.environ.get("BOT_ICON"))
		
		await ctx.send(embed=embed)

	@commands.command(name='debug')
	async def debug(self, ctx):
		current_time=time.time()
		diff = int(round(current_time - start_time))
		embed=discord.Embed(title="Debug Info", color=int(os.getenv('COLOR_DEFAULT'), 16))
		embed.add_field(name="Ping", value=f"{round(self.bot.latency * 1000)}ms")
		embed.add_field(name="Uptime", value=str(datetime.timedelta(seconds=diff)))
		embed.add_field(name="Discord.py Version:", value=discord_version, inline=False)
		embed.add_field(name="Python Version:", value=python_version(), inline=True)
		await ctx.send(embed=embed)
	@commands.command(name='invite')
	async def invite(self, ctx):
		embed = Embed(title=f"Invite {self.bot.user.name}", color=int(os.getenv('COLOR_DEFAULT'), 16), url=os.getenv('INVITE_URL'))
		embed.set_thumbnail(url=os.getenv('BOT_ICON'))
		await ctx.send(embed=embed)
	#a great source of torment
	@commands.command()
	async def echo(ctx, msg):
		if ctx.message.author.id == 332287078832537601:
			await ctx.send(msg)
			await ctx.message.delete()
		else:
			await ctx.send("No. nya~")
	#ya gotta greet them in the best way you know. y'a know? y'a know.
	@Cog.listener()
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
	@Cog.listener()
	async def on_guild_join(guild):
		if guild.system_channel:
			await guild.system_channel.send(f"Hiya! Thanks for adding me to {guild.name}! You can unlock a better join message by buying premium starting at $5.99 a month!")
			"""
			embed = Embed(title=f"Hiya! Thanks for adding me to {guild.name}!", color=int(os.getenv('COLOR_DEFAULT'), 16))
			await guild.system_channel.send(embed=embed)
			"""

def setup(bot):
	bot.add_cog(Utils(bot))
if __name__ == "__main__":
	# Running, running, running, running, oh no it broke!
	import main
	main.main()