import os, sys
from discord.ext import commands
from discord.ext.commands import Cog, command
from discord import Embed, Color

# Path corrector, very magical isn't it?
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Extra Imports
from mcstatus import MinecraftServer

class MineStatus(Cog):
	def __init__(self, bot):
		self.server = MinecraftServer("waitwhat.maculos.dev", 25565)
		self.bot = bot
	
	@commands.command(name='ms', aliases=['minestatus', 'status'])
	async def ms(self, ctx):
		try:
			status = self.server.status()
			embed=Embed(title="Online", url="", description="{0} players online with a ping of {1} ms".format(status.players.online, status.latency), color=int(os.getenv('COLOR_SUCCESS'), 16))
			await ctx.send(embed=embed)
		except:
			embed=Embed(title="Offline", url="", description="", color=int(os.getenv('COLOR_ERROR'), 16))
			await ctx.send(embed=embed)
	
	@commands.command(name="ms.players", help="Gets the server's status.", aliases=["ms.p"])
	async def players(self, ctx):
		try:
			query = self.server.query()
			embed = Embed(title="Online Players", description=f"{', '.join(query.players.names)}", color=int(os.getenv('COLOR_SUCCESS'), 16))
			await ctx.send(embed=embed)
		except:
			embed = Embed(title="Offline", description="", color=int(os.getenv('COLOR_FAIL'), 16))
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(MineStatus(bot))

if __name__ == "__main__":
	# Running, running, running, running, oh no it broke!
	import main
	main.main()