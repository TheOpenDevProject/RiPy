__author__ = 'TheOpenDevProject'
from RiPy.BasicProfile import BasicProfileAPI
from RiPy.Ranked import RankedProfileAPI
from RiPy.MatchAndStats import MatchAndStats
import io

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
summoners = {
    0:"EllipsisPlaying"



}

profile = BasicProfileAPI(apiKey, region[7])
rankedStats = RankedProfileAPI(apiKey, region[7])
MatchHistory = MatchAndStats(apiKey, region[7],15)

for j in range(0, len(summoners)):
    profile.requestSummonerProfile(summoners[j])
    rankedStats.getRankedProfile(str(profile.getSummonerID()))
    MatchHistory.requestMatchHistory(str(profile.getSummonerID()))
    with io.open("profileDumps/" + summoners[j] + ".profile",'w') as file:
        file.write(unicode("Summoner Name:" + str(profile.getSummonerName()) + "\n"))
        file.write(unicode("Summoner ID:" + str(profile.getSummonerID()) + "\n"))
        file.write(unicode("Ranked League: " + str(rankedStats.getLeagueName()) + "\n"))
        file.write(unicode("Ranked Tier: " + str(rankedStats.getRankedTier()) + "\n"))
        file.write(unicode("Ranked Division: " + str(rankedStats.getDivision()) + "\n"))
        file.write(unicode("Ranked League Points: " + str(rankedStats.getCurrentLP()) + "\n"))
        file.write(unicode("Ranked Wins: " + str(rankedStats.getRankedWins()) + "\n"))
        file.write(unicode("Ranked Hot-Streak: " + str(rankedStats.getIsHotStreak()) + "\n"))
        file.write(unicode("Ranked Tier Veteran: " + str(rankedStats.getIsVeteran()) + "\n"))
        file.write(unicode("#---End Ranked Stats---#\n"))
        file.write(unicode("Average Damage Taken: " + str(MatchHistory.getAverageDamageTaken()) + "\n"))
        file.write(unicode("Average PentaKills: " + str(MatchHistory.getAveragePentaKills()) + "\n"))
        file.write(unicode("Average Assists: " + str(MatchHistory.getAverageAssists()) + "\n"))
        file.write(unicode("Average Magic Damage: " + str(MatchHistory.getAverageMagicDamageDone()) + "\n"))
    file.close()