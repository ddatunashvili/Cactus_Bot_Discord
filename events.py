
import discord
from discord.ext import commands


class bot_events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.author.bot:
            return
        if msg.content in ["გამარჯობა", "გაუმარჯოს", "სალამი"]:
            await msg.channel.send("გაგიმარჯოს")

        await self.bot.process_commands(msg)
    
    # @commands.Cog.listener()
    # async def on_member_join(self,member):
    #     channel = self.bot.get_channel(1062326970932801586)

    #     embed = discord.Embed(title="welcome", description="welcome message",color=discord.Color.purple() )

    #     embed.set_image(url="https://i.imgur.com/a8V0yIL.gif")
    #     embed.set_author(name=member.name, icon_url=member.avatar.url)

    #     await channel.send(embed=embed)
        