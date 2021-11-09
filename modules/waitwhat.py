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
		if ctx.guild.id == 801180663122100234:
			try:
				status = self.server.status()
				embed=Embed(title="Online", url="", description="{0} players online with a ping of {1} ms".format(status.players.online, status.latency), color=int(os.getenv('COLOR_SUCCESS'), 16))
				await ctx.send(embed=embed)
			except:
				embed=Embed(title="Offline", url="", description="", color=int(os.getenv('COLOR_ERROR'), 16))
				await ctx.send(embed=embed)
		else:
			return
	
	@commands.command(name="ms.players", help="Gets the server's status.", aliases=["ms.p"])
	async def players(self, ctx):
		if ctx.guild.id == 801180663122100234:
			query = self.server.query()
			embed = Embed(title="Online Players", description=f"{', '.join(query.players.names)}", color=int(os.getenv('COLOR_SUCCESS'), 16))
			await ctx.send(embed=embed)
		else:
			await ctx.reply("This command is only available in the WaitWhat server.")
	@Cog.listener()
	async def on_message(self,ctx):
		if ctx.author.bot:
			return
		else:
			if ctx.author.guild_permissions.administrator: 
				if ctx.mentions:
					if ctx.mentions[0].id == 332287078832537601:
						await ctx.reply("They'll be notified, including via threats if needed.")
					else:
						return

def setup(bot):
	bot.add_cog(MineStatus(bot))

if __name__ == "__main__":
	# Running, running, running, running, oh no it broke!
	import main
	main.main()