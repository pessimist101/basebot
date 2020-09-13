# Basebot
This is a barebones Discord bot written in discord.py

## Setup
Create a `config.py` file using the template `example.config.py` and input all the necessary fields - you'll need to acquire a bot token from the Discord Developers portal.
Create a virtual environment and install the packages required for this bot within the virtual environment. I use the venv module in python.
```
$ python3 -m venv ./env
$ source ./env/bin/activate
(env) $ python3 -m pip install -r requirements.txt
```

## Cogs
All cogs should be in directories within the `cogs` directory, like so:
```
.
├── bot.py
├── cogs
│   ├── mycog
│   │   ├── config.json
│   │   ├── mycog.py
│   │   ├── README.md
│   │   └── requirements.txt
│   └── cog2
│       ├── cog2.py
│       ├── config.json
│       ├── README.md
│       └── requirements.txt
└── config.py
```

## Running the bot
Run the bot with `./start.sh` (make sure to make this executable with `chmod +x start.sh`!)
