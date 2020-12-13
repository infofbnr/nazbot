import discord
import json
import random
import os
import subprocess as sp
import typing
import aiohttp
from datetime import datetime
from PIL import Image
from PIL import ImageFont
import psutil
from PIL import ImageDraw
from io import BytesIO
from aiohttp import request
import asyncio
from discord.ext import commands
import os
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
# also
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"




intents = discord.Intents.all()
token = open("token.txt", "r").readline()
client = commands.Bot(command_prefix=".", intents=intents, case_insensitive=True,
                      status=discord.Status.online, activity=discord.Game(name='.help'))



extensions = ['cogs.HelpCommand','cogs.CommandEvents','cogs.CommandErrors','cogs.Christmas','cogs.MiscCommands','cogs.FunCommands','cogs.APICommands']

if __name__ == '__main__':
    for ext in extensions:
        client.load_extension(ext)


client.load_extension('jishaku')
client.run(token, reconnect=True)
