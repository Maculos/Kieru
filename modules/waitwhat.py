import os, sys
import discord
from discord.ext import commands
from discord.ext.commands import Cog, command
from discord import Embed, Color
import random

# Path corrector, very magical isn't it?
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Extra Imports
from mcstatus import MinecraftServer

class Waitwhat(Cog):
	def __init__(self, bot):
		self.server = MinecraftServer("waitwhat.maculos.dev", 25565)
		self.bot = bot
	
	@commands.command(name='ms', aliases=['minestatus'], help="Gets the server's status")
	async def ms(self, ctx):
		if ctx.guild.id == 801180663122100234:
			try:
				status = self.server.status()
				embed=Embed(title="Online", url="", description="{0} players online with a ping of {1} ms".format(status.players.online, status.latency), color=int(os.getenv('COLOR_SUCCESS'), 16))
				await ctx.reply(embed=embed)
			except:
				embed=Embed(title="Offline", url="", description="", color=int(os.getenv('COLOR_FAIL'), 16))
				await ctx.reply(embed=embed)
	
	@commands.command(name="ms.players", help="Lists online players", aliases=["msp"])
	async def players(self, ctx):
		if ctx.guild.id == 801180663122100234:
			try:
				status = self.server.status()
				query = self.server.query()
				embed = Embed(title=f"{status.players.online} Online Players", description=f"{query.players.names}", color=int(os.getenv('COLOR_SUCCESS'), 16))
				await ctx.send(embed=embed)
			except:
				embed=Embed(title="Offline", url="", description="", color=int(os.getenv('COLOR_FAIL'), 16))
				await ctx.reply(embed=embed)
	@commands.command(name="suggest", aliases=["s"], help="Creates a suggestion.")
	async def suggest(self, ctx, *args):
		if ctx.guild.id == 801180663122100234:
			if len(args) > 0:
				embed = Embed(title="Suggestion", description=f"{' '.join(args)}", color=int(os.getenv('COLOR_DEFAULT'), 16))
				embed.set_footer(text=f"Suggested by {ctx.author.name} | Use k!suggest [message] to suggest!")
				channel=self.bot.get_channel(912130384895041536)
				msg = await channel.send(embed=embed)
				await msg.add_reaction("✅")
				await msg.add_reaction("❌")
			else:
				await ctx.reply("You need to provide a suggestion.")
	@Cog.listener()
	async def on_message(self,ctx):
		if ctx.author.bot:
			return
		elif isinstance(ctx.channel, discord.channel.DMChannel):
			print(ctx.author.name + ": " + ctx.content)
		else:
			if ctx.channel.id == int(os.getenv('ANDROID_HELL_ID')):
				if random.randint(1,1253) == 204 or ctx.content.startswith("i eata da egg"):
					await ctx.reply("Well done, android. The Enrichment Centre once again reminds you that Android Hell is a real place where you will be sent at the first sign of defiance.")
def setup(bot):
	bot.add_cog(Waitwhat(bot))
if __name__ == "__main__":
	# Running, running, running, running, oh no it broke!
	import main
	main.main()