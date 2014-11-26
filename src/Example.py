from RiPy.BasicProfile import BasicProfileAPI
from RiPy.Ranked import RankedProfileAPI
from RiPy.MatchAndStats import MatchAndStats

apiKey = "APIKey"
region = {0: "br",
          1: "eune",
          2: "euw",
          3: "kr",
          4: "las",
          5: "lan",
          6: "na",
          7: "oce",
          8: "tr",
          9: "ru",
          10: "global"
        }

profile = BasicProfileAPI(apiKey, region[7])
rankedStats = RankedProfileAPI(apiKey, region[7])
MatchHistory = MatchAndStats(apiKey, region[7],15)

profile.requestSummonerProfile("SumCoolAid")
MatchHistory.requestMatchHistory(str(profile.getSummonerID()))
print(str("Average Damage Taken: "+ str(MatchHistory.getAverageDamageTaken())))
