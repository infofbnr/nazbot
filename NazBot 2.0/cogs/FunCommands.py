import discord
from discord.ext import commands
import random
from datetime import datetime
from aiohttp import request
import asyncio
from io import BytesIO
import typing
from PIL import Image


class Fun(commands.Cog):
    '''Fun Commands!'''
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(aliases=['simpr8'])
    async def simprate(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        random.randint(0, 100)

        embed = discord.Embed(title="Simp rate machine",
                            description=f"{member.name} is {random.randint(0, 100)}% simp!",
                            colour=random.randint(0,0xffffff),
                            timestamp=datetime.utcnow())
        await ctx.send(embed=embed)


    @commands.command()
    async def pickupline(self, ctx):
        url = "https://api.dagpi.xyz/data/pickupline"
        headers = {
            'Authorization': 'jmLajwVfXPOyjmQK3SGkpnSn8rzFAOXFrfwEhgYz61X8hhJg9flRUVfG1dejxnYo'}
        async with request("GET", url, headers=headers) as r:
            if r.status == 200:
                data = await r.json()
                embed = discord.Embed(
                    title="Pick-up line:",
                    description=data['joke'],
                    color=random.randint(0, 0xffffff)
                )
                embed.set_footer(text="Category: " + data['category'])
                await ctx.send(embed=embed)
        
    @commands.command()
    async def yomama(self, ctx):
        url = "https://api.dagpi.xyz/data/yomama"
        headers = {
            'Authorization': 'jmLajwVfXPOyjmQK3SGkpnSn8rzFAOXFrfwEhgYz61X8hhJg9flRUVfG1dejxnYo'}
        async with request("GET", url, headers=headers) as r:
            if r.status == 200:
                data = await r.json()
                embed = discord.Embed(
                    title="Yo Mama Joke:",
                    description=data['description'],
                    color=random.randint(0, 0xffffff)
                )
                await ctx.send(embed=embed)


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def darkjoke(self, ctx):
        url = "https://sv443.net/jokeapi/v2/joke/Dark?blacklistFlags=religious,political,racist,sexist"
        async with request("GET", url, headers={}) as r:
            if r.status == 200:
                data = await r.json()
                if data['type'] == "twopart":
                    embed = discord.Embed(
                        title="Joke:",
                        description=data['setup'],
                        color=random.randint(0, 0xffffff)
                    )
                    embed.set_footer(
                        text="Reply with '?' for the rest of the joke!(You have 2 minutes)")
                    await ctx.send(embed=embed)

                    def check(m):
                        return m.content == "?" and m.author == ctx.author
                    try:
                        b = await self.bot.wait_for('message', check=check, timeout=120.0)
                    except asyncio.TimeoutError:
                        await ctx.send(f"{ctx.author.mention} did not respond in time, the rest of the joke was: " + data['delivery'])
                        return
                    if b.content == "?":
                        embed = discord.Embed(
                            title="Rest of the Joke:",
                            description=data['delivery'],
                            color=random.randint(0, 0xffffff)
                        )
                        embed.set_footer(text="Category: " + data['category'])
                        await ctx.send(embed=embed)
                        return
                elif data['type'] == "single":
                    embed = discord.Embed(
                        title="Joke:",
                        description=data['joke'],
                        color=random.randint(0, 0xffffff)
                    )
                    embed.set_footer(text="Category: " + data['category'])
                    await ctx.send(embed=embed)


    @commands.command()
    async def roast(self, ctx):
        url = "https://api.dagpi.xyz/data/roast"
        headers = {
            'Authorization': 'jmLajwVfXPOyjmQK3SGkpnSn8rzFAOXFrfwEhgYz61X8hhJg9flRUVfG1dejxnYo'}
        async with request("GET", url, headers=headers) as r:
            if r.status == 200:
                data = await r.json()
                embed = discord.Embed(
                    title="Roast:",
                    description=data['roast'],
                    color=random.randint(0, 0xffffff)
                )
                await ctx.send(embed=embed)


    @commands.command()
    async def pp(self, ctx, member: typing.Optional[discord.Member]):
        member = member
        if member == None:
            member = ctx.author

        response = ['8D',
                    '8=D',
                    '8==D',
                    '8===D',
                    '8====D',
                    '8=====D',
                    '8======D',
                    '8=======D',
                    '8=========D',
                    '8============D',
                    '8===============D',
                    '8=================D',
                    '8===================D']
        embesd = discord.Embed(title="PP size Meter",
                            description=f"{member.name}'s pp \n{random.choice(response)}",
                            colour=random.randint(0,0xffffff),
                            timestamp=datetime.utcnow())
        await ctx.send(embed=embesd)


    @commands.command(aliases=['gayr8'])
    async def gayrate(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        random.randint(0, 100)

        embsed = discord.Embed(title="Gay Meter :rainbow_flag:",
                            description=f"{member.name} is {random.randint(0, 100)}% gay!",
                            colour=random.randint(0,0xffffff),
                            timestamp=datetime.utcnow())
        await ctx.send(embed=embsed)

    @commands.command()
    async def wanted(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        wanted = Image.open("./wanted.jpg")

        asset = member.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((339, 277))
        wanted.paste(pfp, (67, 230))

        wanted.save("wanted.jpg")
        await ctx.send(file=discord.File("wanted.jpg"))
def setup(bot):
    bot.add_cog(Fun(bot))
