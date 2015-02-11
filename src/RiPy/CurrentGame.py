__author__ = 'TheOpenDevProject'
import urllib2
import json
from APIInternals import APIInternalsCore

class CurrentMatch(APIInternalsCore):
    #HACK to fix the fact that the call is different for the region to EVERY other end point ty ty
    #You might be thinking but why not just do to upper and then add a 1, You can thank LA1,LA2 for that.
    #tl;dr hooooooray for doing a reverse lookup for no point.#
    OBSModeFix = {"oce":"OC1",
                  "na":"NA1",
                  "br":"BR1",
                  "eun":"EUN1",
                  "las":"LAN1",
                  "lan":"LAN2",
                  "ru":"RU",
                  "tr":"TR1",
                  "kr":"KR"
                  }
    def __init__(self,apiKey,region):
        self.apiKey = apiKey
        self.region = region

    def requestCurrentGame(self,summonerID):
        #Get the data from the end point#
        #Simply the most creative way to f#$%^ every single call up OC1 are you srs...#
        EndPoint = "https://" +self.region + ".api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/"+ self.OBSModeFix[self.region] +"/"+ summonerID +"?api_key=" + self.apiKey
        try:
            EndPointBinDat = urllib2.urlopen(EndPoint)
        except urllib2.HTTPError as errorCode:
            print(self.APIResponse[errorCode.code])

        endPointData = EndPointBinDat.read()
        print(endPointData)

