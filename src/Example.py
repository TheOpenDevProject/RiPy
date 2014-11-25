from RiPy.BasicProfile import BasicProfileAPI

profile = BasicProfileAPI("APIKey","oce")

profile.requestSummonerProfile("SumCoolAid")

print(profile.summonerID)

