from flask import Blueprint, render_template, redirect, request, url_for, flash
import requests
import json
import random

WrongSkill = Blueprint('WrongSkill', __name__)

# Variables Globales
random1 = 0
random1 = 0

champ1 = ""
champ2 = ""
champ3 = ""
champ4 = ""     

@WrongSkill.route("/")
def index():
    return render_template('index.html')

@WrongSkill.route("/play")
def play():

    listChampions = list()
    listUrlSpells = list()

    urlChampion = 'https://ddragon.leagueoflegends.com/cdn/11.9.1/data/es_MX/champion.json';

    res = requests.get(urlChampion)

    if res.status_code == 200:
        print('Established connect to API Riot')

        datas = res.json()

        nameAllChampions = datas['data']
        
        for champion in nameAllChampions.keys():
            listChampions.append(champion)

        numRandoms = getRandomNumbers();

        champ1 = listChampions[numRandoms[0]]
        champ2 = listChampions[numRandoms[1]]
        #champ3 = listChampions[numRandoms[2]]
        #champ4 = listChampions[numRandoms[3]]

        print(str(numRandoms[0]) + " " + champ1)
        print(str(numRandoms[1]) + " " + champ2)
        #print(str(numRandoms[2]) + " " + champ3)
        #print(str(numRandoms[3]) + " " + champ4)

        urlChamp1 = 'https://ddragon.leagueoflegends.com/cdn/11.9.1/data/es_MX/champion/' + champ1 + '.json'
        urlChamp2 = 'https://ddragon.leagueoflegends.com/cdn/11.9.1/data/es_MX/champion/' + champ2 + '.json'

        listSpells = list()
        listChamp = list()

        listChamp.append(champ2)
        #listChamp.append(champ3)
        #listChamp.append(champ4)

        res1 = requests.get(urlChamp1)
        onlyChampion1 = res1.json()

        res2 = requests.get(urlChamp2)
        onlyChampion2 = res2.json()

        image = list()

        image.append(onlyChampion1["data"][champ1]["spells"][0]["image"]["full"])
        image.append(onlyChampion1["data"][champ1]["spells"][1]["image"]["full"])
        image.append(onlyChampion1["data"][champ1]["spells"][2]["image"]["full"])
        image.append(onlyChampion1["data"][champ1]["spells"][3]["image"]["full"])

        for i in image:
            listUrlSpells.append("https://ddragon.leagueoflegends.com/cdn/11.9.1/img/spell/" + i)

        image2 = onlyChampion2["data"][champ2]["spells"][random.randrange(0,4)]["image"]["full"]
        url_img2 = "https://ddragon.leagueoflegends.com/cdn/11.9.1/img/spell/" + image2

        listUrlSpells[random.randrange(0,4)] = url_img2

    return render_template('play.html', urls = listUrlSpells, nameChamp1 = champ1, nameChamp2 = champ2, fourChampions = listChamp)

@WrongSkill.route('/confirm', methods=['POST'])
def confirm():
    if request.method == 'POST':
        textNameChamp = request.form['nameChampion']
        champ2 = request.form['champ2']
        if champ2.casefold() == textNameChamp.casefold():
            print('You win')
            flash('You win')
            return redirect(url_for('.play'))
        else:
            print('You loss')
            flash('You loss')
            return redirect(url_for('.play'))
    else:
        return render_template('index.html')


def getRandomNumbers():

    listRandomNumbers = list()

    random1 = random.randrange(0,156)
    random2 = random.randrange(0,156)
    random3 = random.randrange(0,156)
    random4 = random.randrange(0,156)

    while random1 == random2:
        random2 = random.randrange(0,156)
        if (random3 or random4) == (random1 or random2):
            random3 = random.randrange(0,156)
            
    listRandomNumbers.append(random1)
    listRandomNumbers.append(random2)
    listRandomNumbers.append(random3)
    listRandomNumbers.append(random4)

    return listRandomNumbers

