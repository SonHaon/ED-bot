import requests
import json

def login(id) -> dict:

    with open("user_mdp.json","r") as file:
        data=json.load(file)

    url = "https://api.ecoledirecte.com/v3/login.awp"

    querystring = {"v":"4.37.1"}

    payload = {
        "identifiant": data[id]["username"],
        "motdepasse": data[id]["mdp"],
        "isReLogin": False,
        "uuid": ""
    }

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
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }

    response = requests.post(url, data=payload, headers=headers, params=querystring)

    return response.json()