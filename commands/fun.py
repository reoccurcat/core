# General Imports
import discord, sys, localconfig, os, random, time
from discord.ext import commands

# Defining cog
class fun(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
# Start Command List

    # F
    @commands.command()
    async def f(self, ctx, *, message2):
        em = discord.Embed(title = f"F in the chat to: **{message2}**", color=discord.Color.orange())
        msg = await ctx.send(embed = em)
        await msg.add_reaction('🇫')
        #reaction = await self.bot.wait_for_reaction([r'\N{regional_indicator_f}'], msg)
        #await ctx.send(f"You responded with {reaction.emoji}.")

# End Cog File
def setup(bot):
    bot.add_cog(fun(bot))