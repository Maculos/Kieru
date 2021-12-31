#barebones imports
import os, sys
import random
import discord
from typing import cast
from discord.ext import commands
from discord import Embed, Color
from aiohttp import ClientSession

# Set the path to the root of the project
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

possums = ["https://i.pinimg.com/236x/de/30/8e/de308e86ba7cdcbd55a67925d9868e28.jpg", "https://cdn.discordapp.com/attachments/816891837481615371/913677946785513472/IMG_6109.png", "https://i.pinimg.com/736x/f1/bd/b4/f1bdb491406091be19da6fdd6ddf6984.jpg", "https://i.pinimg.com/236x/ea/03/36/ea0336248c1cbd9406e98a52b40f52ce.jpg", "https://i.pinimg.com/236x/c2/e5/8f/c2e58fa5c34a43456697e6f5766ce1c0.jpg", "https://i.pinimg.com/236x/f2/7a/6e/f27a6e056ab28da8984f8dfa26f1fe8f.jpg", "https://i.pinimg.com/236x/b5/00/50/b50050ef1b37e1234cadc8ec81d65e42.jpg", "https://i.pinimg.com/236x/b7/4c/53/b74c533e82ac1120962f7bb24447abfa.jpg", "https://i.pinimg.com/236x/8d/b5/ce/8db5ce70e793495d7faf43469baeaae6.jpg", "https://i.pinimg.com/236x/26/98/6b/26986b6e1ea62e14871c4cee96607059.jpg", "https://i.pinimg.com/236x/48/7f/cd/487fcd31f3d51b6eb665a011ff6f5a50.jpg", "https://i.pinimg.com/236x/39/d0/32/39d032c2bbbc61796582896319ca61f3.jpg", "https://i.pinimg.com/236x/b4/85/9a/b4859a4a33c6dd5fb57a1eca22ad16a5.jpg", "https://i.pinimg.com/236x/36/16/95/361695ac25d75bd599f7e29ff12c1373.jpg", "https://i.pinimg.com/236x/5c/5d/8d/5c5d8d97773543d9b4a508724f95bc70.jpg", "https://i.pinimg.com/236x/19/bc/ba/19bcba6ebcd06be9bc4a439932447801.jpg", "https://i.pinimg.com/236x/be/a4/07/bea407608e38c619cd4930b7897dbae6.jpg", "https://i.pinimg.com/236x/2b/d7/97/2bd797a63e8ad09fb4cfc984ee50197a.jpg", "https://i.pinimg.com/236x/4b/75/13/4b751379864520e3bd14cf6e48da254c.jpg", "https://i.pinimg.com/236x/22/1f/b5/221fb5f524f63ce401af17e30dc3aaba.jpg", "https://i.pinimg.com/236x/28/de/d2/28ded2f0c74fe7ec3813d707bcc6d77f.jpg", "https://i.pinimg.com/236x/84/fe/81/84fe817b3f5b2025a94d2b5bd5377d9b.jpg", "https://i.pinimg.com/236x/ad/e1/55/ade155efd6e5d5e0066186508c2c7c28.jpg", "https://i.pinimg.com/236x/a9/d6/c6/a9d6c63520759677ed78b3b84e8fd301.jpg", "https://i.pinimg.com/236x/c0/a5/9d/c0a59d2af2cb3c8eb6b9953410839f81.jpg", "https://i.pinimg.com/236x/ac/10/4d/ac104d79f3ff4f2fb6576a6cbfb477d7.jpg", "https://i.pinimg.com/236x/de/ae/ef/deaeefc31858b07438bc8e5c82bc188a.jpg", "https://i.pinimg.com/236x/74/f5/af/74f5afbec61e683687d10b3471023ef5.jpg", "https://i.pinimg.com/236x/59/1e/17/591e1791aa6b9b194c2da7db25667a54.jpg", "https://i.pinimg.com/236x/bf/2d/34/bf2d34ce7d6c17acd0011de53bd4f065.jpg", "https://i.pinimg.com/236x/9d/b0/7e/9db07ea428133ca4d1cb3211d697916b.jpg", "https://i.pinimg.com/236x/7b/3e/94/7b3e943ae5abab73e51e2150cd2d30da.jpg", "https://i.pinimg.com/236x/8f/e1/b3/8fe1b30de79a76fde9718dd24aedfdf5.jpg", "https://i.pinimg.com/236x/51/91/3f/51913f544fd3adf64b36b3f7ce25fdea.jpg", "https://i.pinimg.com/236x/14/ef/bc/14efbc3fee95de54bb6f347ef8a03edc.jpg", "https://i.pinimg.com/236x/34/77/f7/3477f7ba5b51310ab5674cd981a95c76.jpg", "https://i.pinimg.com/236x/42/d7/3c/42d73cf628f01e2eb76b53a3cb5eca03.jpg", "https://i.pinimg.com/236x/9d/ba/fe/9dbafe15c227a10c9cc31dcd35016817.jpg", "https://i.pinimg.com/236x/9f/c8/1a/9fc81aac1a3da852a2559c07f9b3ee45.jpg", "https://i.pinimg.com/236x/1e/20/63/1e206315599aad68e7838499d3855133.jpg", "https://i.pinimg.com/236x/c5/29/d6/c529d66c290d92b5414d7572414005b4.jpg", "https://i.pinimg.com/236x/c3/d0/7e/c3d07ea9f78294420b5ed060cff81188.jpg", "https://i.pinimg.com/236x/c6/79/27/c6792709fe69efc17aa6d9e795b77435.jpg", "https://i.pinimg.com/236x/81/50/6a/81506a956b4c9c95581d41d818bde1ea.jpg", "https://i.pinimg.com/236x/e5/ff/09/e5ff09a8b2759b52f19e5af8635378b2.jpg", "https://i.pinimg.com/236x/74/b5/7b/74b57b61f85f28757a5e2de4309196ad.jpg", "https://i.pinimg.com/236x/ef/40/01/ef40014a41bb4139eef8bfd3ac5c134a.jpg", "https://i.pinimg.com/236x/bb/43/25/bb4325cae7b0432bbf89051966291cd9.jpg", "https://i.pinimg.com/236x/40/18/59/401859eafc2c9ac6c06cdb177c6c3227.jpg", "https://i.pinimg.com/236x/e5/ff/09/e5ff09a8b2759b52f19e5af8635378b2.jpg", "https://i.pinimg.com/236x/2d/ba/a2/2dbaa28246f48f6b3a88cfc813339ec1.jpg", "https://i.pinimg.com/236x/88/17/e8/8817e845a22e8f9ee35fdb816036e78c.jpg", "https://i.pinimg.com/236x/8a/72/e8/8a72e8457ca53013319538ada6cf431a.jpg", "https://i.pinimg.com/236x/31/5c/75/315c757089c36c475a014e597622edd7.jpg", "https://i.pinimg.com/236x/83/3d/a7/833da7bc1c4da1d6bcf8fcc8aeaa05be.jpg", "https://i.pinimg.com/236x/7d/01/f4/7d01f42eb58133f07283340b8f0c632c.jpg", "https://i.pinimg.com/236x/12/33/09/123309c3b9eec1df701a2996109f8bf4.jpg", "https://i.pinimg.com/236x/5b/c0/b1/5bc0b154c12b08217469ede47bce94a0.jpg", "https://i.pinimg.com/236x/5b/c0/b1/5bc0b154c12b08217469ede47bce94a0.jpg", "https://i.pinimg.com/236x/1a/57/96/1a579699386d9af8bc8871c66fe97567.jpg", "https://i.pinimg.com/236x/93/74/6b/93746b6f8004abb65b7091bec719d075.jpg", "https://i.pinimg.com/236x/cb/fa/f2/cbfaf26cd8c6e3af9648d021192f140f.jpg", "https://i.pinimg.com/236x/24/b0/ab/24b0ab6e9472725390ce7d13b15006d4.jpg", "https://i.pinimg.com/236x/07/7e/34/077e34109fd9d8d549ae1d8d1b03f675.jpg", "https://i.pinimg.com/236x/48/3f/df/483fdfcdb9497646afacd7e37c3d7984.jpg", "https://cdn.discordapp.com/attachments/816891837481615371/910004215798186094/8338AD5D-8FF1-4DE1-8FFE-11090AC38926.jpg", "https://cdn.discordapp.com/attachments/816891837481615371/910004215424880661/24636BE3-3D5F-4440-9E75-23F914D10344.jpg", "https://cdn.discordapp.com/attachments/816891837481615371/910004215022247946/E64867DB-87C7-42A3-B046-17EA68DAF0CA.jpg", "https://cdn.discordapp.com/attachments/816891837481615371/910004214728654938/46066A68-7D18-4FAF-83B3-BEF996592FD1.jpg", "https://cdn.discordapp.com/attachments/816891837481615371/910004214384693258/27039385-375E-43AD-AAF7-48E7F44BEC53.jpg", "https://cdn.discordapp.com/attachments/816891837481615371/910004213751361556/98AA3403-DAE1-443D-B295-C0DD301BBFFB.jpg", "https://cdn.discordapp.com/attachments/816891837481615371/910004349684568124/94CF392B-50DE-4738-B066-CAB71666D055.jpg", "https://cdn.discordapp.com/attachments/816891837481615371/910004349927841832/72EC81A7-973F-4608-BFFA-40C0916ACD39.jpg", "https://cdn.discordapp.com/attachments/816891837481615371/910004350263365672/4D77D514-352A-420F-931A-51452BAC42D6.jpg", "https://cdn.discordapp.com/attachments/816891837481615371/910004527485296760/IMG_5924.png"]
cats = ["https://i.pinimg.com/236x/fb/3c/00/fb3c00f6691443eac6f8031433697701.jpg","https://i.pinimg.com/236x/fb/3c/00/fb3c00f6691443eac6f8031433697701.jpg"]

