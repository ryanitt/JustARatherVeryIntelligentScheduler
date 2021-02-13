import discord
from discord.ext import commands
#client (our bot)

#client = discord.Client() #### old client getter
client = commands.Bot(command_prefix = '#')
client_id = 810231896524193833
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
    await msg.send("Hello, I am JARVIS, your personal secretary.")
    await msg.send("Input '#Meeting' inorder to set up a meeting with your peers")
@client.event
@client.event
async def on_message(message):

    if message.content == "Meeting":
        msg = client.get_channel(client_id)
        await msg.send("A meeting has been requested. React to this message to RSVP")
    await client.process_commands(message)
    

@client.command("setup")
async def setup(context):
    msg = client.get_channel(client_id)
    embedder = discord.Embed(title="First Argument ", description="Time in form HH:MM(A/Pm)")
    embedder.add_field(name="Second Argument:", value="Server Name", inline=False)
    embedder.add_field(name="Finally: ", value="Please call #meeting with required args.", inline=False)

@client.command("meeting")
async def meeting(context):
    await context.send("A meeting has been requested. React to this message to RSVP.")


@client.command("returnoftheking")
async def returnoftheking(context):
    await context.send("https://support.riotgames.com/hc/en-us/requests/new")
    await context.send("Let's bring the king home!")

   
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
