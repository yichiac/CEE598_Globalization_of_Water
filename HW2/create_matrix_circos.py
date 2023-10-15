# The output of this script is a matrix of trade flux between countries
# The matrix can be visualized as circos plot through http://mkweb.bcgsc.ca/tableviewer/visualize/

import pandas as pd
import numpy as np

# read data
df = pd.read_csv('AWF_agg.csv')
df.dropna(inplace=True)

# aggregate actual water footprint with same paris of countries
df_group = df.groupby(['country_export', 'country_import']).agg('sum').reset_index()

# drop trade flux under the threshold to get clear a chord plot
awf = df['Actual_WF_(m3)']
awf = awf.to_numpy()
threshold = np.quantile(awf, 0.90)
df_group = df_group[df_group['Actual_WF_(m3)'] > threshold]

# get the list of countries meeting trade flux threshold
exporters = df_group['country_export'].unique()
importers = df_group['country_import'].unique()

# create trade flux matrix
matrix = pd.DataFrame(0, index=exporters, columns=importers)

for index, row in df_group.iterrows():
    export_country = row['country_export']
    import_country = row['country_import']
    value = int(row['Actual_WF_(m3)'])
    matrix.at[export_country, import_country] = value

# sorting the matrix: exporter total AWF in descending order
tawf = matrix.sum(axis=1)
tawf.sort_values(ascending=False, inplace=True)
matrix = matrix.reindex(index=tawf.index)

# export matrix
matrix.to_csv('circos_matrix.txt', sep ='\t', index_label='data')
