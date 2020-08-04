import discord
import os
import random

from discord.ext import commands, tasks
from itertools import cycle
from discord.ext.commands import Bot

client  = commands.Bot(command_prefix = ".")

status = cycle(["My bro is eating", "Im watching TV", "My dad is on his phone"])

@client.event
async def on_ready():
    print("I'm ready!")
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("Under construction..."))
    change_status.start()

@client.event
async def on_member_join(member):
    print(f"{member} has joined the server!")

@client.event
async def on_member_remove(member):
    print(f"{member} has left the server!")    

@client.command(aliases = ["8ball", "balls"])
async def _8ball(ctx, *, question):
    responses = ["Yes", "No", "Maybe"]
    await ctx.send(f"Question: {question} \n Answer: {random.choice(responses)}")

@client.command()
async def clear(ctx, amount = 3):
    await ctx.channel.purge(limit = amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f"Banned {member.mention}")

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:  
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {member.mention}")
            return
            
@tasks.loop(seconds = 2)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command! Please try again!")

client.run(os.environ.get("Vaibhavbot"))    