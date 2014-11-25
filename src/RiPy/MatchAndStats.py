__author__ = 'TheOpenDevProject'
import urllib2
import json
from APIInternals import APIInternalsCore
class MatchAndStats(APIInternalsCore):
    matchHistory = {}

    def __init__(self,apiKey,region):
        self.apiKey = apiKey
        self.region = region

    def requestMatchHistory(self,summonerID):
        endPoint = "https://" + self.region + ".api.pvp.net/api/lol/" + self.region + "/v2.2/matchhistory/"+ summonerID +"?api_key=" + self.apiKey
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
        goldTotal = 0
        goldAverage = 0
        for i in range(0,nGames):
            goldTotal += self.matchHistory[i]["participants"][0]["timeline"]["goldPerMinDeltas"]["zeroToTen"]

        goldAverage = goldTotal / nGames

        return goldAverage

    #def getAverageGoldFromTenToTwenty(self):
     #   nGames = len(self.matchHistory)
      #  goldTotal = 0
       # goldAverage = 0
        #for i in range(0,nGames):
         #   if "tenToTwenty" in self.matchHistory[i][0]["timeline"]["goldPerMinDeltas"]:
          #      goldTotal += self.matchHistory[i][0]["timeline"]["goldPerMinDeltas"]["tenToTwenty"]
           # else:
            #    print("Gold Per Min For Game(" + str(i) + ") Is Missing")

