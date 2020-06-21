# Basebot
This is a barebones Discord bot written in discord.py

## Setup
Create a `config.json` file using the template `example.config.json`
Input all the necessary fields. Authorised users is an array of user IDs, and log channel is a single channel ID

## Cogs
All cogs should be in individual directories on the same level as the bot directory, like so:
```
.
└── myBotFolder
    ├── basebot
    ├── cog1
    ├── cog2
    ├── cog3
```
This is to isolate cog components and make it easier to add/remove cogs without worrying about conflicting assets