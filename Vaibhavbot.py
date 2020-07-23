import discord
import os

from discord.ext import commands

client  = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("I'm ready!")

@client.event
async def on_member_join(member):
    print(f"{member} has joined the server!")

@client.event
async def on_member_remove(member):
    print(f"{member} has left the server!")    

client.run(os.environ.get("Vaibhavbot"))    