import discord
from discord.ext import commands
#client (our bot)

#client = discord.Client() #### old client getter
client = commands.Bot(command_prefix = '#')
client_id = 810231896524193833
client.remove_command("help")
token = input("Enter Token")

@client.command(name="version")
async def Version(context):
    msg = client.get_channel(client_id)
    embedder = discord.Embed(title="Current Version", description="Alpha")
    embedder.add_field(name="Version code:", value="Alpha.a.1", inline=False)
    embedder.add_field(name="Release Date", value="Feburary 2021", inline = False)
    await context.message.channel.send(embed = embedder)

@client.event
async def on_ready():
    #Do stuff/// (once bot is done I will need to change id channel)
    msg = client.get_channel(client_id)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command("setup")
async def setup(context):
    msg = client.get_channel(client_id)
    embedder = discord.Embed(title="First Argument ", description="Time in form HH:MM (EG: 10:00pm)")
    embedder.add_field(name="Second Argument:", value="Server Name", inline=False)
    embedder.add_field(name="Third Argument:", value="Roles of people requested for meeting.", inline=False)
    embedder.add_field(name="Finally: ", value="Please call #meeting as (#meeting time server_name roles)", inline=False)
    await context.message.channel.send(embed = embedder)

@client.command("meet")
async def meet(context, time, svrname, roles):
    await context.send(time)
    await context.send(svrname)
    await context.send(roles)
@client.command("meeting")
async def meeting(context):
    await context.send("A meeting has been requested. React to this message to RSVP.")

# My Help Button
@client.command("commands")
async def commands(context):
    msg = client.get_channel(client_id)
    helplist = discord.Embed(title="Commands", description="Prefix for all commands is #", color=0xFF00FF)
    helplist.add_field(name="commands", value="Shows commands.", inline=True)
    helplist.add_field(name="status", value = "Gives status of Account", inline=False)
    helplist.add_field(name="version", value="Shows the version.", inline=False)
    helplist.add_field(name="meeting", value="Meeting stuff.", inline=False)
    await context.message.channel.send(embed = helplist)
#Run the client on the server
client.run(token)
