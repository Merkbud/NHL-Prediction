import pandas as pd
import player as Player
from player import Player
import goalie as Goalie
from goalie import Goalie
import team as Team
from team import Team

def read_data():
    # Read the player data from the Excel file using Pandas
    player_data = pd.read_excel('C:\\Users\\White\\NHL-Prediction\\data\\player_stats.xlsx')
    goalie_data = pd.read_excel('C:\\Users\\White\\NHL-Prediction\\data\\goalie_stats.xlsx')
    team_data = pd.read_excel('C:\\Users\\White\\NHL-Prediction\\data\\team_stats.xlsx')

    # Create a list to store the player objects
    players = []
    goalies = []
    teams = []

    # Iterate over each row in the player data
    for index, row in player_data.iterrows():
        # Create a new player object using the data from the current row
        player = Player(row['Rk'], row['Fname'], row['Age'], row['Tm'], row['Pos'], row['GP'], row['G'], row['A'], row['PTS'], row['PM'], row['PIM'], row['PS'], row['EVG'], row['PPG'], row['SHG'], row['GWG'], row['EVA'], row['PPA'], row['SHA'], row['Shots'], row['SP'], row['TOI'], row['ATOI'], row['BLK'], row['HIT'], row['FOW'], row['FOL'], row['FOP'], row['NAME'])
        
        # Add the player object to the list of players
        players.append(player)
        
    #Printing to check if it works
    #for player in players:
        #print(player)
        
    # Iterate over each row in the goalie data    
    for index, row in goalie_data.iterrows():
        # Create a new goalie object using the data from the current row
        goalie = Goalie(row['Rk'], row['Fname'], row['Age'], row['Tm'], row['GP'], row['GS'], row['W'], row['L'], row['T/O'], row['GA'], row['SA'], row['SV'], row['SVP'], row['GAA'], row['SO'], row['GPS'], row['MIN'], row['QS'], row['QSP'], row['RBS'], row['GAP'], row['GSAA'], row['G'], row['A'], row['PTS'], row['PIM'], row['NAME'])
        
        # Add the goalie object to the list of goalie data
        goalies.append(goalie)
        
    #Printing to check if it works
    #for goalie in goalies:
        #print(goalie)
        
    # Iterate over each row in the team data    
    for index, row in team_data.iterrows():
        # Create a new team object using the data from the current row
        team = Team(row['Rk'], row['Team'], row['AvAge'], row['GP'], row['W'], row['L'], row['OL'], row['PTS'], row['PTSP'], row['GF'], row['GA'], row['SOW'], row['SOL'], row['SRS'], row['SOS'], row['GF/G'], row['GA/G'], row['PP'], row['PPO'], row['PPP'], row['PPA'], row['PPOA'], row['PKP'], row['SH'], row['SHA'], row['PIM/G'], row['S'], row['SP'], row['SA'], row['SVP'], row['SO'], row['NAME'])
        
        # Add the team object to the list of teams
        teams.append(team)
        
    #Printing to check if it works
    #for team in teams:
        #print(team)

    return players, goalies, teams

#read_data()