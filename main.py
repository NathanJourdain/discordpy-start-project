import discord
from discord.ext import commands
from discord.ext.commands.errors import ExtensionNotLoaded
from discord_slash import SlashCommand
from discord_components import DiscordComponents
import os

DEFAULT_PREFIX = "."


client = commands.Bot(command_prefix=DEFAULT_PREFIX, intents=discord.Intents.all(), case_insensitive=True)
slash = SlashCommand(client, override_type = True, sync_commands=True, sync_on_cog_reload=True)
client.remove_command("help")


# reload command
@client.command()
async def reload(ctx):
        for filename in os.listdir("./cogs"):
            if filename.endswith('.py'):
                try:
                    client.reload_extension(f"cogs.{filename[:-3]}")
                except ExtensionNotLoaded as e:
                    client.load_extension(f"cogs.{filename[:-3]}")
        await ctx.send("Reload effectué !" , delete_after = 5)

# On ready
@client.event
async def on_ready():
    print('Le bot {0.user} est en ligne !'.format(client))
    await client.change_presence(status= None)
    DiscordComponents(client)

# Load cogs
for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        try:
            client.load_extension(f"cogs.{filename[:-3]}")
        except Exception as e:
            print(e)



TOKEN = "YOUR_TOKEN"
client.run(TOKEN)