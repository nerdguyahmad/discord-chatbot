import discord
import sqlite3
from discord.ext import commands

conn= sqlite3.connect("dbs/main.db")

class Commands(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.cooldown(1, 30, commands.BucketType.guild)
	@commands.has_permissions(manage_channels=True)

	async def setchannel(self, ctx, *, cbchannel: discord.TextChannel = None):
		if cbchannel == None:
			await ctx.send(":warning: You have to mention the channel that you want as the channel in which users will talk to me. Example: `!!setchannel #channel-name`")
			await self.setchannel.reset_cooldown(ctx)
			return
		elif cbchannel != None:
			try:
				cur= conn.cursor()
				guildID= str(ctx.guild.id)
				r= cur.execute("SELECT channel_id FROM main WHERE guild_id = '"+guildID+"'")
				row= None
				for row in r:
					...
				if row != None:
					await ctx.send(f":warning: The channel is already setup to <#{row[0]}>. Use `!!settings channel` to change it.")
				elif row == None:
					guildID= str(ctx.guild.id)
					channelID= str(cbchannel.id)

					cur.execute("INSERT INTO main(guild_id, channel_id, toggle) VALUES('"+guildID+"', '"+channelID+"', '1')")
					conn.commit()
					await ctx.send(f":tada: Start talking to me in {cbchannel.mention}!")

			except discord.NotFound:
				await ctx.send(":warning: I can't find that channel. Make sure I can access it or channel is valid.")
				return

			except discord.MissingPermissions:
				await ctx.send(":warning: I can't send messages in that channel.")
				return


	@commands.group(invoke_without_command=True)
	async def settings(self, ctx):
		em= discord.Embed(title="Discord Chat Bot Settings", description="Welcome to Discord Chat Bot Settings! Here are the list of commands you can use to setup the bot. If this is your first time with this bot, Use the `!!setchannel` command first. **Arguments enclosed in `<>` are required!**")
	
		em.add_field(name="`!!settings channel <channel_mention>`", value="Updates the chatting channel.")
		em.add_field(name="`!!settings toggle <toggle>`", value="Toggles the bot chat on or off. This doesn't disable commands.")
		await ctx.send(embed=em)

	@settings.command()
	@commands.has_permissions(manage_channels=True)
	@commands.cooldown(1, 30, commands.BucketType.guild)

	async def channel(self, ctx, *, cbchannel: discord.TextChannel = None):
		cur= conn.cursor()
		if cbchannel == None:
			guildID= str(ctx.guild.id)
			r= cur.execute("SELECT channel_id FROM main WHERE guild_id = '"+guildID+"'")
			row= None
			for row in r:
				...
			if row != None:		
				await ctx.send(f"I'm currently waiting for messages in <#{row[0]}>. Run `!!settings channel #channel-mention` to change this.")
			elif row == None:
				await ctx.send("Channel is not even setup yet! Use `!!setchannel` to set a channel.")

		elif cbchannel != None:
			guildID= str(ctx.guild.id)
			channelID= str(cbchannel.id)
			r= cur.execute("SELECT channel_id FROM main WHERE guild_id = '"+guildID+"'")
			row= None
			for row in r:
				...

			if row == None:
				await ctx.send("Channel is not even setup yet! Use `!!setchannel` to set a channel.")
			elif row != None:
				cur.execute("UPDATE main SET channel_id = '"+channelID+"' where guild_id = '"+guildID+"'")
				conn.commit()
				await ctx.send(f":tada: Channel has been updated to {cbchannel.mention}!")

	@settings.command()
	@commands.has_permissions(manage_channels=True)
	@commands.cooldown(1, 30, commands.BucketType.guild)

	async def toggle(self, ctx, *, toggle = None):
		if toggle == None:
			await ctx.send(":warning: Use the command again but mention the toggle i.e `on` or `off` For example: `!!settings toggle on` to toggle on, `!!settings toggle off` to toggle off.")
			await self.toggle.reset_cooldown(ctx)
		elif toggle != None:
			if toggle.lower() == "on":
				toggle = '1'
			elif toggle.lower() == 'off':
				toggle = '0'
			
			else:
				await ctx.send(":warning: Use the command again but mention the toggle correctly. i.e `on` or `off` For example: `!!settings toggle on` to toggle on, `!!settings toggle off` to toggle off.")
				return

			guildID= str(ctx.guild.id)
			cur= conn.cursor()
			r= cur.execute("SELECT toggle FROM main WHERE guild_id = '"+guildID+"'")
			row= None
			for row in r:
				...

			if row == None:
				await ctx.send("Channel is not setup yet! Use `!!setchannel` to set a channel.")
			elif row != None:
				cur.execute("UPDATE main SET toggle = '"+toggle+"' where guild_id = '"+guildID+"'")
				conn.commit()
				await ctx.send(f":tada: Toggle updated!")



def setup(bot):
	bot.add_cog(Commands(bot))