class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	# Commands
	@commands.command(name="possum", help="Sends a random possum image! All hail possums!")
	async def possum(self, ctx):
		await ctx.reply(possums[random.randint(0, len(possums)-1)])
	@commands.command(name="cat", help="Sends a random cat!")
	async def cat(self, ctx):
		await ctx.reply(cats[random.randint(0, len(cats)-1)])

	@commands.command(name='urban', aliases=['ud'], help='Searches the urbs for a term.')
	async def urbandictionary(self, ctx, *args):
		try:
			term = " ".join(args[0:len(args)])
			url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
			querystring = {"term":term}
			headers = {
			'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
			'x-rapidapi-key': os.getenv("URB_KEY")
			}
			async with ClientSession() as session:
				async with session.get(url, headers=headers, params=querystring) as response:
					r = await response.json()
					embed = discord.Embed(title=f"Urban dictionary result for {term}", color=int(os.getenv('COLOR_SUCCESS'), 16), description= f"Definition: {r['list'][0]['definition']}")
			await ctx.send(embed=embed)
		except:
			embed=Embed(title=f"Could not find results for {term}", url="", description="", color=int(os.getenv('COLOR_FAIL'), 16))
			await ctx.reply(embed=embed)
def setup(bot):
	bot.add_cog(Fun(bot))

if __name__ == "__main__":
	# Run the bot
	import main
	main.main()