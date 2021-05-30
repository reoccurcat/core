# General Imports
import discord, sys, localconfig
from discord.ext import commands
# Optional Imports
import psutil, datetime, time

# Grab Start Time
startTime = time.time()

# Defining cog
class general(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
# Start Command List

    # Help
    @commands.command()
    async def help(self, ctx):
        em = discord.Embed(title="Help", color=discord.Color.blue())
        em.add_field(name="General", value="help, about")
        em.add_field(name="Fun", value="f")
        em.add_field(name="Utilities", value="qemoji")
        await ctx.send(embed=em)
    
    @commands.command()
    async def about(self, ctx):
        em = discord.Embed(title="About", description="About this instance", color=discord.Color.blue())
        em.add_field(name="Prefix", value=f"`{localconfig.prefix}`")
        em.add_field(name="Bot Owner", value=f"<@!{localconfig.ownerID}>")
        if 'psutil' in sys.modules:
            cpuUsage = psutil.cpu_percent()
            em.add_field(name="Host CPU Usage", value=f"{cpuUsage}%")
            memUsage = psutil.virtual_memory().percent
            em.add_field(name="Host Memory Usage", value=f"{memUsage}%")
        if 'datetime' and 'time' in sys.modules:
            currentTime = time.time()
            difference = int(round(currentTime - startTime))
            botUptime = str(datetime.timedelta(seconds=difference))
            em.add_field(name="Uptime", value=botUptime)
        em.add_field(name="Ping", value=f"`{round(self.bot.latency*1000)} ms`")
        servers = list(self.bot.guilds)
        serversNumber = len(servers)
        em.add_field(name="Server Numbers", value=serversNumber)
        await ctx.send(embed=em)

    


# End Cog File
def setup(bot):
    bot.add_cog(general(bot))