import discord
from discord.ext import commands
import random
import json

class CommandEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if await self.bot.is_owner(before.author):
            await self.bot.process_commands(after)

    @commands.Cog.listener()
    async def on_message(self, msg):
        if not msg.author.bot:
            try:
                if msg.mentions[0] == self.bot.user:
                    with open("./prefixes.json", "r") as f:
                        prefixes = json.load(f)
                        pre = prefixes[str(msg.guild.id)]
                        embed = discord.Embed(
                                title="I been heard you pinged me?",
                                description=f"My prefix for this server is `{pre}`",
                                color=random.randint(0, 0xffffff)
                        )
                        await msg.channel.send(embed=embed)
            except:
                pass

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in')


def setup(bot):
    bot.add_cog(CommandEvents(bot))
