# Discord Spyfall Bot
General bot that creates a spyfall game, assigning roles and locations to all players who join.

# Dependencies
- discord client
- discord api library
- python 3.5
- friends

# Setup
1. clone this repository or download the master branch
2. acquire a discord token from [Here](https://discordapp.com/developers/applications/me)
3. rename `config.json.example` to `config.json`
4. edit the file to add in your privately generated bot token key
5. Invited your bot to your server and give it permission to read and send messages
6. Optionally, if you wish to add your own custom locations, you may do so as you pleased, the file is called `spyfall_locations.json`, editing the file and restart the bot, assuming there are no **syntax** error, will automatically be added.

# Usage
`<Command_Trigger>` is the trigger used to initiliaze the bot. (See `config.json` to change the trigger)
```
<Command_Trigger> Join -- join the game
<Command_Trigger> Leave -- leaves the game
<Command_Trigger> Startgame -- starts the game, and displays a list of all locations
<Command_Trigger> Players -- displays a list of people who are currently joined / playing
<Command_Trigger> Purge -- wipes everyone from the user list
```
