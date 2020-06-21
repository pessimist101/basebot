import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import json

with open('config.json', 'r') as f:
    config = json.load(f)

client = commands.Bot(command_prefix = config['prefix'])

@client.event
async def on_ready():
    print('I\'m ready!')
    await client.get_channel(config['logChannel']).send('I\'m ready!')
    await client.change_presence(activity=discord.Game(name=f'{config['prefix']} help'))

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

for filename in os.listdir('./'):
    if filename == 'bot.py':
        continue
    if filename.endswith('.py'):
        client.load_extension(f'{filename[:-3]}')

client.run(config['token'])