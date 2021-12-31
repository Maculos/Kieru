#barebones imports
import os, sys
from discord.ext import commands
from discord import Embed, Color

# Set the path to the root of the project
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Template(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# Commands
	@commands.command(name="template", help="if you can see this, something went wrong.")
	async def template(self, ctx):
		embed = Embed(title="yarr its a title.", description="Here's a description. (supposedly)", color=Color.from_rgb(0, 0, 0))
		embed.add_field(name="This be a feild.", value="This is a value. It has no value to anyone.")
		embed.set_thumbnail(url=os.environ.get("BOT_ICON"))
		
		await ctx.send(embed=embed)

	# Listeners (when something occurs, like sending a message)
	@commands.Cog.listener()
	async def on_message(self, message):
		await message.channel.send("You sent a message!")

def setup(bot):
	bot.add_cog(Template(bot))

if __name__ == "__main__":
	# Running, but not through the bot framework (for testing) and not as a module (for importing)
	# or a cog (for adding) and not as a cog (for removing) or a cog (for reloading) or a cog (for reloading)
	# and not as a cog (for reloading) for reloading or something like that (for reloading) 
	#Thanks copilot for that wild """sentence"""
	import main
	main.main()