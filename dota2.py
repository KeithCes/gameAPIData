import requests

APIKey = "5B748B8084F1DCC4F23B3FEC8818B9CC"

def requestData(playerID):
    URL = "https://api.opendota.com/api/players/" + playerID
    response = requests.get(URL)
    return response.json()


def main():

    steam32bitID = "219586243"
    responseData = requestData(steam32bitID)

    mmr = responseData["competitive_rank"]

    print("MMR: " + str(mmr))


if __name__ == "__main__":
    main()

