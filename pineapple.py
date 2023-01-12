#Get API key stored in the config.py file (that file is included in the .gitignore)
from config import api_secret
import pprint
import requests
import os
import pandas as pd
import json

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


# Write JSON response to a file
with open("./STOCK/response.json", "w") as outfile:
    json.dump(response.text, outfile)

# Load the JSON data
json_data = json.loads(response.text)

# Convert the JSON data to a DataFrame
df = pd.json_normalize(
    json_data, 
    record_path=['Dimension'],
    meta=['ProductName', 'ItemVariantId', 'Quantity', 'Price', ['Dimension']]
    )

# Export the DataFrame to a CSV file
df.to_csv("./STOCK/output.csv", index=False)