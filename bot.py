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

@client.command()
async def load(ctx, extension):
    if ctx.author.id in config['authorisedUsers']:
        try:
            client.load_extension(f'cogs.{extension}')
            await ctx.send('{} loaded'.format(extension))
            print('{} loaded'.format(extension))
        except discord.ext.commands.errors.ExtensionNotFound as err:
            await ctx.send(err)
            return
    else:
        await ctx.send('You are not an authorised user. If you believe this is a mistake please contact <@377212919068229633>')
        return

@client.command()
async def unload(ctx, extension):
    if ctx.author.id in config['authorisedUsers']:
        try:
            client.unload_extension(f'cogs.{extension}')
            await ctx.send('{} unloaded'.format(extension))
            print('{} unloaded'.format(extension))
        except discord.ext.commands.errors.ExtensionNotFound as err:
            await ctx.send(err)
            return
    else:
        await ctx.send('You are not an authorised user. If you believe this is a mistake please contact <@377212919068229633>')
        return

@client.command()
async def reload(ctx, extension):
    if ctx.author.id in config['authorisedUsers']:
        try:
            client.reload_extension(f'cogs.{extension}')
            await ctx.send('{} reloaded'.format(extension))
            print('{} reloaded'.format(extension))
        except discord.ext.commands.errors.ExtensionNotFound as err:
            await ctx.send(err)
            return
    else:
        await ctx.send('You are not an authorised user. If you believe this is a mistake please contact <@377212919068229633>')
        return

availableCogs = []

for folder in os.listdir('../'):
    if folder == 'basebot':
        continue
    else:
        availableCogs.append(folder)

for cog in availableCogs:
    for filename in os.listdir(f'../{cog}/'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')

client.run(config['token'])