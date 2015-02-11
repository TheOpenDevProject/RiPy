from RiPy.BasicProfile import BasicProfileAPI
from RiPy.Ranked import RankedProfileAPI
from RiPy.MatchAndStats import MatchAndStats
from RiPy.CurrentGame import CurrentMatch
apiKey = ""
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
cm = CurrentMatch(apiKey,region[7])
profile.requestSummonerProfile("")
cm.requestCurrentGame(str(profile.getSummonerID()))