import discord
from discord.ext import commands
#client (our bot)

#client = discord.Client() #### old client getter
client = commands.Bot(command_prefix = '#')
client_id = 810231896524193833
client.remove_command("help")
token = input("Enter Token")

@client.event
async def on_ready():
    msg = client.get_channel(client_id)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def setup(ctx, *args):
    args = list(args)
    for_ryan = args
    if len(args) <= 1:
        embed = discord.Embed(title="Meeting Instructions", color=0xFF22FF)
        embed.add_field(name="First Argument: Time", value="Please enter time as first argument in the form HH:MM")
        embed.add_field(name="Second Argument: Location", value="Please enter location as second argument as one word or containted within " "")
        embed.add_field(name="Additional Arguments: Names", value="You can enter as many names as you want as command line arguments after the first two.")
        embed.add_field(name="When Ready", value="Create a meeting by using #setup time location names....")
        await ctx.message.channel.send(embed=embed)
    
    embed = discord.Embed(title="Meeting Information", color=0xFF00FF)
    embed.add_field(name="Time", value=args[0], inline=True)
    embed.add_field(name="Location", value=args[1], inline=True)
    args.pop(0)
    args.pop(0)
    embed.add_field(name='Names',value=args,inline=True )

    await ctx.message.channel.send(embed = embed)



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
    helplist.add_field(name="meeting", value="Meeting stuff.", inline=False)
    await context.message.channel.send(embed = helplist)
#Run the client on the server
client.run(token)
