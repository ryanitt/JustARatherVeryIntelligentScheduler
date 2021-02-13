import discord
from discord.ext import commands
#client (our bot)

#client = discord.Client() #### old client getter
client = commands.Bot(command_prefix = '#')
client_id = 810231896524193833
token = input("Enter Token")

@client.command(name="version")
async def Version(context):
    bot_test = client.get_channel(client_id)
    embedder = discord.Embed(title="Current Version", description="Alpha")
    embedder.add_field(name="Version code:", value="Alpha.a.1", inline=False)
    embedder.add_field(name="Release Date", value="Feburary 2021", inline = False)

    await context.message.channel.send(embed = embedder)

@client.event
async def on_ready():

    #Do stuff/// (once bot is done I will need to change id channel)
    bot_test = client.get_channel(client_id)
    await bot_test.send("Hello, I am JARVIS, your personal secretary.")
    await bot_test.send("Input '#Meeting' inorder to set up a meeting with your peers")
@client.event
async def on_reaction_add(reaction,user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} has added {} to the message {}'.format(user.name,reaction.emoji, reaction.message.content))

@client.event
async def on_reaction_remove(reaction,user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} has added {} to the message {}'.format(user.name,reaction.emoji, reaction.message.content))
@client.event
async def on_message(message):

    if message.content == "Meeting":
        bot_test = client.get_channel(client_id)
        await bot_test.send("A meeting has been requested. React to this message to RSVP")
    await client.process_commands(message)
    


@client.command("returnoftheking")
async def returnoftheking(context):
    await context.send("https://support.riotgames.com/hc/en-us/requests/new")
    await context.send("Let's bring the king home!")

   
# My Help Button
@client.command("commands")
async def commands(context):
    bot_test = client.get_channel(client_id)
    helplist = discord.Embed(title="Commands", description="Prefix for all commands is #", color=0xFF00FF)
    helplist.add_field(name="commands", value="Shows commands.", inline=True)
    helplist.add_field(name="status", value = "Gives status of Account", inline=False)
    helplist.add_field(name="version", value="Shows the version.", inline=False)
    helplist.add_field(name="traitor", value="The sneakiest snake.", inline=False)
    helplist.add_field(name="returnoftheking", value="Helps Return the king", inline=False)
    helplist.add_field(name="offense", value = "Logs", inline=False)
    await context.message.channel.send(embed = helplist)
#Run the client on the server
client.run(token)
