#Get API key stored in the config.py file (that file is included in the .gitignore)
from config import api_secret
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

    # Write JSON response to a file
    with open("./STOCK/response.json", "w") as outfile:
        json.dump(response.text, outfile)

    # End of the function
    return response

# Call getPhones function
response = getPhones()

# Deserialize the JSON data
df = pd.read_json(response.text)

# Extract key-value from Dimension
df["Color"] = df["Dimension"].apply(lambda x: next((item for item in x if item["Key"] == "Color"), None)["Value"])
df["Cloud Lock"] = df["Dimension"].apply(lambda x: next((item for item in x if item["Key"] == "Cloud Lock"), None)["Value"])
df["Appearance"] = df["Dimension"].apply(lambda x: next((item for item in x if item["Key"] == "Appearance"), None)["Value"])
df["Functionality"] = df["Dimension"].apply(lambda x: next((item for item in x if item["Key"] == "Functionality"), None)["Value"])
df["Boxed"] = df["Dimension"].apply(lambda x: next((item for item in x if item["Key"] == "Boxed"), None)["Value"])

df.drop("Dimension", axis=1, inplace=True)
# Write the data to a CSV file
df.to_csv('./STOCK/output.csv', index=False)
