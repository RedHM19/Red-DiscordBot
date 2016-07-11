import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def void(self):
        """Void stinks"""

        #Your code will go here
        await self.bot.say("YOU SUCK VOID!! BOOOOOOOOOOOOOOO!!")
   

def setup(bot):
    bot.add_cog(Mycog(bot))
