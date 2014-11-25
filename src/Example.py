from RiPy.BasicProfile import BasicProfileAPI

profile = BasicProfileAPI("APIKey","oce")

profile.requestSummonerProfile("SummonerName")

print("Summoner ID:" + str(profile.getSummonerID()))
print("Summoner Level:" + str(profile.getSummonerLevel()))
print("Summoner Icon ID:" + str(profile.getSummonerProfileIconID()))
