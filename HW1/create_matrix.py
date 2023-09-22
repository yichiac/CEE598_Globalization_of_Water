import pandas as pd
import numpy as np

# read data
df = pd.read_csv('AWF_2005.csv')
df.dropna(inplace=True)

# aggregate actual water footprint with same paris of countries
df_group = df.groupby(['country_export', 'country_import']).agg('sum').reset_index()

# drop trade flux under the threshold to get clear a chord plot
awf = df['Actual WF (m3)']
awf = awf.to_numpy()
threshold = np.quantile(awf, 0.95)
df_group = df_group[df_group['Actual WF (m3)'] > threshold]

# get the list of countries meeting trade flux threshold
exporters = df_group['country_export'].unique()
importers = df_group['country_import'].unique()
all_countries = np.unique(np.concatenate((exporters, importers), axis=0))

# create trade flux matrix
matrix = pd.DataFrame(0, index=all_countries, columns=all_countries)

for index, row in df_group.iterrows():
    export_country = row['country_export']
    import_country = row['country_import']
    value = row['Actual WF (m3)']
    matrix.at[export_country, import_country] = value

matrix.to_csv('output_matrix.csv')