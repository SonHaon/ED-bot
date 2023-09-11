import asyncio
from datetime import datetime
import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import locale_str as _t
from discord.ui import *
import random
import os
from io import BytesIO
from PIL import Image,ImageFont,ImageDraw,ImageOps
import logging
import json


class account(commands.GroupCog,name="account"):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="create",description="")
    async def create(self,interaction:discord.Interaction,username:str,mdp:str):
        await interaction.response.defer(ephemeral=True)
        with open("user_mdp.json","r") as file:
            data=json.load(file)

        existe=False
        for user in data:
            if id ==user:
                existe=True
        with open("user_mdp.json","w") as file:
            if existe:
                interaction.edit_original_response(content="tu as déjà ton compte pour le modifier fait /account edit")
            else:
                data[id]={"username":username,"mdp":mdp}
                interaction.edit_original_response(content="voila ton compte est créé")
            file.write(json.dumps(data))
                
    @app_commands.command(name="edit",description="")
    async def edit(self,interaction:discord.Interaction,username:str,mdp:str):
        await interaction.response.defer(ephemeral=True)
        with open("user_mdp.json","r") as file:
            data=json.load(file)

        pareil=False
        existe=False
        for user in data:
            if id ==user:
                existe=False
                if data[user]["username"]==username and data[user]["mdp"]==mdp:
                    pareil=True
        with open("user_mdp.json","w") as file:
            if existe:
                if pareil:
                    interaction.edit_original_response(content="tu avais déjà ce mot de passe et username")
                else:
                    data[id]={"username":username,"mdp":mdp}
                    interaction.edit_original_response(content="voila ton compte est modifié")
            else:
                interaction.edit_original_response(content="tu n'as pas encore de compte, fait /account create pour le créer")
            file.write(json.dumps(data))

    @app_commands.command(name="delete",description="")
    async def delete(self,interaction:discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        with open("user_mdp.json","r") as file:
            data=json.load(file)

        existe=False
        for user in data:
            if id ==user:
                existe=True
        with open("user_mdp.json","w") as file:
            if existe:
                del data[id]
                interaction.edit_original_response(content="voila ton compte est supprimé")
            else:
                interaction.edit_original_response(content="tu n'as pas encore de compte, fait /account create pour le créer")
            file.write(json.dumps(data))