import discord
from discord.ext import commands

class jamcog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def jamfartos(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("(╯°□°）╯︵ ┻━┻  JAMFARTOS IS ON A JAMPAGE!!!  ┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻")

def setup(bot):
    bot.add_cog(jamcog(bot))
