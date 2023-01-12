#Get API key stored in the config.py file (that file is included in the .gitignore)
from config import api_secret
import pprint
import requests
import os

#Clear the console
os.system('cls')

def getPhones():
    url = "https://foxway.shop/api/v1/catalogs/working/pricelist"

    querystring = {"dimensionGroupId":"1","itemGroupId":"1","vatMargin":"true"}

    payload = ""
    headers = {
        "accept": "text/json",
        "X-ApiKey": api_secret
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    return response

response = getPhones()
pprint.pprint(response.text)