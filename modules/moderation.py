#barebones imports
import os, sys
from discord.ext import commands
from discord import Embed, Color

# Set the path to the root of the project
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Moderation(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# Listeners (when something occurs, like sending a message)
	#@commands.Cog.listener()
	#async def on_message(self, message):
	#	await message.channel.send("You sent a message!")

	# Commands
	@commands.command(name="template", help="if you can see this, something went wrong.")
	async def template(self, ctx):
		embed = Embed(title="This is a title.", description="Here's a description.", color=Color.from_rgb(0, 0, 0))
		embed.add_field(name="This be a corn feild.", value="This is a value.")
		embed.set_thumbnail(url=os.environ.get("BOT_ICON"))
		
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Moderation(bot))
if __name__ == "__main__":
	# Run the bot
	import main
	main.main()