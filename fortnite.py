import requests

APIKey = "53488390-f0e9-4010-ac4f-98901903dccc"


def requestPlayerData(playerName):
    url = "https://api.fortnitetracker.com/v1/profile/pc/" + playerName
    headers = {"TRN-Api-Key": APIKey}
    responsePlayerData = requests.get(url, headers=headers)
    return responsePlayerData.json()


def main():
    #playerName = (str)(input('Type your Player Name here: '))
    playerName = "ninja"
    responsePlayerData = requestPlayerData(playerName)
    playerDataArray = responsePlayerData["lifeTimeStats"]
    wins = 0
    played = 0
    kd = 0
    for stat in playerDataArray:
        if stat["key"] == "Wins":
            wins = int(stat["value"])
        elif stat["key"] == "Matches Played":
            played = int(stat["value"])
        #elif stat["key"] == "Win%":
        elif stat["key"] == "K/d":
            kd = float(stat["value"])

    print("Wins: " + str(wins))
    print("Matches Played: " + str(played))
    print("K/D Ratio: " + str(kd))
    print("Win Rate: " + str(round((wins/played)*100, 2)) + "%")


if __name__ == "__main__":
    main()
