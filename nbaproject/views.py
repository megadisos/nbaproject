from django.shortcuts import render
import requests
import json
# Create your views here.
r = requests.get('https://mach-eight.uc.r.appspot.com/')
data = r.json()
def home(request):
    organize_data = sorted(data["values"],key=lambda k: k["first_name"])
    return render(request, "nbaproject/index.html",{"data":organize_data})

def details(request,name,last):
    player_info = {}
    players = []
    names = ""
    for i in data["values"]:
        if i["first_name"] == name and i["last_name"]  == last:
            player_info = {k:v for (k,v) in i.items()}
    
    for i in data["values"]:
        if int(i["h_in"]) == int(player_info["h_in"]):
            names = i["first_name"] +" "+ i["last_name"]
            players.append(names)
    print(players)            
    return render(request, "nbaproject/details.html",{"player":player_info,"players":players})
def matches(request):
    return  render(request, "nbaproject/matches.html",{"players":[],"value":0})
def get_matches(request):
    player = {}
    cont = 1
    value = int(request.GET.get("inch"))
    pairs = []
    tp = ()
    for i in data["values"]:
        player[i["first_name"]+"_"+i["last_name"]] = i["h_in"]
    mk = [k for k in player.keys()]
    for k,v in player.items():
        cont = 1
        while cont <= len(player):
            tp = ()
            if int(v) + int(player[mk[cont-1]]) == value and k!=mk[cont-1]:
                if (k,mk[cont-1]) not in pairs and (mk[cont-1],k) not in pairs:
                    tp = (k,mk[cont-1])
                    pairs.append(tp)
                    cont += 1 
            cont += 1
        # for m,c in player.items():
        #     if k !=m:
        #         if sum([int(v),int(c)]) == value:
        #             tp = (k,m)
        #             pairs.append(tp)
    if len(pairs) == 0:
        return  render(request, "nbaproject/matches.html",{"players":["NO DATA FOUND"],"value":0})
    else:           
        return  render(request, "nbaproject/matches.html",{"players":pairs,"value":value})

def organizer(request,value):
    organize_data = sorted(data["values"],key=lambda k: k[value])
    print(organize_data)
    return render(request, "nbaproject/index.html",{"data":organize_data})
