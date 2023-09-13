import requests
import json
from discord.ext import commands
from discord import app_commands
import discord
import datetime

from .login import login
from .checks import check
from .fonction import date



class emploi_du_temps(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.bot = bot

    @check.has_account()
    @app_commands.command(name="emploi_du_temps",description="pas encore")
    async def emploi_du_temps(self,interaction:discord.Interaction,jour:str="None",mois:str="None"):
        if jour=="None":
            jour =date().day
        if mois=="None":
            mois =date().month
        await interaction.response.defer(ephemeral=False)
        info=login(str(interaction.user.id))
        token=info["token"]

        url = f"https://api.ecoledirecte.com/v3/E/{info['data']['accounts'][0]['id']}/emploidutemps.awp?verbe=get"

        querystring = {"v":"4.37.1"}
        dates=f"{date().year}-{date(int(mois)).month}-{date(int(jour)).day}"
        payload = {'data':json.dumps({
            "dateDebut": dates,
            "dateFin": dates,
            "avecTrous": False
        })}
        headers = {
            "content-type": "application/x-www-form-urlencoded",
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
        cours=data["data"]
        new_cours=[False]*24
        for i in range(len(cours)):
            new_cours[int(cours[i]["start_date"][11:-3])]=cours[i]
        embeds=[discord.Embed(title=f"Emploi du temps du {dates}")]
        for cour in new_cours:
            if cour:
                embeds.append(discord.Embed(title=f"__**{cour['text']}**__",description=f"> Professeur : {cour['prof']}\n\n> Salle : {cour['salle']}\n\n> Heures : {cour['start_date'][11:]} - {cour['end_date'][11:]}",color=discord.Color.from_str(cour["color"])))
        await interaction.edit_original_response(embeds=embeds)
        
        