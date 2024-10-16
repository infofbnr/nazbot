from discord.ext import commands
import discord
import random
import datetime
import asyncio


class Christmas(commands.Cog):
    """Christmas Stuff"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=["sbf"])
    async def snowballfight(self, ctx, user: discord.Member):
        """Starts a snowball fight with someone!"""

        if user == ctx.author:
            return await ctx.send("You can't fight yourself...")

        currently_fighting = True
        peoples_hp = {
            ctx.author: 100,
            user: 100
        }
        turn = 0

        while currently_fighting:
            if turn == 0:
                damage = random.randint(1, 25)
                peoples_hp[user] -= damage
                hp_now = peoples_hp[user] if peoples_hp[user] > 0 else 0
                await ctx.send(
                    f"{ctx.author.mention} throws a snowball at {user.mention} hitting them for {damage} HP\n"
                    f"{user.mention} is now at {hp_now} HP",
                    delete_after=5
                )
                turn = 1

            elif turn == 1:
                damage = random.randint(1, 25)
                peoples_hp[ctx.author] -= damage
                hp_now = peoples_hp[ctx.author] if peoples_hp[ctx.author] > 0 else 0
                await ctx.send(
                    f"{user.mention} throws a snowball at {ctx.author.mention} hitting them for {damage} HP\n"
                    f"{ctx.author.mention} is now at {hp_now} HP",
                    delete_after=5
                )
                turn = 0

            elif turn == 3:
                pass

            if peoples_hp[ctx.author] <= 0:
                currently_fighting = False
                turn = 3
                winner = user
            if peoples_hp[user] <= 0:
                currently_fighting = False
                turn = 3
                winner = ctx.author

            await asyncio.sleep(random.choice([1, 2]))

        await ctx.send(f"{winner} won with {peoples_hp[winner]} HP left!")


def setup(bot):
    bot.add_cog(Christmas(bot))
