import discord
from discord.ext import commands
import asyncio
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix='@', intents=intents)
takeInputs = False
botActive = False
inputMessage = ''

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    global inputMessage
    global takeInputs
    if message.author == bot.user:
        return

    if takeInputs:
        inputMessage = message.content

    await bot.process_commands(message)

@bot.command()
async def start(ctx):
    global botActive
    if not botActive:
        botActive = True
    await ctx.send(f'Starting...')

async def input():
    global inputMessage
    global takeInputs
    inputMessage = ''
    takeInputs = True
    while inputMessage == '':
        await asyncio.sleep(0.1)
    return inputMessage

async def send_msg(message):
    channel = bot.get_channel(1281851925851144325)  # Replace with your actual channel ID
    if channel:
        await channel.send(message)
    else:
        print("Channel not found")

async def output(message):
    await send_msg(message)

async def run_bot():
    # token = temporarily not available
    await bot.start()  # Replace with your actual bot token

async def close_bot():
    await bot.close()

if __name__ == "__main__":
    asyncio.run(run_bot())