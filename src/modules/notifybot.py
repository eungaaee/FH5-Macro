import asyncio

import discord
from discord.ext import commands

import config # set your DISCORD_BOT_TOKEN in /src/config.py (DISCORD_BOT_TOKEN = "your_token")


description = "description"

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

ready_event = asyncio.Event()
channel = None


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    global channel
    channel = bot.guilds[0].text_channels[0]
    ready_event.set()


async def send_message(text):
    global channel
    if channel is not None:
        await channel.send(text)
    else:
        print("Channel not found.")


async def start_bot():
    await bot.start(config.DISCORD_BOT_TOKEN)


async def close_bot():
    await bot.close()


""" # Examples from the documentation
@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    await ctx.send('Yes, the bot is cool.') """


if __name__ == '__main__':
    bot.run(config.DISCORD_BOT_TOKEN)