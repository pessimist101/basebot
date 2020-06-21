# Basebot
This is a barebones Discord bot written in discord.py

## Setup
Create a `config.json` file using the template `example.config.json`
Input all the necessary fields.

## Cogs
All cogs should be in individual directories in the `cogs` directory, like so:
```
.
├── bot.py
├── cogs
│   ├── cog1
│   │   ├── cog1.py
│   │   └── cog1.config.json
│   ├── cog2
│   │   ├── cog2.py
│   │   └── cog2.config.json
│   └── cog3
│   │   ├── cog3.py
│   │   └── cog3.config.json
└── config.json
```
This is to isolate cog components and make it easier to add/remove cogs without worrying about conflicting assets
