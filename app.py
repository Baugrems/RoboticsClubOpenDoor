import os
import discord
from discord.ext.commands import Bot
import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(24, GPIO.OUT)           # set GPIO24 as an output   
 
BOT_PREFIX='-'
TOKEN = (os.environ['TOKEN'])

bot = Bot(command_prefix=BOT_PREFIX)
 

def opendoor():
    GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
    sleep(0.5)                 # wait half a second  
    GPIO.output(24, 0)         # set GPIO24 to 0/GPIO.LOW/False  
    sleep(0.5)                 # wait half a second 

# @bot.group(pass_context=True)
# async def door(ctx):
#     if ctx.invoked_subcommand is None:
#     	await ctx.message.channel.send("Do what with the door?")

# @door.command(name="Open Door",
#                 description="Opens the door to robotics club",
#                 brief="Open the door",
#                 aliases=["open, access, go"],
#                 pass_context=True)
# async def open(context):
#     opendoor()
    

@bot.event
async def on_message(message):
    if message.content.contains == "door open":
        opendoor()
        msg = "Unlocking door now!"
        await message.channel.send(msg)

bot.run(TOKEN)