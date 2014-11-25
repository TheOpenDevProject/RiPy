__author__ = 'TheOpenDevProject'
import urllib2
import json
from APIInternals import APIInternalsCore


class BasicProfileAPI(APIInternalsCore):
    summonerID = None
    summonerName = None
    summonerProfileIconId = None
    summonerLevel = None
    summonerRevisionDate = None

    def __init__(self, apiKeyInit, regionInit):
        self.apiKey = apiKeyInit
        self.region = regionInit

    def requestSummonerProfile(self, summonerName):
        #Set the Data Endpoint#

        EndPoint = "https://" + self.region + ".api.pvp.net/api/lol/" + self.region + "/v1.4/summoner/by-name/" + summonerName.replace(
            " ", "") + "?api_key=" + self.apiKey
        print ("Contacting Endpoint " + EndPoint)
        #Make Request To API / Store the response for processing#
        try:
            endpointBinDAT = urllib2.urlopen(EndPoint)
        except urllib2.HTTPError as errorCode:
            print(self.APIResponse[errorCode.code])

        endPointData = endpointBinDAT.read()

        #Degug ONLY#
        print(endPointData)
        #Debug ONLY#

        #Begin JSON Processing#
        jsonDocument = json.loads(endPointData)
        summonerInfo = jsonDocument[summonerName.replace(" ", "").lower()]

        self.summonerID = summonerInfo['id']
        self.summonerName = summonerInfo['name']
        self.summonerLevel = summonerInfo['summonerLevel']
        self.summonerProfileIconId = summonerInfo['profileIconId']
        self.summonerRevisionDate = summonerInfo['revisionDate']

    def getSummonerName(self):
        return self.summonerName

    def getSummonerID(self):
        return self.summonerID

    def getSummonerLevel(self):
        return self.summonerLevel

    def getSummonerProfileIconID(self):
        return self.summonerProfileIconId

    def getSummonerProfileRevisionDate(self):
        return self.summonerRevisionDate

    def getAsArray(self):
        #This will return the summoners basic profile as an ASSOCARRAY#
        summonerProfileArray = {"summonerId": self.summonerID,
                                "summonerName": self.summonerName,
                                "summonerLevel": self.summonerLevel,
                                "summonerProfileIconId": self.summonerProfileIconId,
                                "summonerRevisionDate": self.summonerRevisionDate
        }
        return summonerProfileArray