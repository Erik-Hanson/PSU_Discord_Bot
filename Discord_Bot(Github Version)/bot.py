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

fallTermStartDate = "2018-09-24 00:00:00"
winterTermStartDate = "2019-01-09 00:00:00"
springTermStartDate = "2019-04-02 00:00:00"
ProficiencyDemo = "2018-11-02 00:00:00"
timeFormat = '%Y-%m-%d %H:%M:%S'

fallTermCountDown = datetime.strptime(fallTermStartDate, timeFormat)
winterTermCountDown = datetime.strptime(winterTermStartDate, timeFormat)
springTermCountDown = datetime.strptime(springTermStartDate, timeFormat)
DemoCountDown = datetime.strptime(ProficiencyDemo, timeFormat)
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
        await bot.send_message(message.channel, "Fall Term Beings In : ``%d days, %d hours``" % HrMinSec(dateSecond(startDate, fallTermCountDown)))

    if message.content == "!winterterm":
        await bot.send_message(message.channel, "Winter Term Beings In : ``%d days, %d hours``" % HrMinSec(dateSecond(startDate, winterTermCountDown)))

    if message.content == "!springterm":
        await bot.send_message(message.channel, "Spring Term Beings In : ``%d days, %d hours``" % HrMinSec(dateSecond(startDate, springTermCountDown)))

    if message.content == "!demo":
        await bot.send_message(message.channel, "The next Proficiency Demo is in : ``%d days, %d hours``" % HrMinSec(dateSecond(startDate, DemoCountDown)))

bot.run('''INSERT TOKEN HERE''')
