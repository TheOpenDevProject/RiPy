__author__ = 'TheOpenDevProject'
import urllib2
import json

class BasicProfileAPI:
    APIResponse = {400: "(400)Riot API - Bad Request",
                   401: "(401)Riot API - Unauthorized (Your API key was invalid or you tried to access an invalid URL)",
                   404: "(404)Riot API - Not Found",
                   429: "(429)Riot API - Rate Limit Exceeded",
                   500: "(500)Riot API - Internal Server Error (AKA Riot swung a wrecking ball into the API server)",
                   503: "(503)Riot API - Service Unavailable"
                    }
    _summonerID = None
    _summonerName = None
    _summonerProfileIconId = None
    _summonerLevel = None
    _summonerRevisionDate = None
    #Settings#
    apiKey = None
    region = None
    def __init__(self,apiKeyInit,regionInit):
        self.apiKey = apiKeyInit
        self.region = regionInit

    def requestSummonerProfile(self,summonerName):
        #Set the Data Endpoint#
        EndPoint = "https://" + self.region + ".api.pvp.net/api/lol/" + self.region + "/v1.4/summoner/by-name/" + summonerName + "?api_key=" + self.apiKey
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
        summonerInfo = jsonDocument[self.summonerName]

        self.summonerID = summonerInfo['id']

    def getSummonerName(self):
        return self._summonerName

    def getSummonerID(self):
        return self._summonerID

    def getSummonerLevel(self):
        return self._summonerLevel

    def getSummonerProfileIconID(self):
        return self._summonerProfileIconId

    def getSummonerProfileRevisionDate(self):
        return self._summonerRevisionDate