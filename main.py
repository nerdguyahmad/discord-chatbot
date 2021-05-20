import discord
import os
import json
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

		cur= conn.cursor()
		guildID= str(message.guild.id)
		cur= cur.execute("SELECT * FROM main WHERE guild_id = '"+guildID+"'")

		cur= cur.fetchone()

		if cur == None: # If channel isn't setup
			return

		if cur[2] == "0": # If chatbot is toggled off
			return

		if message.channel.id == int(cur[1]): # If channel is the chatting channel.
			async with message.channel.typing():
				try:
					msg = message.content
					if message.mentions != []:
						for i in message.mentions:
							msg = msg.replace(f'<@!{i.id}>', i.name)

					response= await rs.get_ai_response(msg)
				except json.decoder.JSONDecodeError:
					await asyncio.sleep(3)
					response= await rs.get_ai_response(msg)
						
			await message.channel.send(response)
					
		else:
			return

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandOnCooldown):
		await ctx.send(f":warning: This command is currently on cooldown. Try again in {round(error.retry_after, 2)} seconds.")

	print(error)
client.run(TOKEN)
