import discord
import datetime as dt
from discord.ext import commands
import db 

database = db.DataBase()


client = commands.Bot(command_prefix = '#')
client_id = 810231896524193833
client.remove_command("help")
token = input("Enter Token")


def setupDB():
    database.createTables()
    # database.createMeeting("meeting 1", 1997, 1, 31, 13, 45)
    # database.createMeeting("meeting 2", 1998, 2, 1, 7, 30)
    # database.createMeeting("meeting 3", 1999, 3, 2, 2, 00)
    # database.createMeeting("meeting 4", 2000, 4, 3, 15, 15)
    # database.createPerson("<@!103683474916925440>")
    # database.createPerson("<@!216745727857131520>")
    # database.createPerson("<@!128311377767956481>")
    
    # database.createAttendence("<@!103683474916925440>", "meeting 1")
    # database.createAttendence("<@!216745727857131520>", "meeting 3")
    # database.createAttendence("<@!128311377767956481>", "meeting 2")
    # database.createAttendence("<@!216745727857131520>", "meeting 4")
    # database.showInfo()
    database.saveToDB()

@client.event
async def on_ready():
    msg = client.get_channel(client_id)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    setupDB()

def sendtoDB(l):
    # print(l)
    # print(l[0])
    # print(dt.datetime.now().strftime("%Y-%m-%d %H:%M"))
    # run = True
    # while True:
    #     if dt.datetime.now().strftime("%Y-%m-%d %H:%M") == l[0]:
            
    #         break
    pass
            
def split(names):
    all = ''
    for i in names:
        all = all + i
    return all


@client.event
async def on_reaction_add(reaction,user):
    channel = reaction.message.channel
    await channel.send('{} has added {} to the message: {}'.format(user.name,reaction.emoji, reaction.message.content))
    print(user)

@client.event
async def on_reaction_remove(reaction,user):
    channel = reaction.message.channel
    await channel.send('{} has removed {} to the message: {}'.format(user.name,reaction.emoji, reaction.message.content))

@client.command("hello")
async def setup(context):
    embedder = discord.Embed(title = "Greetings, my name is J.A.R.V.I.S. (Just A Rather Very Intelligent Scheduler)")
    await context.message.channel.send(embed = embedder)
    
# @client.command("setuphelp")
# async def setup(context):
#     msg = client.get_channel(client_id)
#     embedder = discord.Embed(title="First Argument ", description="Time in form HH:MM (EG: 10:00pm)")
#     embedder.add_field(name="Second Argument:", value="Server Name", inline=False)
#     embedder.add_field(name="Third Argument:", value="Roles of people requested for meeting.", inline=False)
#     embedder.add_field(name="Finally: ", value="Please call #meeting as (#meeting time server_name roles)", inline=False)
#     await context.message.channel.send(embed = embedder)
@client.command()
async def setup(ctx, *args):
    args = list(args)
    print(args)
    # for_ryan = args
    # sendtoDB(for_ryan)
    if len(args) <= 1:
        embed = discord.Embed(title="Meeting Instructions", color=0xFF22FF)
        embed.add_field(name="First Argument: Date Time", value="Please enter date-time value (year-month-day hour:minute")
        embed.add_field(name="Second Argument: Location", value="Please enter location as second argument as one word or containted within " "")
        embed.add_field(name="Additional Arguments: Names", value="You can enter as many names as you want as command line arguments after the first two.")
        embed.add_field(name="When Ready", value="Create a meeting by using #setup time location names....")
        await ctx.message.channel.send(embed=embed)
    elif len(args) >= 3:
        database.createMeeting(args[1], args[0])
        for p in args[2:]:
            database.createPerson(p)
            database.createAttendence(p, args[1])
        database.saveToDB()


    embed = discord.Embed(title="Meeting Information", color=0xFF00FF)
    embed.add_field(name="Date-Time", value=args[0], inline=True)
    embed.add_field(name="Location", value=args[1], inline=True)
    args.pop(0)
    args.pop(0)
    embed.add_field(name='Names',value= split(args) ,inline=True)
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
