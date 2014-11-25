__author__ = 'TheOpenDevProject'
from APIInternals import APIInternalsCore
class MatchAndStats(APIInternalsCore):


    def __init__(self,apiKey,region):
        self.apiKey = apiKey
        self.region = region

    def requestMatchHistory(self,summonerID):
        endPoint = "https://" + self.region + ".api.pvp.net/api/lol/" + self.region + "/v2.2/matchhistory/"+ summonerID +"?api_key=" + self.apiKey
        print("Contacting EndPoint:" + endPoint)
        