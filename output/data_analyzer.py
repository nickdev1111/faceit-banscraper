import pandas as pd
# permutations using library function to generate map permutations
from itertools import permutations 

# Read the CSV file into a DataFrame
df = pd.read_csv('simp_tokyo.csv')

# Team names includes previous names - should be automated later
team_names = ["tokyo"]

# map names
maps = ["Anubis", "Overpass", "Inferno", "Ancient", "Dust2", "Nuke", "Mirage", "Vertigo"]

# initializing 2 and 3 map permutation
two_map_perms = permutations(maps, 2)
three_map_perms = permutations(maps, 3)
five_map_perms = permutations(maps, 5)

# initiliaze the team ban dictionaries
a_insta_bans = dict.fromkeys(maps, 0)
a_final_bans = dict.fromkeys(five_map_perms, 0)
b_insta_bans = dict.fromkeys(three_map_perms, 0)
b_final_bans = dict.fromkeys(two_map_perms, 0)
maps_played  = dict.fromkeys(maps, 0)

# print dictionaries nicely and EXCLUDES zero amounts
def print_dct(dct):
    for item, amount in dct.items():  # dct.iteritems() in Python 2
        if amount != 0:
            print(f"{item} banned {amount} time(s).")

# iterates through each row, ie each matches vetos
for index, row in df.iterrows():
    maps_played[row["veto7"]] += 1
    
    # teamA bo1
    if row["team_type"]==0 and row["match_type"]==1: 
        for map in maps:
            #if map is in veto1 adds to intsa ban counter
            if map in row["veto1"]:
                a_insta_bans[map] += 1
                
            # checks for the map in each veto position and records the order
            a_final_bans[(row["veto1"],row["veto2"],row["veto3"],row["veto4"],row["veto5"])] += 1
                
    # teamB bo1
    if row["team_type"]==1 and row["match_type"]==1: 
        # checks for the map in each veto position and records the order
        b_insta_bans[(row["veto1"],row["veto2"],row["veto3"])] += 1
        
        # print((row["veto6"],row["veto7"]))
        b_final_bans[(row["veto6"],row["veto7"])] += 1

# temporary output 
print("\n{}'s maps played in best of 1 matches:\n".format(team_names[0]))
for item, amount in maps_played.items():
    if amount != 0:
        print(f"{item} played {amount} time(s).")
print("\n{} insta bans as team A in best of 1 matches:\n".format(team_names[0]))
print_dct(a_insta_bans)
print("\n{} final bans as team A in best of 1 matches:\n".format(team_names[0]))
print_dct(a_final_bans)
print("\n{} insta bans as team B in best of 1 matches:\n".format(team_names[0]))
print_dct(b_insta_bans)
print("\n{} final bans as team B in best of 1 matches:\n".format(team_names[0]))
print_dct(b_final_bans)
                    
#    if "0" in row["team_type"] and "3" in row["match_type"]: # teamA bo3
#    if "1" in row["team_type"] and "3" in row["match_type"]: # teamB bo3