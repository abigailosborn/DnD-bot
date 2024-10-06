from os import system
import sqlite3
import random 
import discord
import dnd 
from discord.ext import commands

# For some reason this allows colors
# to be printed in command prompt and
# PowerShell natively?
# Source: https://stackoverflow.com/a/54955094
system("")

connection = sqlite3.connect("dnd.db")
cur = connection.cursor()

#cur.execute("CREATE TABLE player_characters(player_name, character_name, dexerity, strength, constitution, wisom, intelligence, charisma)")

res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

TOKEN: str
with open("./.token", "r") as file: TOKEN = file.read()
print(TOKEN)
ADMINS = []

characters = []
character_names = []

#setting permissions 
intents = discord.Intents.default()
#playing, listening to, eg
intents.presences = True
#server members
intents.members = True
#it's in the name 
intents.message_content = True
bot = commands.Bot(command_prefix="~", intents=intents)

#event listener 
#async: call the function but don't wait for return 
@bot.event 
async def on_ready():
    print(f"{BLUE}{bot.user.name}{RESET} connected to:")
    #As responses are received execute for loop
    async for guild in bot.fetch_guilds():
        print(f"{guild}")
#@ specifies a decorator
#ctx is god
@bot.command(name="commands")
async def on_message(ctx: commands.Context):
    #triple quote is multi line string 
    #wait until done executing to move on
    await ctx.send(f"""
    Commands:      
    - **~commands** - Display the command list (if you're here you should know that...)
    - **~d4**      - Roll a d4
    - **~d6**      - Roll a d6
    - **~d8**      - Roll a d8
    - **~d10**     - Roll a d10
    - **~d12**     - Roll a d12
    - **~d20**     - Roll a d20
    - **~d100**    - Roll a d100
    - **~spell (name of spell)** Looks up spell information (This is broken)
    - **~name**    - Randomly Generate a character name
    - **~character**  - Randomly Generate a character
    - **~mycharacters** - Display your characters
    - **~(character name)** - Display the stats for a specific character (Replace (character name) with the name of your character)(This is broken))
                   """) 

@bot.command(name = "d4")
async def on_message(ctx: commands.Context):
    await ctx.send(f"{ctx.author.display_name} rolled a **{dnd.dice_rolls.d_four()}**!")

@bot.command(name = "d6")
async def on_message(ctx: commands.Context):
    await ctx.send(f"{ctx.author.display_name} rolled a **{dnd.dice_rolls.d_six()}**!")

@bot.command(name = "d8")
async def on_message(ctx: commands.Context):
    await ctx.send(f"{ctx.author.display_name} rolled a **{dnd.dice_rolls.d_eight()}**!")

@bot.command(name = "d10")
async def on_message(ctx: commands.Context):
    await ctx.send(f"{ctx.author.display_name} rolled a **{dnd.dice_rolls.d_ten()}**!")

@bot.command(name = "d12")
async def on_message(ctx: commands.Context):
    await ctx.send(f"{ctx.author.display_name} rolled a **{dnd.dice_rolls.d_twelve()}**!")

@bot.command(name = "d20")
async def on_message(ctx: commands.Context):
    await ctx.send(f"{ctx.author.display_name} rolled a **{dnd.dice_rolls.d_twenty()}**!")

@bot.command(name = "d100")
async def on_message(ctx: commands.Context):
    await ctx.send(f"{ctx.author.display_name} rolled a **{dnd.dice_rolls.d_hundred()}**!")

@bot.command(name = 'name')
async def on_message(ctx: commands.Context):
    await ctx.send(f"{ctx.author.display_name} Your name is: **{dnd.character.gen_names()}**!")
@bot.command(name = 'spell')
async def on_message(ctx: commands.Context):
    await ctx.send(f"Your spell is!: ")

@bot.command(name = 'character')
async def on_message(ctx: commands.Context):
    stats = []
    name = dnd.character.gen_names()
    dex = dnd.character.gen_stats()
    strn = dnd.character.gen_stats()
    con = dnd.character.gen_stats()
    intel = dnd.character.gen_stats()
    wis = dnd.character.gen_stats()
    cha = dnd.character.gen_stats()
    player = ctx.author.display_name
    cur.execute("insert into player_characters(player_name, character_name, dexerity, strength, constitution, wisom, intelligence, charisma) values (?, ?, ?, ?, ?, ?, ?, ?)", (player, name, dex, strn, con, intel, wis, cha))
    connection.commit()
    res = cur.execute("SELECT character_name FROM player_characters")
    print(res.fetchall())
    stats.append(dex)
    stats.append(strn)
    stats.append(con)
    stats.append(intel)
    stats.append(wis)
    stats.append(cha)
    await ctx.send(f"""
    {ctx.author.display_name} Your character is: 
    Name: **{name}**
    Class: **{dnd.character.gen_class()}**
    Race: **{dnd.character.gen_race()}**
    Dex: **{dex}**
    Str: **{strn}**
    Con: **{con}**
    Int: **{intel}**
    Wis: **{wis}**
    Cha: **{cha}**
    """)
    my_character = (ctx.author.display_name, name, stats)
    characters.append(my_character)
    character_names(name.strip())

@bot.command(name = 'mycharacters')
async def on_message(ctx: commands.Context):
    author = ctx.author.display_name
    count = 0
    for i in characters:
        for j in characters[count]:
            if(j == author):
                await ctx.send("**Character:** ")
                for k in characters[count]:
                    await ctx.send(k)
        count += 1
        
try:
    bot.run(TOKEN)
except: pass