import discord 
from discord.ext import commands

client = commands.Bot (command_prefix = ".")
@client.event

async def on_ready():
 		print("Ботиха приконектилась") 


@client.command(pass_context = True)

async def hello(ctx):
	await ctx.send ("Ботиха Тут")

client.run("ODgxMTIwNjExMjQ4NzcxMTIy.YSoNhA.DMoKKqj_2lLBqrxhEpznXhM1XxM")