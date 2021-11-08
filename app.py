import os
import discord
from discord.ext.commands import Bot
# import RPi.GPIO as GPIO            # import RPi.GPIO module
from gpiozero import Servo  
from time import sleep             # lets us have a delay  
# GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD  
# GPIO.setup(8, GPIO.OUT)           # set GPIO24 as an output   
 
BOT_PREFIX='-'
TOKEN = (os.environ['TOKEN'])
bot = Bot(command_prefix=BOT_PREFIX)
servo = Servo(14)

def opendoor():
    # GPIO.output(8, 1)         # set GPIO8 to 1/GPIO.HIGH/True  
    # sleep(0.5)                 # wait half a second  
    # GPIO.output(8, 0)         # set GPIO8 to 0/GPIO.LOW/False  
    # sleep(0.5)                 # wait half a second 
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)
    servo.min()

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
    if message.content == "door open":
        opendoor()
        msg = "Unlocking door now!"
        await message.channel.send(msg)

bot.run(TOKEN)