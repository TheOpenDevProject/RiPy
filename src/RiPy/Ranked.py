__author__ = 'TheOpenDevProject'
from APIInternals import APIInternalsCore
import urllib2
import json

class RankedProfileAPI(APIInternalsCore):

    #Solo5x5 Ranked Members#
    leagueName = None
    leaguePoints = None
    isFreshBlood = None
    isHotStreak = None
    division = None
    isInactive = None
    isVeteran = None
    rankedWins = None
    rankedTier = None

    def __init__(self,apiKey,region):
            self.region = region
            self.apiKey = apiKey


    def getRankedProfile(self,summonerID):
        endPoint = "https://" + self.region +".api.pvp.net/api/lol/"+ self.region +"/v2.5/league/by-summoner/"+ summonerID +"/entry?api_key=" + self.apiKey
        print("Contacting Endpoint: " + endPoint)

        try:
            endpointBinDAT = urllib2.urlopen(endPoint)
        except urllib2.HTTPError as errorCode:
            print(self.APIResponse[errorCode.code])

        endPointData = endpointBinDAT.read()

        #Begin JSON Processing#
        jsonDocument = json.loads(endPointData)
        rankedInfo = jsonDocument[summonerID]
        self.parseRankedStats(rankedInfo)

    def parseRankedStats(self,rankedInfoJSON):
        self.leagueName = rankedInfoJSON[0]["name"]
        self.leaguePoints = rankedInfoJSON[0]["entries"][0]["leaguePoints"]
        self.isFreshBlood = rankedInfoJSON[0]["entries"][0]["isFreshBlood"]
        self.isHotStreak = rankedInfoJSON[0]["entries"][0]["isHotStreak"]
        self.division = rankedInfoJSON[0]["entries"][0]["division"]
        self.isInactive = rankedInfoJSON[0]["entries"][0]["isInactive"]
        self.isVeteran = rankedInfoJSON[0]["entries"][0]["isVeteran"]
        self.rankedWins = rankedInfoJSON[0]["entries"][0]["wins"]
        self.rankedTier = rankedInfoJSON[0]["tier"]

    def getLeagueName(self):
        return self.leagueName

    def getCurrentLP(self):
        return self.leaguePoints

    def getIsFreshBlood(self):
        return self.isFreshBlood

    def getIsHotStreak(self):
        return self.isHotStreak

    def getDivision(self):
        return self.division

    def getIsInactive(self):
        return self.isInactive

    def getIsVeteran(self):
        return self.isVeteran

    def getRankedWins(self):
        return self.rankedWins

    def getRankedTier(self):
        return self.rankedTier