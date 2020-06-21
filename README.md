# Basebot
This is a barebones Discord bot written in discord.py

## Setup
Create a `config.json` file using the template `example.config.json`
Input all the necessary fields. You'll need to acquire a bot token from the Discord Developers portal.
Create a virtual environment and install the packages required for this bot within the virtual environment. I use the venv module in python.
```python3 -m venv ./env
source ./env/bin/activate
python3 -m pip install -r requirements.txt```

## Cogs
All cogs should be in the `cogs` directory, like so:
```
.
├── bot.py
├── cogs
│   ├── cog1.py
│   ├── cog1.config.json
│   ├── cog2.py
│   ├── cog2.config.json
│   ├── cog3.py
│   └── cog3.config.json
└── config.json
```

## Running the bot
Run the bot with `python3 bot.py`
