import discord
from discord.ext import commands


class bot_functions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="show_help")
    async def show_help(self, msg):
        embed = discord.Embed(title="ბოტის ბრძანებები",
                            description="ბოტს შეუძლია:")

        embed.add_field(
            name="<დაპოსტე",
            value="დისქორდ Embed ის დაპოსტვა სასურველ ჩენელში, სასურველი ფორმით",
            inline=False)

        await msg.channel.send(embed=embed)

    @commands.command(name="დაპოსტე")
    async def create_post(self,
                        msg,
                        chnl_id=986693980211265607,
                        title="Don't touch me",
                        color="#10de09",
                        desc="არავინ არ გამერჭოთ ",
                        img="https://i.imgur.com/5Q7clcJ.jpg",
                        emojis="💢 🔱 ⚠️ 🪡"):

        if msg.channel.id == 986693980211265607:

            if color == "purple":
                color = discord.Color.purple()
            elif color == "green":
                color = discord.Color.green()
            elif color == "blue":
                color = discord.Color.blue()
            elif color == "teal":
                color = discord.Color.teal()
            elif color.startswith("#"):
                color = int(color[1:], 16)

            embed = discord.Embed(title=title, description=desc, color=color)

            embed.set_image(url=img)

            channel = self.bot.get_channel(int(chnl_id))

            msg = await channel.send(embed=embed)
            for emoji in emojis.split():
                await msg.add_reaction(emoji)

        else:
            await msg.channel.send(
                "თქვენ არ გაქვთ ამ ჩენელში ბრძანების გამოყენების უფლება",
                delete_after=5)

