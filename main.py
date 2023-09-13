import asyncio
from pathlib import Path
import discord
from discord.ext import commands
from discord import app_commands, Locale
from discord.ui import *
import random
import os
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image,ImageFont,ImageDraw,ImageOps
import logging
import logging.handlers
import deepl
from discord.app_commands import Translator, locale_str, TranslationContext, TranslationContextLocation


from Cogs_sommaire import *
load_dotenv(".env")
TOKEN = os.getenv("TOKEN")
guild = discord.Object(id="1022844623372165260")

logger = logging.getLogger('discord.artichauds')
logger.setLevel(logging.INFO)





class bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents = intents,command_prefix="%µ¨£%£µ%",help_command=None)
        
    async def setup_hook(self):
        await self.add_cog(account(self),guild=guild)
        await self.add_cog(emploi_du_temps(self),guild=guild)

        await self.tree.sync(guild=guild)
        await self.tree.sync()


    async def on_ready(self):
        await self.wait_until_ready()
        

SonHaon_Bot = bot()
tree = SonHaon_Bot.tree

@tree.error
async def on_app_command_error(interaction:discord.Interaction,error):
    if isinstance(error,app_commands.BotMissingPermissions):
        try:
            await interaction.response.send_message(content="je n'ai pas les permissions de faire ça",ephemeral=True)
        except:
            await interaction.edit_original_response(content="je n'ai pas les permissions de faire ça")
    elif isinstance(error, app_commands.MissingPermissions or app_commands.MissingRole or app_commands.MissingAnyRole):
        try:
            await interaction.response.send_message(content="vous ne pouvez pas faire ça",ephemeral=True)
        except:
            await interaction.edit_original_response(content="vous ne pouvez pas faire ça")
    elif isinstance(error,app_commands.CheckFailure):
        try:
            await interaction.response.send_message(content="vous ne pouvez pas faire ça",ephemeral=True)
        except:
            await interaction.edit_original_response(content="vous ne pouvez pas faire ça")
    else:
        embed=discord.Embed(title="Une erreur inattendue est survenue",description=f"""```{error}```\ncopie-colle l’erreur et mentionne {SonHaon_Bot.member.SonHaon.mention} avec l’erreur""")
        try:
            await interaction.response.send_message(embed=embed,ephemeral=True)
        except:
            await interaction.edit_original_response(embed=embed)
        raise error
    
SonHaon_Bot.run(TOKEN)