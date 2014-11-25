from RiPy.BasicProfile import BasicProfileAPI
from RiPy.Ranked import RankedProfileAPI
profile = BasicProfileAPI("16e553c8-70cf-44cf-95b4-81c6c2269bee","oce")
rankedStats = RankedProfileAPI("16e553c8-70cf-44cf-95b4-81c6c2269bee","oce")

profile.requestSummonerProfile("KeepCalmGainLP")

rankedStats.getRankedProfile(str(profile.getSummonerID()))
print("Summoner:" + profile.getSummonerName())
print(rankedStats.getRankedTier())
print(rankedStats.getDivision())


