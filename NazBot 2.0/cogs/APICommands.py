import discord
from discord.ext import commands
from aiohttp import request
import aiohttp
from io import BytesIO
import typing
class API(commands.Cog):
    """API Commands."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def changemymind(self,ctx, *, text):
        async with ctx.typing():
            session = aiohttp.ClientSession()
            async with session.get(f"https://vacefron.nl/api/changemymind?text={text}") as r:
                if r.status != 200:
                    await ctx.send(f"**Unable to load image (Status = {r.status})**")
                    await session.close()
                    return
                else:
                    data = BytesIO(await r.read())
                    await ctx.send(file=discord.File(data, 'changemind.png'))
                    await session.close()

    @commands.command()
    async def pixel(self, ctx, member: typing.Optional[discord.Member]):
        member = member
        if member == None:
            member = ctx.author
        async with ctx.typing():
            headers = {
                'Authorization': 'jmLajwVfXPOyjmQK3SGkpnSn8rzFAOXFrfwEhgYz61X8hhJg9flRUVfG1dejxnYo'}

            url = f"https://api.dagpi.xyz/image/pixel/?url={member.avatar_url_as(format='jpg')}"
            async with request("GET", url, headers=headers) as r:
                if r.status != 200:
                    await ctx.send(f"**Unable to load image (Status = {r.status})**")
                    return
                else:
                    data = BytesIO(await r.read())
                    await ctx.send(file=discord.File(data, 'pixeled.png'))

    @commands.command()
    async def water(self, ctx, text: str):
        session = aiohttp.ClientSession()
        async with session.get(f"https://vacefron.nl/api/water?text={text}") as r:
            if r.status != 200:
                err = (await r.json())['message']
                await ctx.send(f"**Unable to load image (Status = {r.status}, Error = {err})**")
                await session.close()
                return
            else:
                data = BytesIO(await r.read())
                await ctx.send(file=discord.File(data, 'water.png'))
                await session.close()

    @commands.command()
    async def eject(self, ctx, name: str, color: str,  imposter: bool):
        session = aiohttp.ClientSession()
        async with session.get(f"https://vacefron.nl/api/ejected?name={name}&impostor={imposter}&crewmate={color}") as r:
            if r.status != 200:
                err = (await r.json())['message']
                await ctx.send(f"**Unable to load image (Status = {r.status}, Error = {err})**")
                await session.close()
                return
            else:
                data = BytesIO(await r.read())
                await ctx.send(file=discord.File(data, 'ejected.png'))
                await session.close()

    @commands.command()
    async def emergencymeeting(self, ctx, *, text: str):
        session = aiohttp.ClientSession()
        async with session.get(f"https://vacefron.nl/api/emergencymeeting?text={text}") as r:
            if r.status != 200:
                err = (await r.json())['message']
                await ctx.send(f"**Unable to load image (Status = {r.status}, Error = {err})**")
                await session.close()
                return
            else:
                data = BytesIO(await r.read())
                await ctx.send(file=discord.File(data, 'em.png'))
                await session.close()

def setup(bot):
    bot.add_cog(API(bot))