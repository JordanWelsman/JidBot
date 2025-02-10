# Jid's First Discord Bot

# Module Imports
import discord
import schedule

import asyncio
import json
import os
import random
import time as pytime

from discord.ext import commands

import buttons
import economy

# Bot Token
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Intents
intents = discord.Intents.default()
intents.messages = True # enable message-related events
intents.message_content = True # needed for responsing to messages

# Bot Initialization
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.command()
async def ping(ctx):
    """
    !ping
    Pings the bot
    """
    await ctx.send("Pong!")

@bot.command()
async def echo(ctx, *, content:str):
    """
    !echo <content>
    Echoes the content
    """
    await ctx.send(content)

@bot.command()
async def smile(ctx):
    """
    !smile
    Sends a smiley face
    """
    await ctx.send(":smile:")

@bot.command()
async def roll(ctx, arg:str=1):
    """
    !roll
    Rolls <n> dice and returns the sum if n>1
    Rolls a <dX> where X is the number of sides of a die
    """
    # TODO: Fix no arg given case ('!roll' should roll 1 die)
    if arg[0] in "dD":
        die_size = int(arg[1:])
        assert die_size > 0, "Die size must be bigger than 1"
        roll = random.randint(1, die_size)
        await ctx.send(f"You rolled a D{die_size} for {roll}")
    else:
        count = int(arg)
        assert count > 0, "Count must be greater than 0"
        rolls = [random.randint(1, 6) for _ in range(count)]
        if count == 1:
            await ctx.send(f"You rolled a {rolls[0]}")
        else:
            await ctx.send(f"You rolled {rolls} for a total of {sum(rolls)}")

@bot.command()
async def coinflip(ctx):
    """
    !coinflip
    Flips a coin
    """
    result = random.choice(["Heads", "Tails"])
    await ctx.send(result)

@bot.command()
async def time(ctx):
    """
    !time
    Sends the current time
    """
    await ctx.send(pytime.ctime())

@bot.command()
async def add(ctx, a:int):
    """
    !add <a>
    Adds 5 to a
    """
    await ctx.send(a + 5)

@bot.command()
async def button(ctx):
    """
    !button
    Sends a button
    """
    view = buttons.TestButtonView()
    await ctx.send("Press the button!", view=view)

@bot.command()
async def buttonmenu(ctx):
    """
    !buttonmenu
    Sends a button menu
    """
    view = buttons.RouteButtonView()
    await ctx.send("Choose a button:", view=view)

@bot.command()
async def remindme(ctx, time:int, *, message:str):
    """
    !remindme <time> <message>
    Reminds the user after <time> seconds
    """
    original_message = ctx.message # stores the original message
    await ctx.send(f"Reminding you in {time} seconds...")
    await asyncio.sleep(time) # waits for <time> seconds
    await original_message.reply(f"Reminder: {message}")


# Run Bot
bot.run(TOKEN)
