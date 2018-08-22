import game
import player
import discord
import asyncio
import json
import os

if os.path.exists('config.json'):
    with open('config.json','r') as configs:
        configs = json.load(configs)

bot_token = configs['discord']['token']
bot_trigger = configs['discord']['trigger']
bot_description = "Spyfall"

game = game.Game()
bot = discord.Client()

@bot.event
async def on_ready():
    print("Bot User-Name: %s" % bot.user)
    print("Bot User-ID: %s" % bot.user.id)
    print("--------------------")

def embeded_message(role, location):
    if role == "Spy":
        title = "Spyfall - Game"
        content = "Your Role is ---> **SPY** \n The Location is ---> *NOTGIVEN*"
        return discord.Embed(title=title, description=content)
    elif role != "Spy":
        title = "Spyfall - Game"
        content = "Your role is ---> **%s** \nThe location is ---> *%s*" % (role, location)
        return discord.Embed(title=title, description=content)

@bot.event
async def on_message(message):
    message_delete = message
    message_author = message.author
    message_author_id = message.author.id
    message_channel = message.channel
    message_content = message.content.lower()


    if message_content.startswith(bot_trigger + 'join'):
        game.join_player(message_author_id)
        await bot.send_message(message.channel, "<@%s> has joined the game." % message_author_id)

        print(message_author)

        print(game.players)
    if message_content.startswith(bot_trigger + 'leave'):
        game.leave_player(message_author_id)
        await bot.send_message(message.channel, "<@%s> has left the game." % message_author_id)

        print(game.players)
    if message_content.startswith(bot_trigger + 'purge'):
        game.purge()
        await bot.send_message(message.channel, "All users purged!")

        print(game.players)

    if message_content.startswith(bot_trigger + 'startgame'):
        game.start_game()

        for player in game.players:
            await bot.send_message(discord.User(id=player.name), embed=embeded_message(player.role, game._game_data['locations'][game.location]['Location']))

        await bot.send_message(message.channel, "The game has started!")

        location_title = "Spyfall - Locations List"
        location_content = ''
        for i in game.loc_list:
            location_content += "**%s**\n" % i

        loc_embed = discord.Embed(title=location_title, description=location_content)

        locs = await bot.send_message(message.channel, embed=loc_embed)

        # Create a simple timer to time the game.
        time = await bot.send_message(message.channel, game.get_formatted_time())

        while not game.tick():
            await bot.edit_message(time, game.get_formatted_time())
            await asyncio.sleep(1)

        # Loop exited, game has run out of time. End it and clear messages.
        await bot.delete_message(locs)
        await bot.delete_message(time)
        await bot.send_message(message.channel, "Time is up. Vote who you think the spy is now.")

    if message_content.startswith(bot_trigger + 'players'):
        playing = 'Current Players:\n'
        for player in game.players:
            playing += "<@%s>" % player.name
            playing += ' '

        await bot.send_message(message.channel, playing)

    if message_content.startswith(bot_trigger + 'reveal'):
        reveal_title = 'Spyfall - Reveal'
        reveal_location = 'The Location Was --> %s\n' % (game._game_data['locations'][game.location]['Location'])

        reveal_players = ''
        for player in game.players:
            reveal_players += '<@%s> --> %s\n' % (player.name, player.role)

        reveal_content = reveal_location + reveal_players

        reveal_embed = discord.Embed(title=reveal_title, description=reveal_content)

        await bot.send_message(message.channel, embed=reveal_embed)
        game.end_game()

bot.run(bot_token)
