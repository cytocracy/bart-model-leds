
import requests
import json
from colorama import init
from termcolor import colored
import colors
init()


stationDict = {}
curr_stations = []

def get_stations():
    data = requests.get('http://api.bart.gov/api/stn.aspx?cmd=stns&key=MW9S-E7SL-26DU-VV8V&json=y').json()
    global stations
    stations = data["root"]["stations"]["station"]
    # print(stations)
    dict_stations()

def dict_stations():
    global stationDict
    
    for x in stations:  
        stationDict[x["abbr"]] = x


def get_curr_stations():
    data = requests.get('http://api.bart.gov/api/etd.aspx?cmd=etd&orig=ALL&key=MW9S-E7SL-26DU-VV8V&json=y').json()
    for x in data["root"]["station"]:
        for i in x["etd"]:
            for j in i["estimate"]:
                if(j["minutes"] == "Leaving"):
                    #change to abbr
                    #print name in color of line

                    print(colors.get_color(j["color"].lower()) + x["name"])
                    curr_stations.append(x["name"])
                    #also get color here eventually

        # lowest = x["etd"][0]
        # for i in x["etd"]:
        #     if int(i["estimate"][0]["minutes"]) < int(lowest["estimate"][0]["minutes"]):
        #         lowest = i
        # if (int(lowest["estimate"][0]["minutes"]) <= 5):
        #     curr_stations.append(x["name"])

    # print(json.dumps(data, indent=4))

get_stations()
#print(json.dumps(stationDict, indent=4))
get_curr_stations()
curr_stations = list(set(curr_stations))
print('\033[0m'+'\nCurrent stations: \n \n' + curr_stations.__str__() + '\n')

