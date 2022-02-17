import discord
from discord.ext import commands, tasks

class Loop(commands.Cog):
    def __init__(self, client: discord.Client) -> None:
        self.client: discord.Client = client
        self.loop.start()

    @tasks.loop(seconds=10)
    async def loop(self):
        print("loop")


def setup(client:discord.Client):
    client.add_cog(Loop(client))
