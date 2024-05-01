import requests
import json

response = requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v2/")

x = response.json()
#print(x["applist"]["apps"][0]["appid"])
#print(len(x["applist"]["apps"]))

names = []

for i in range(len(x["applist"]["apps"])):
    names.append(x["applist"]["apps"][i]["name"])

""" #print(appids)
    
appidsgame = []
    
for i in range(len(appids)):
    appidsgame.append(appids[i]//10)

    
def sumOfDigits(a) : 
    sm = 0
    while (a!=0) : 
        sm = sm + a % 10
        a = a // 10      
    return sm

biggest = 0
biggestid = []

for i in range(len(appids)):
    x = sumOfDigits(appids[i])
    if x > biggest:
        biggest = x
        print(x)
        biggestid.append(appids[i])

#print(sumOfDigits(1941401))
print(biggest)
print(biggestid) """

possible = []

for i in range(len(names)):
    if len(names[i]) == 24:
        if names[i][5] == " ":
            if names[i][8] == " ":
                if names[i][12] == " ":
                    if names[i][18] == " ":
                        possible.append(names[i])


print(possible)
