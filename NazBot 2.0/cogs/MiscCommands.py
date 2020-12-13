import discord
from discord.ext import commands
import random
class Misc(commands.Cog):
    """Misc commands!"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['pong'])
    @commands.cooldown(1, 1, commands.BucketType.channel)
    async def ping(self, ctx):
        """Checks the latency of the bot(lower is better)
        Uses: `a-ping`"""
        ping = int(self.bot.latency * 1000)
        g = self.bot.get_user(639164486846251011)
        embedVar = discord.Embed(title="***PONG!***  :ping_pong:",
                                color=random.randint(0,0xffffff),
                                 timestamp=ctx.message.created_at, description="My ping is *" + str(ping) + "ms*")
        embedVar.set_footer(
            text=f"Bot made by {g}", icon_url=g.avatar_url)  # if you like to
        await ctx.send(embed=embedVar)


    @commands.command(name='8ball')
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain.',
                    'It is decidedly so.',
                    'Without a doubt.',
                    'Yes - definitely.',
                    'You may rely on it.',
                    'As I see it, yes.',
                    'Most likely.',
                    'Outlook good.',
                    'Yes.',
                    'Signs point to yes.',
                    'Reply hazy, try again.',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'Concentrate and ask again.',
                    "Don't count on it.",
                    'My reply is no.',
                    'My sources say no.',
                    'Outlook not so good.',
                    'Very doubtful.']
        embed = discord.Embed(title="8-Ball",
                            description=f'Question: {question}\nAnswer: {random.choice(responses)}',
                            colour=random.randint(0,0xffffff))
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Misc(bot))
