import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import json
import config

client = commands.Bot(command_prefix = config.PREFIX)

@client.event
async def on_ready():
    print('I\'m ready!')
    await client.get_channel(config.LOG_CHANNEL).send('I\'m ready!')
    await client.change_presence(activity=discord.Game(name=f"{config.PREFIX}help"))

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send('{} loaded'.format(extension))
    print('{} loaded'.format(extension))

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('{} unloaded'.format(extension))
    print('{} unloaded'.format(extension))

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    client.reload_extension(f'cogs.{extension}')
    await ctx.send('{} reloaded'.format(extension))
    print('{} reloaded'.format(extension))

for directory in [i for i in os.listdir('cogs/') if os.path.isdir(f'cogs/{i}')]:
    for cog in [i[:-3] for i in os.listdir(f'cogs/{directory}/') if i.endswith('.py')]:
        client.load_extension(f'cogs.{directory}.{cog}')

client.run(config.TOKEN)