import discord
from discord.ext import commands
 # check if BeautifulSoup4 is installed
	from bs4 import BeautifulSoup
	soupAvailable = True

	soupAvailable = False

class bulbapedia:
    """Bulbapedia cog that searches stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
async def bulba(self):
    """Search on Bulbapedia"""

    #Your code will go here
    url = "http://bulbapedia.bulbagarden.net/wiki/Special:Search?tbm=isch&q=" #build the web adress
    async with aiohttp.get(url) as response:
        soupObject = BeautifulSoup(await response.text(), "html.parser") 

def setup(bot):
	if soupAvailable:
		bot.add_cog(bulbapedia(bot))
        
        raise RuntimeError("You need to run `pip3 install beautifulsoup4`")