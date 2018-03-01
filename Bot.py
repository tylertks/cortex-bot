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
        await ctx.send(outstring)
    except:
        await ctx.send("Sorry, I couldn't process your request")

@bot.command()
async def cr(ctx,s:str):
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
        if(len(results)>1):
            length = 2
        else:
            length = 1
        usableDice = []
        for x in range(0,length):
            index = find_highest_index(results)
            if(results[index] != 1):
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
        if(fumbles==1):
            outstring+="\nand "+str(fumbles)+" spoiler"
        elif(fumbles > 1):
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
    #a = random.randint(1,10)
    catlist = [
    "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif"
    ,"https://i.imgur.com/cVr63gm.gifv"
    ,"https://i.imgur.com/kEDlSCp.gifv"
    ,"https://i.imgur.com/OM1jAhs.gif"
    ,"https://i.imgur.com/W0JfyHW.gif"
    ,"https://i.imgur.com/P7RiAtO.gifv"
    ,"http://i.imgur.com/LbPsLrC.gifv"
    ,"http://i.imgur.com/YV8DNtr.gifv"
    ,"https://gfycat.com/OrangeBowedAlpineroadguidetigerbeetle"
    ,"https://i.imgur.com/CyRKrHm.gifv"
    ]
    a = random.randint(0,len(catlist)-1)
    catgif=catlist[a]
    await ctx.send(catgif)

@bot.command()
async def dog(ctx):
    doglist = [
    "https://imgur.com/WO1b8ox"
    ,"https://gfycat.com/UnderstatedCourageousIberiannase"
    ]
    a = random.randint(0,len(doglist)-1)
    doggif = doglist[a]
    await ctx.send(doggif)

@bot.command()
async def dicks(ctx):
    dicklist = [
        "https://i.imgur.com/2i6fTNP.gif"
        ,"http://stream1.gifsoup.com/view3/4291631/weird-guy-slap-dong-pole-o.gif"
    ]
    a = random.randint(0,len(dicklist)-1)
    dickgif = dicklist[a]
    await ctx.send(dickgif)

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
    embed.add_field(name="$dog", value="Gives a cute dog gif")
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)
    embed.add_field(name="$cr", value="$cr 2d6+d8 will roll 2 d6s and 1 d8 and return the results with cortex rules applied Dice can be separate with any character that is not whitespace, a number or the letter 'd'")
    embed.add_feidl(name="$roll", value="Rolls dice just like $cr, but without the cortex interpretation (no spoilers, effect die, etc)")
    await ctx.send(embed=embed)

connectString = open('connectstring.txt','r')
bot.run(connectString.readline())
#bot.run('NDE2OTU1Njk4ODk1OTEyOTYy.DXL_zQ.piWWLYD-umpnwTat5pb4kjgJXN4')