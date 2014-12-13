__author__ = 'TheOpenDevProject'
import urllib2
import json
from APIInternals import APIInternalsCore
class MatchAndStats(APIInternalsCore):
    matchHistory = {}
    sampleSize = 10
    def __init__(self,apiKey,region,sampleSize):
        self.apiKey = apiKey
        self.region = region
        self.sampleSize = sampleSize
    def requestMatchHistory(self,summonerID):
        endPoint = "https://" + self.region + ".api.pvp.net/api/lol/" + self.region + "/v2.2/matchhistory/"+ summonerID +"?beginIndex=0&endIndex="+ str(self.sampleSize) +"&api_key=" + self.apiKey
        print("Contacting EndPoint:" + endPoint)

        try:
            endPointBinDAT = urllib2.urlopen(endPoint)
            endPointData = endPointBinDAT.read()
            jsonDocument = json.loads(endPointData)
            self.parseMatchHistory(jsonDocument)
        except urllib2.HTTPError as errorCode:
            print(self.APIResponse[errorCode.code])

    def parseMatchHistory(self,jsonDocument):
        for i in range(0,len(jsonDocument["matches"])):
            self.matchHistory[i] = jsonDocument["matches"][i]

    #This function will return the JSON of a specific match#
    def getMatchByID(self,matchID):
        return self.matchHistory[matchID]

    def getAverageGoldBeforeTen(self):
        nGames = len(self.matchHistory)
        print("Sample Size: " + str(nGames))
        goldTotal = 0
        goldAverage = 0
        for i in range(0,nGames):
            goldTotal += self.matchHistory[i]["participants"][0]["timeline"]["goldPerMinDeltas"]["zeroToTen"]

        goldAverage = goldTotal / nGames

        return goldAverage

    def getAverageDamageTaken(self):
        nGames = len(self.matchHistory)
        print("Sample Size: " + str(nGames))
        totalDamage = 0
        averageDamage = 0
        for i in range (0,nGames):
            print()
            totalDamage += self.matchHistory[i]["participants"][0]["stats"]["totalDamageTaken"]

        averageDamage = totalDamage / nGames

        return averageDamage

    def getAveragePentaKills(self):
        nGames = len(self.matchHistory)
        print("Sample Size: " + str(nGames))
        totalPentaKills = 0
        averagePentaKills = 0
        for i in range (0,nGames):
            totalPentaKills += self.matchHistory[i]["participants"][0]["stats"]["pentaKills"]
        averagePentaKills = totalPentaKills / nGames

        return averagePentaKills

    def getAverageAssists(self):
        nGames = len(self.matchHistory)
        assistTotal = 0
        assistAverage = 0
        for i in range(0,nGames):
            assistTotal += self.matchHistory[i]["participants"][0]["stats"]["assists"]
        assistAverage = assistTotal / nGames
        return assistAverage

    def getAverageMagicDamageDone(self):
        nGames = len(self.matchHistory)
        totalMagicDamage = 0
        averageMagicDamage = 0
        for i in range(0, nGames):
            totalMagicDamage += self.matchHistory[i]["participants"][0]["stats"]["magicDamageDealt"]
        averageMagicDamage = totalMagicDamage / nGames
        return averageMagicDamage