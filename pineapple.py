#Get API key stored in the config.py file (that file is included in the .gitignore )
import time
from config import api_secret
import requests
import os
import pandas as pd
import json
import logging

#Clear the console
os.system('cls')

#We set a folder to work with
chemin = os.path.dirname(os.path.realpath(__file__))

# Configure Logging
logging.basicConfig(filename=chemin+"/log/log.txt", level=logging.DEBUG,
                    format="%(asctime)s %(message)s", filemode="a")
logging.debug("Program Launched")
# logging.debug("Debug logging test...")
# logging.info("Program is working as expected")
# logging.warning("Warning, the program may not function properly")
# logging.error("The program encountered an error")
# logging.critical("The program crashed")


print(
    '''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⢻⡄⠀⠀⠀⣠⡀⠀⠀⣰⣿⠋⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⠀⢧⠀⠀⢠⢿⡇⢀⠞⢹⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡀⠀⠀⠀⠀⡄⠀⠀⢸⠀⠘⡆⢠⠏⢸⣧⠋⠀⡿⠀⠀⠀⠀⢀⡀⠀
⠀⠀⠈⠿⡶⢤⣀⠀⢻⡷⣄⢸⠀⠀⢻⡏⠀⣸⠋⠀⢸⠃⠀⠀⣀⣴⣾⠿⠀
⠀⠀⠀⠀⠙⣦⠈⠳⣄⣳⠈⢿⠀⠀⠀⢧⣰⠃⠀⠀⣾⣠⠴⠋⣱⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠈⢣⠀⠀⠙⢦⣸⠀⠀⠀⢸⠃⠀⢀⡼⠛⠁⢀⡼⠃⠀⠀⠀⠀
⢀⣄⣀⣀⣀⣀⠀⢷⠀⠀⠀⠙⣤⡀⢀⡏⠀⣠⠟⠀⠀⠀⡜⢁⣀⣤⣴⡶⠀
⠈⠉⠑⠲⣌⡉⠉⠚⠣⣤⡀⠀⠈⢳⣘⠀⡴⠁⠀⢀⣠⠜⠋⢉⡵⠞⠁⠀⠀
⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠉⠳⢤⡀⠹⡞⠀⣠⠶⠉⠀⢀⡴⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠙⠛⢁⡼⠁⠀⠀⢨⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡄⠀⠀⠀⢠⠏⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠛⠲⢄⡀⠟⠀⣀⣤⠤⠾⢳⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡴⠛⣧⠀⠀⢀⡤⠟⠻⢯⡁⠀⠀⢀⣰⠟⢷⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⠏⠀⠀⠈⣷⣴⡋⠀⠀⠀⠈⠳⣄⣴⠋⠀⠀⠀⢻⡄⠀⠀⠀⠀
⠀⠀⢀⡿⣇⠀⠀⣰⠞⠁⠈⢳⡀⠀⠀⢀⣤⠟⠉⠳⣄⠀⠀⠀⣻⣧⠀⠀⠀
⠀⠀⡼⠀⣹⡦⣾⠁⠀⠀⠀⠀⠻⣄⣠⠞⠁⠀⠀⠀⠈⢓⡦⣿⠋⢹⡄⠀⠀
⠀⣸⣧⠞⠁⠀⠙⢦⡀⠀⠀⣠⡴⠋⠙⠢⣄⠀⠀⠀⣰⠋⠁⠙⢦⡀⣧⠀⠀
⠀⡿⣇⠀⠀⠀⠀⠀⢱⣤⣼⠃⠀⠀⠀⠀⠀⠑⣦⣞⠁⠀⠀⠀⠀⠉⣻⣷⠀
⢸⡇⠘⢦⡀⠀⣀⠴⠋⠁⠈⠳⣄⡀⠀⢀⡴⠚⠁⠈⠳⢦⣀⠀⢀⡾⠉⢸⠀
⠸⡇⢀⡤⠟⠿⣄⠀⠀⠀⠀⠀⠀⣙⡶⢇⠀⠀⠀⠀⠀⠀⢈⡿⠻⠤⣀⣸⠀
⢀⣿⠋⠀⠀⠀⠙⢦⡀⠀⠀⢠⠞⠋⠀⠈⠳⣄⠀⠀⢀⡴⠋⠀⠀⠀⠀⣹⡆
⢨⣿⡄⠀⠀⠀⠀⠀⠙⣦⣴⠋⠀⠀⠀⠀⠀⠈⣹⠒⢯⣀⠀⠀⠀⠀⣰⠋⡇
⠈⣷⠙⣦⠀⠀⢀⣴⠎⠉⠙⢧⡀⠀⠀⠀⢀⡼⠁⠀⠀⠈⠑⠦⣤⣾⡁⢰⠇
⠀⠸⡇⢈⣳⢤⡞⠁⠀⠀⠀⠀⠙⠲⣤⣴⠋⠀⠀⠀⠀⠀⢀⡼⠁⠀⠉⣻⠀
⠀⠐⢿⠉⠀⠀⠹⢦⡀⠀⠀⣠⠴⠋⠁⠀⠙⠢⣄⣀⣀⡴⠋⠀⠀⠀⡼⠇⠀
⠀⠀⠈⠳⣄⠀⠀⠀⠙⣲⠺⢥⣀⠀⠀⠀⠀⢠⡴⠋⠉⠓⠢⢤⣠⡾⠃⠀⠀
⠀⠀⠀⠀⠈⠳⣤⠖⠋⠀⠀⠀⠉⠓⢤⣠⠞⠁⠀⠀⠀⠀⢀⣠⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠙⠲⠶⠤⠤⣄⣀⣼⣁⣀⣀⣠⠤⠶⠋⠉⠀⠀⠀⠀⠀⠀
    ''')

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
print("Downloading stock from Fowxway.shop")
response = getPhones()
print("Done ✅")
print("------------------------------------------------------------------------------------------")

def createCSV():
    print("Save CSV to ./STOCK/")
    # Deserialize the JSON data
    df = pd.read_json(response.text)

    # Extract key-value from Dimension
    df["Color"] = df["Dimension"].apply(lambda x: next((item for item in x if item["Key"] == "Color"), None)["Value"])
    df["Cloud Lock"] = df["Dimension"].apply(lambda x: next((item for item in x if item["Key"] == "Cloud Lock"), None)["Value"])
    df["Appearance"] = df["Dimension"].apply(lambda x: next((item for item in x if item["Key"] == "Appearance"), None)["Value"])
    df["Functionality"] = df["Dimension"].apply(lambda x: next((item for item in x if item["Key"] == "Functionality"), None)["Value"])
    df["Boxed"] = df["Dimension"].apply(lambda x: next((item for item in x if item["Key"] == "Boxed"), None)["Value"])

    # We extracted all values needed from "Dimension", now we can remove this
    #df.drop("Dimension", axis=1, inplace=True)

    # Write the data to a CSV file
    df.to_csv('./STOCK/output.csv', index=False)
    print("Done ✅")
    print("------------------------------------------------------------------------------------------")

# Call the function to create CSV
createCSV()

#Sleep for X seconds then quit
print("------------------------------------------------------------------------------------------")
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r'+'Finished. Exiting in : ')
        time.sleep(1)
        time_sec -= 1

    print("stop")
countdown(5)
