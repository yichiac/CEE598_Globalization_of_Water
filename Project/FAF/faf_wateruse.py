import pandas as pd

df_faf = pd.read_csv("../FAF/county_FIPS_FAF_zone.csv")

year = 2015
filename = 'Total_Withdrawal_' + str(year) + '.csv'
df_water = pd.read_csv(filename)

df_faf['ANSI_ST_CO'] = df_faf['ANSI_ST_CO'].astype(float)
df_faf['CFS07DDGEO'] = df_faf['CFS07DDGEO'].astype(str).str.zfill(3)
county_fips_to_cfs07ddgeo = dict(zip(df_faf['ANSI_ST_CO'], df_faf['CFS07DDGEO']))

# Add a new column 'FAF' to the first dataframe based on the mapping
df_water['FAF'] = df_water['FIPS'].map(county_fips_to_cfs07ddgeo)

# convert to 5 digits geo fips
df_water['FIPS'] = df_water['FIPS'].astype(float).astype(int).astype(str).str.zfill(5)

# Save the new dataframe to a csv file
df_water.to_csv('Total_Withdrawal_' + str(year) + '_faf.csv', index=False)