#PSU_Discord_Bot Created By Steven Schulze, Erik Hanson, .....

#discord api wrapper written in python
import discord
from discord.ext.commands import Bot
from discord.ext import commands
#used for discord import
import asyncio
from datetime import datetime
from datetime import time

#some variables
client = discord.Client()
bot = commands.Bot(command_prefix = "!")
eventTime = "2018-09-24 00:00:00"
wigglyText = '%Y-%m-%d %H:%M:%S'
stopDate = datetime.strptime(eventTime, wigglyText)
startDate = datetime.now()

@bot.event
async def on_ready():
    print("Test bot is ready")

def dateSecond(date1, date2):
  difference = date2 - date1
  return difference.days * 24 * 3600 + difference.seconds

def HrMinSec(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    return (days, hours)

@bot.event
async def on_message(message):
    if message.content == "suh dude?":
        await bot.send_message(message.channel, "asuh dude")


    if message.content == "!help":
        await bot.send_message(message.channel, "A list of commands so far:\n"
                                "```1. !fallterm - countdown to fall term 2018\n"
                                "2. !holidays - holidays for entire school year\n"
                                "3. !falldates - important fall dates and deadlines```")

    if message.content == "!falldates":
        file = open("fallDates.txt", "r")
        fileContents = file.read()
        await bot.send_message(message.channel, "``" + fileContents + "``")
        file.close()

    if message.content == "!holidays":
        file = open("holidays.txt", "r")
        fileContents = file.read()
        await bot.send_message(message.channel, "``" + fileContents + "``")
        file.close()

    if message.content == "!fallterm":
        await bot.send_message(message.channel, "Fall Term Beings In : ``%d days, %d hours``" % HrMinSec(dateSecond(startDate, stopDate)))

bot.run('''INSERT TOKEN HERE''')
