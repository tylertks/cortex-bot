import discord
from discord.ext import commands
import re
import random

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def roll(ctx,s:str):
    try:
        results=[]
        dice=[]
        top=[]
        fumbles=0
        currentTop = 0
        currentTopIndex = 0
        to_roll = re.findall('(?:\d*?d\d+)',s.lower())
        print(to_roll)
        for roll in to_roll:
            print(list(roll))
            if(list(roll)[0] == 'd'):
                die = 0
                if(len(roll)==2):
                    die = int(list(roll)[1])
                else:
                    dlist = list(roll)
                    dlist.pop(0)
                    die = int(''.join(dlist))
                a = random.randint(1,die)
                if(a==1):
                    fumbles+=1
                results.append(a)
                print(a)
                dice.append(die)
            else:
                d = list(roll).index('d')
                num=int(''.join(list(roll)[0:d]))
                print(num)
                for x in range(0,num):
                    die = 0
                    if(len(roll)==2):
                        die = int(list(roll)[1])
                    else:
                        dlist = list(roll)
                        for y in range(0,len(str(num))+1):
                            dlist.pop(0)
                        dd = ''.join(dlist)
                        die = int(dd)
                    a = random.randint(1,die)
                    results.append(a)
                    print(a)
                    if(a==1):
                        fumbles+=1
                    dice.append(die)
        outstring = "RESULTS\n--------\n"
        for x in range(0,len(results)):
            outstring+="d"+str(dice[x])+" : "+str(results[x])+"\n"
        length = 0
        if(len(results)>2):
            length = 2
        else:
            length = 1
        usableDice = []
        for x in range(0,length):
            index = find_highest_index(results)
            top.append(results[index])
            results.pop(index)
            dice.pop(index)
        dice = remove_spoilers(results,dice)
        if(len(top)>1):
            outstring+="\nFor a roll of: "+str(top[0]+top[1])
        else:
            outstring+="\nFor a roll of: "+str(top[0])
        if(len(dice)>0):
            outstring+="\nwith an effect die of: d"+str(dice[0])
        else:
            outstring+="\nwith an effect die of: d4"
        if(fumbles>0):
            outstring+="\nand "+str(fumbles)+" spoilers"
        await ctx.send(outstring)
    except:
        await ctx.send("Sorry, I couldn't process your request")
def find_highest_index(a:list):
    highest = 0
    index = 0
    for x in range(0,len(a)):
        if(highest < a[x]):
            highest = a[x]
            index = x
    return index

def remove_spoilers(a:list, b:list):
    new_list = []
    for x in range(0,len(a)):
        if(a != 1):
            new_list.append(b[x])
    new_list.sort()
    new_list.reverse()
    return new_list

@bot.command()
async def cat(ctx):
    a = random.randint(1,10)
    catgif=""
    if(a == 1):
        catgif="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif"
    elif(a == 2):
        catgif="https://i.imgur.com/cVr63gm.gifv"
    elif(a == 3):
        catgif="https://i.imgur.com/kEDlSCp.gifv"
    elif(a == 4):
        catgif="https://i.imgur.com/OM1jAhs.gif"
    elif(a == 5):
        catgif="https://i.imgur.com/W0JfyHW.gif"
    elif(a == 6):
        catgif="https://i.imgur.com/P7RiAtO.gifv"
    elif(a == 7):
        catgif="http://i.imgur.com/LbPsLrC.gifv"
    elif(a==8):
        catgif="http://i.imgur.com/YV8DNtr.gifv"
    elif(a==9):
        catgif="https://gfycat.com/OrangeBowedAlpineroadguidetigerbeetle"
    elif(a==10):
        catgif="https://i.imgur.com/CyRKrHm.gifv"
    await ctx.send(catgif)

@bot.command()
async def alien(ctx):
    a = random.randint(1,2)
    gif=""
    if(a==1):
        alien="https://media1.tenor.com/images/0011b4161c1845e4356566c8b1619b48/tenor.gif"
    elif(a==2):
        alien="https://media1.tenor.com/images/de9a248b7c1d48703fac51da0b251bfd/tenor.gif"
    await ctx.send(alien)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Cortex Dice Roller", description="A Dice Rolling Bot for Cortex Prime", color=0xeee657) 
    # give info about you here
    embed.add_field(name="Author", value="scorche")
    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="https://discordapp.com/api/oauth2/authorize?client_id=416955698895912962&permissions=2048&scope=bot")
    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Cortex Dice Roller", description="A Dice Rolling Bot for Cortex Prime. List of commands are:", color=0xeee657)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)
    embed.add_field(name="$roll", value="$roll 2d6+d8 will roll 2 d6s and 1 d8 and return the results")
    await ctx.send(embed=embed)

bot.run('NDE2OTU1Njk4ODk1OTEyOTYy.DXL_zQ.piWWLYD-umpnwTat5pb4kjgJXN4')