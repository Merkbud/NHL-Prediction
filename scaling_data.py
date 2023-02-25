from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

# Import the dataframes
from numpy_pandas_data import np_ar_pd_df

players_df, goalies_df, teams_df = np_ar_pd_df()

#print(players_df.columns)
#print(goalies_df.columns)

# Separate the text features from the numeric features
players_text = players_df[['Fname', 'Tm', 'Pos', 'NAME', 'ATOI']]
players_numeric = players_df.drop(['Fname', 'Tm', 'Pos', 'NAME', 'ATOI'], axis=1)

goalies_text = goalies_df[['Fname', 'Tm', 'NAME']]
goalies_numeric = goalies_df.drop(['Fname', 'Tm', 'NAME'], axis=1)

teams_text = teams_df[['Team', 'NAME']]
teams_numeric = teams_df.drop(['Team', 'NAME'], axis=1)

# Create a scaler object
scaler = StandardScaler()

# Scale the numeric data
players_numeric_scaled = scaler.fit_transform(players_numeric)
goalies_numeric_scaled = scaler.fit_transform(goalies_numeric)
teams_numeric_scaled = scaler.fit_transform(teams_numeric)

# Combine the text features with the scaled numeric data
players_combined = np.column_stack((players_text, players_numeric_scaled))
goalies_combined = np.column_stack((goalies_text, goalies_numeric_scaled))
teams_combined = np.column_stack((teams_text, teams_numeric_scaled))

# Convert the combined data back to a pandas dataframe
players_df_scaled = pd.DataFrame(players_combined, columns=['Fname', 'Tm', 'Pos', 'NAME', 'ATOI'] + players_numeric.columns.tolist())
goalies_df_scaled = pd.DataFrame(goalies_combined, columns=['Fname', 'Tm', 'NAME'] + goalies_numeric.columns.tolist())
teams_df_scaled = pd.DataFrame(teams_combined, columns=['Team', 'NAME'] + teams_numeric.columns.tolist())

# Print the scaled dataframes
print(players_df_scaled)
print(goalies_df_scaled)
print(teams_df_scaled)
