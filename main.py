import re
import discord
import json
import os
import sqlite3
from discord.ext import commands
from prsaw import RandomStuff

client= commands.Bot(command_prefix="!!", case_insensitive=True)
client.remove_command("help")
rs= RandomStuff(async_mode=True)
conn= sqlite3.connect("dbs/main.db")

with open("config.json", "r") as f:
	config= json.load(f)
	f.close()

TOKEN= config['token']
extensions= [
"commands",
]

@client.event
async def on_ready():
	for extension in extensions:
		client.load_extension(f"cogs.{extension}")

	if os.name == 'nt':
		os.system("cls")
	else:
		os.system('clear')

	print("[ Discord ChatBot ]\n")
	print(f"\nCurrently Logged in as: {client.user.name}")
	print(f"ID: {client.user.id}")

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	else:
		if message.content.lower().startswith('!!'):
			await client.process_commands(message)

		message.content = re.sub('<@.*?>', '"someone"', message.content)
		cur= conn.cursor()
		guildID= str(message.guild.id)
		r= cur.execute("SELECT * FROM main WHERE guild_id = '"+guildID+"'")

		row = None
		for row in r:
			...

		if row[2] == "0":
			return

		if row == None:
			return

		elif row != None:
			if message.channel.id == int(row[1]):
				async with message.channel.typing():
					response= await rs.get_ai_response(message.content)
				await message.channel.send(response)
					
			else:
				return

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f":warning: This command is currently on cooldown. Try again in {round(error.retry_after, 2)} seconds.")

	print(error)
client.run(TOKEN)
