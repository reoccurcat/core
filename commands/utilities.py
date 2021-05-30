# General Imports
import discord, sys, localconfig
from discord.ext import commands

# Defining cog
class utilities(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
# Start Command List

    # F
    @commands.command()
    async def qemoji(self, ctx, emoji: discord.Emoji = None):
        if emoji == None:
            em = discord.Embed(title="Error", description="No emoji provided. Please specify an emoji.", color=discord.Color.red())
            await ctx.send(embed=em)
        else:
            em = discord.Embed(timestamp=emoji.created_at, color=discord.Color.blue())
            em.set_author(name=f":{emoji.name}:", icon_url=emoji.url)
            em.set_thumbnail(url=emoji.url)
            em.set_footer(text="Created on")
            em.add_field(name="Emoji ID", value=emoji.id)
            em.add_field(name="Usage", value=f"`{emoji}`")
            em.add_field(name="URL", value=f"<{emoji.url}>")
            await ctx.send(embed=em)


# End Cog File
def setup(bot):
    bot.add_cog(utilities(bot))