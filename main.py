
import os

import discord
from discord.ext import commands

intents = discord.Intents.all()
from keep_alive import keep_alive

bot = commands.Bot(command_prefix="<", intents=intents)

keep_alive()

# import custom modules
from functions import bot_functions
from events import bot_events


@bot.event
async def on_ready():
  # run custom modules
  await bot.add_cog(bot_functions(bot))
  await bot.add_cog(bot_events(bot))
                    
  print("Bot is ready!")





bot.run(os.environ['token'])
