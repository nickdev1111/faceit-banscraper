import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('simp_Boop Boop Gang.csv')
df.describe()
# Team names includes previous names - should be automated later
team_names = ["Boop Boop Gang"]

# map names
maps = ["Anubis", "Overpass", "Inferno", "Ancient", "Dust2", "Nuke", "Mirage", "Vertigo"]

# initialize a insta bans dictionary
a_insta_bans = dict.fromkeys(maps, 0)
maps_played = dict.fromkeys(maps, 0)

# initializing all the possible first 3 bans
b_insta_bans_possiblities = []
for first_map in maps:
    for second_map in maps:
            for third_map in maps:
                if first_map != second_map and first_map != third_map and second_map != third_map:
                    b_insta_bans_possiblities.append((first_map,second_map,third_map))
# initiliaze the dictionary
b_insta_bans = dict.fromkeys(b_insta_bans_possiblities, 0)

# initialize the last 2 possible bans
b_final_bans_possiblities = []
for first_map in maps:
    for second_map in maps:
        if first_map != second_map:
                    b_final_bans_possiblities.append((first_map,second_map))
# initialize the dictionary
b_final_bans = dict.fromkeys(b_final_bans_possiblities, 0)


# print dictionaries nicely and EXCLUDES zero amoutns
def print_dct(dct):
    for item, amount in dct.items():  # dct.iteritems() in Python 2
        if amount != 0:
            print("{} banned {} time(s).".format(item, amount))

# iterates through each row, ie each matches vetos
for index, row in df.iterrows():
    maps_played[row['veto7']] += 1
    # teamA bo1
    if row["team_type"]==0 and row["match_type"]==1: 
        for one_map in maps:
            #if map is in veto1 adds to intsa ban counter
            if one_map in row["veto1"]:
                a_insta_bans[one_map] += 1
                
    # teamB bo1
    if row["team_type"]==1 and row["match_type"]==1: 
        # checks for the map in each veto position and records the order
        b_insta_bans[(row["veto1"],row["veto2"],row["veto3"])] += 1
        
        #print((row["veto6"],row["veto7"]))
        b_final_bans[(row["veto6"],row["veto7"])] += 1

# temporary output 
print("{} insta bans as team A in best of 1 matches:\n".format(team_names[0]))
print_dct(a_insta_bans)
print("\n{} insta bans as team B in best of 1 matches:\n".format(team_names[0]))
print_dct(b_insta_bans)
print("\n{} final bans as team B in best of 1 matches:\n".format(team_names[0]))
print_dct(b_final_bans)
print("\n{} played maps in best of 1 matches:\n".format(team_names[0]))
for item, amount in maps_played.items():
    if amount != 0:
        print("{} played {} time(s).".format(item, amount))
                    
#    if "0" in row["team_type"] and "3" in row["match_type"]: # teamA bo3
#    if "1" in row["team_type"] and "3" in row["match_type"]: # teamB bo3