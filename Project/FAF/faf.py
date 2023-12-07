import pandas as pd

df_faf = pd.read_csv("county_FIPS_FAF_zone.csv")
df_ag = pd.read_csv("df_ag.csv")
df_ag = df_ag.drop(df_ag.columns[0], axis=1)

df_faf['ANSI_ST_CO'] = df_faf['ANSI_ST_CO'].astype(float)
df_faf['CFS07DDGEO'] = df_faf['CFS07DDGEO'].astype(str).str.zfill(3)
county_fips_to_cfs07ddgeo = dict(zip(df_faf['ANSI_ST_CO'], df_faf['CFS07DDGEO']))

# Add a new column 'CFS07DDGEO' to the first dataframe based on the mapping
df_ag['CFS07DDGEO'] = df_ag['Geo_FIPS'].map(county_fips_to_cfs07ddgeo)

# county 46102 is not in the faf data

# convert to 5 digits geo fips
df_ag['Geo_FIPS'] = df_ag['Geo_FIPS'].astype(float).astype(int).astype(str).str.zfill(5)

# Save the new dataframe to a csv file
df_ag.to_csv("df_ag_faf.csv", index=False)