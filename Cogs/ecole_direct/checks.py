import discord
from discord import app_commands
import json

class check:
    def has_account():
        def predicate(interaction: discord.Interaction) -> bool:
            with open("user_mdp.json","r") as file:
                data=json.load(file)

            for user in data:
                if interaction.user.id ==user:
                    return True
            return False
        return app_commands.check(predicate)
        