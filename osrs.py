import requests
from bs4 import BeautifulSoup

def requestHiscores(player):
    URL = "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=" + player
    #print(URL)
    response = requests.get(URL)
    rawSoup = BeautifulSoup(response.content, 'html.parser')
    return rawSoup


def main():

    playerName = "oh yeah ok"
    responseHiscores = requestHiscores(playerName)

    #print(responseHiscores)
    responseHiscoresList = str(responseHiscores).split('\n')

    skills = ["Total Level", "Attack", "Defence", "Strength", "Hitpoints", "Ranged", "Prayer", "Magic", "Cooking",
              "Woodcutting", "Fletching", "Fishing", "Firemaking", "Crafting", "Smithing", "Mining", "Herblore",
              "Agility", "Thieving", "Slayer", "Farming", "Runecrafting", "Hunter", "Construction"]
    levels = []

    # splits levels from the other useless data received like experience
    for i in range(len(skills)):
        level = responseHiscoresList[i].split(",")[1]
        levels.append(level)

    # makes a dictionary with skill names as keys and levels as values to make searching for levels easy
    skillsDict = {}
    for j in range(len(skills)):
        skillsDict[skills[j]] = levels[j]

    # prints whole dictionary line by line
    for skill, level in skillsDict.items():
        print(skill + ": " + level)

if __name__ == "__main__":
    main()

