import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('mod_tokyo.csv')

# Team names includes previous names - should be automated later
team_names = ["tokyo","TOKYO","F5 Esports","StompGods"]

# map names
maps = ["Anubis", "Overpass", "Inferno", "Ancient", "Dust2", "Nuke", "Mirage", "Vertigo"]

# initialize new columns of the simplified data frame
team_types = []
match_types = []

# initialize df_final
df_temp_vetoes = pd.DataFrame(columns=['veto1','veto2','veto3','veto4','veto5','veto6','veto7'])

# iterates through each row, ie each matches vetos
for index, row in df.iterrows():
    # initialize the veto order
    ordered_maps = []
    # checks for the map in each veto position and records the order
    for i in range(1,8):
        for one_map in maps:
            #if map is in veto than record which map
            if one_map in row["veto"+str(i)]:
                ordered_maps.append(one_map)
    
    # filters out 1v1 tourny
    if ordered_maps != []:
        # each for loop runs through all the teams names current/prev and
        # checks if they are team A/B by search veto1 and veto2 respectively
        for team in team_names:
            if team in row["veto1"]:
                team_types.append(0) # 0 = team A
            elif team in row["veto2"]:
                team_types.append(1) # 1 = team B
            
        # sets match type as bo3
        if "picked" in row["veto3"]:
            # adds 3 to column match type
            match_types.append(3)
            #sets match type as bo5
            if "picked" in row["veto6"]:
                # adds 5 to column match type
                match_types.append(5)
        # sets match type as bo1
        else:
            # adds 1 to column match type
            match_types.append(1)
    
        # temp variables to place into simplified data frame
        m1,m2,m3,m4,m5,m6,m7 = ordered_maps
        # temp data frame to append the simplified data frame
        df_temp = {'veto1': m1, 'veto2': m2, 'veto3': m3, 'veto4': m4, 'veto5': m5, 'veto6': m6, 'veto7': m7}
        # adding the ordered maps to the simplified dataframe
        df_temp_vetoes = df_temp_vetoes._append(df_temp, ignore_index=True)
###############################################################################################
# add column match type
df_types = pd.DataFrame({'match_type': match_types, 'team_type': team_types})
# joins the type with the maps
df_final = pd.concat([df_types, df_temp_vetoes], axis=1)

# Write the filtered DataFrame to a new CSV file
df_final.to_csv('simp_tokyo.csv', index=False)