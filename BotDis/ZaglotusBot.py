import discord 
from discord.ext import commands

client = commands.Bot (command_prefix = ".")


@client.event

async def on_ready():
 		print("Ботиха приконектилась") 


@client.command(pass_context = True)

async def hello(ctx):
	await ctx.send ("Ботиха Тут")

@client.command(pass_context = True)

async def help(ctx):
		emb = discord.Embet(title = "Все команды ботихи:")

class MyClient(discord.Client):
	 async def on_message(self, messege):
	 	 print("Messege from {0.author}:{0.content}".format(messege))
client = MyClient()
client.run("ODgxMTMwNjQ5ODc5MTk1Njc4.YSoW3Q.F04kz8ZCkmaTITk4l7z7_afh3RE")