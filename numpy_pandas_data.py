import pandas as pd
import numpy as np

def np_ar_pd_df():
    # Read the player data from the Excel file using Pandas
    player_data = pd.read_excel('C:\\Users\\White\\NHL-Prediction\\data\\player_stats.xlsx')
    goalie_data = pd.read_excel('C:\\Users\\White\\NHL-Prediction\\data\\goalie_stats.xlsx')
    team_data = pd.read_excel('C:\\Users\\White\\NHL-Prediction\\data\\team_stats.xlsx')

    # Convert the data to numpy arrays
    player_array = np.array(player_data)
    goalie_array = np.array(goalie_data)
    team_array = np.array(team_data)

    # Create dataframes from the numpy arrays
    player_df = pd.DataFrame(player_array, columns=player_data.columns)
    goalie_df = pd.DataFrame(goalie_array, columns=goalie_data.columns)
    team_df = pd.DataFrame(team_array, columns=team_data.columns)

    #Printing to check if it works
    print(player_df)
    print(goalie_df)
    print(team_df)

    return player_df, goalie_df, team_df
