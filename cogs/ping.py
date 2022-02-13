import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client: discord.Client) -> None:
        self.client: discord.Client = client

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        await ctx.reply("pong")


def setup(client:discord.Client):
    client.add_cog(Ping(client))
