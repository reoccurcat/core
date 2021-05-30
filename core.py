# CoreBot by reoccurcat
# Licensed with the Apache License

# Imports
import discord
from discord.ext import commands
import asyncio
# Config Import
import localconfig

# Intents
intents = discord.Intents.default()
intents.members = True

# Bot Setup
description = ''
bot = commands.Bot(command_prefix=localconfig.prefix, description=description, intents=intents)
# Remove Built-In Help Command
bot.remove_command('help')

# Defining the bot status loop
async def initialStatusLoop():
    while True:
        # Template for automatically looping the bot status
        await bot.change_presence(activity=discord.Game("Made by reoccurcat"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game("Visual Studio Code"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game("Atom Editor"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game("Fixing Bugs..."))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game("Publishing Releases..."))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Game(f"v0.1 Alpha | {localconfig.prefix}help"))
        await asyncio.sleep(10)

# On_Ready Message
@bot.event
async def on_ready():
    print('\n')
    print(f"Bot logged in!\nLogged in as {bot.user.name}.\nThe bot's user ID is {bot.user.id}.")
    print('\n')
    # Bot Status Loop Initiator
    await initialStatusLoop()

# Loading Command Groups
bot.load_extension("commands.general")
bot.load_extension("commands.fun")
bot.load_extension("commands.utilities")

# Starting Bot
bot.run(localconfig.token)