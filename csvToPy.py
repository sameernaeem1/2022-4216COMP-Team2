# use pandas to manipulate the dataset
import pandas as csvr
list =csvr.read_csv('footballDataset.csv')

# create a list that store the data which has the special case of team
Premier_leagues_team = list[(list['League']=='Premier League')]
Champions_Leagues_team = list[(list['League']=='Champions League')]
season_09_to10=list[(list['Season']=='2009/2010')]
season_10_to11=list[(list['Season']=='2010/2011')]

## ie rank 5 team
team_rank5=list[(list['Rank']==5)]
team_rank2=list[(list['Rank']==2)]
team_rank1=list[(list['Rank']==1)]


## Highest Games
highest_games_team=list[(list['Games']==38)]
zeroGoals_teams=list[(list['Goals']==0)]



# this codes tell how many team is under the specific season (doesn't have to be season it's modifiable) ie.(2009 to 2010 = 130 team)
#print(len(season_09_to10)) 
#print(len(season_10_to11)) 
#print(len(team_rank1))
#print(len(team_rank2))
#print(len(team_rank5))
#print(len(highest_games_team))


print(f"The team which has zero goals are:{zeroGoals_teams}")


## create a function 