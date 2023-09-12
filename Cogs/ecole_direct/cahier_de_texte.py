import requests
import json
from discord.ext import commands,app_commands
import discord

from login import login
from checks import check



class cahier_de_texte(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot

    @check.has_account()
    @app_commands.command(name="cahier_de_texte",description="")
    async def cahier_de_texte(self,interaction:discord.Interaction):
        await interaction.response.defer(ephemeral=False)
        info=login()
        token=info["token"]

        url = f"https://api.ecoledirecte.com/v3/Eleves/{info['data']['accounts'][0]['id']}/cahierdetexte.awp?verbe=get"

        querystring = {"v":"4.37.1"}

        payload = {'data':"{}"}
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "content-lenght":"7",
            "authority": "api.ecoledirecte.com",
            "accept": "application/json, text/plain, */*",
            "accept-language": "fr-FR,fr;q=0.5",
            "origin": "https://www.ecoledirecte.com",
            "referer": "https://www.ecoledirecte.com/",
            "sec-ch-ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Brave\";v=\"116\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "X-Token":token
        }

        response = requests.post(url, data=payload, headers=headers, params=querystring)
        data=response.json()
        