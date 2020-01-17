import requests

APIKey = "RGAPI-52d5d582-3f9b-4c96-9e3a-e315253ac0b2"

def requestSummonerData(region, summonerName):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    #print(URL)
    response = requests.get(URL)
    return response.json()


def requestRankedData(region, ID):
    URL = "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + ID + "/?api_key=" + APIKey
    #print(URL)
    response = requests.get(URL)
    return response.json()


def main():
    region = "NA1"
    summonerName = "iceblitz"
    responseSummonerData = requestSummonerData(region, summonerName)


    ID = responseSummonerData['id']
    ID = str(ID)

    responseRankedData = requestRankedData(region, ID)

    league = responseRankedData[0]['tier']
    rank = responseRankedData[0]['rank']
    LP = responseRankedData[0]['leaguePoints']
    wins = responseRankedData[0]['wins']
    losses = responseRankedData[0]['losses']

    print(league + " " + rank)
    print("LP: " + str(LP))
    print("Wins: " + str(wins))
    print("Losses: " + str(losses))


if __name__ == "__main__":
    main()

