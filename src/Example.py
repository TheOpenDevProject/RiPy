from RiPy.BasicProfile import BasicProfileAPI
from RiPy.Ranked import RankedProfileAPI
profile = BasicProfileAPI("APIKey","oce")
rankedStats = RankedProfileAPI("APIKey","oce")

profile.requestSummonerProfile("SumCoolAid")

rankedStats.getRankedProfile(str(profile.getSummonerID()))
print("Summoner:" + profile.getSummonerName())
print(rankedStats.getRankedTier())
print(rankedStats.getDivision())


