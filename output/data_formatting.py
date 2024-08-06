import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('DeathByGamers.csv')

# Filter out rows where the second column has empty lists
df_filtered = df[df['veto_data'].apply(len) > 2]

# initialize df_final
df_final = pd.DataFrame(columns=['veto1','veto2','veto3','veto4','veto5','veto6','veto7'])

for index, row in df_filtered.iterrows():
    # Remove the enclosing square brackets and split by comma
    # removes cases with 8 or more vetos
    if '8. ' not in row['veto_data']:
        split_vetos = row['veto_data'][1:-1].split(', ')
        # assigns each of the vetos a variable
        m1,m2,m3,m4,m5,m6,m7 = split_vetos
        # data frame formatting
        df_temp = {'veto1': m1, 'veto2': m2, 'veto3': m3, 'veto4': m4, 'veto5': m5, 'veto6': m6, 'veto7': m7}
        df_final = df_final._append(df_temp, ignore_index = True)

# Write the filtered DataFrame to a new CSV file
df_final.to_csv('mod_DeathByGamers.csv', index=False)