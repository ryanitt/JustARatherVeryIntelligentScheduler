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
    #Do stuff/// (once bot is done I will need to change id channel)
    msg = client.get_channel(client_id)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command()
async def setup(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))
    await ctx.send('Meeting Created!')
    await ctx.send("Time:")
    await ctx.send(args[0])
    await ctx.send("Location:")
    await ctx.send(args[1])
    args = list(args)
    args.pop(0)
    args.pop(1)
    for i in range(len(args)):
        await ctx.send('Name:')
        await ctx.send(args[i])
        i = i + 1

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
