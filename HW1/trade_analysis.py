import numpy as np
import pandas as pd

read_file_data = pd.read_csv('.\\calculated_trade_footprint\\Trade_footprint_2005.csv', header=0).to_numpy()

def find_net_links(read_file_data):
    out_df = np.array(('Donor', 'Recipient', 'Commodity', 'VWT', 'Water Saved'), dtype=object).reshape(1, -1)

    for i in range(len(read_file_data)):
        # print(out_df)
        idx_trade = np.argwhere(np.logical_and(np.logical_and(out_df[:, 0] == read_file_data[i, 1],
                                                              out_df[:, 1] == read_file_data[i, 2]),
                                                              out_df[:, 2] == read_file_data[i, 3])).reshape(-1)
        if(len(idx_trade)==0):
            temp_array = read_file_data[i, 1:4].reshape(1, -1)
            temp_array = np.hstack((temp_array, read_file_data[i, -2:].reshape(1, -1)))
            out_df = np.vstack((out_df, temp_array.reshape(1, -1)))
        else:
            out_df[idx_trade, -2] = np.nansum([out_df[idx_trade,-2], read_file_data[i, -2]])
            out_df[idx_trade, -1] = np.nansum([out_df[idx_trade,-1], read_file_data[i, -1]])
    
    pd.DataFrame(out_df).to_csv('.\\calculated_trade_footprint\\Link_commodity_analysis.csv', header=None, index=None)

def find_countrywise_export(read_file_data):
    out_df = np.array(('Donor','VWT'), dtype=object).reshape(1, -1)

    for i in range(len(read_file_data)):
        # print(out_df)
        idx_trade = np.argwhere(out_df[:, 0] == read_file_data[i, 1]).reshape(-1)
        if(len(idx_trade)==0):
            temp_array = np.array(['country', 0.0], dtype=object)
            temp_array[0] = read_file_data[i, 1]
            temp_array[1] = read_file_data[i, -2]
            out_df = np.vstack((out_df, temp_array.reshape(1, -1)))
        else:
            try:    
                out_df[idx_trade, -1] = np.nansum([out_df[idx_trade,-1], read_file_data[i, -2]])
            except:
                if(out_df[idx_trade, -1] == 'nan'):
                    out_df[idx_trade, -1] = read_file_data[i, -2]

    percent_column = np.copy(out_df[:, -1])
    percent_column[1:] = out_df[1:, -1]*100/np.nansum(out_df[1:, -1])

    out_df = np.hstack((out_df, percent_column.reshape(-1, 1)))

    pd.DataFrame(out_df).to_csv('.\\calculated_trade_footprint\\Donors_VWT.csv', header=None, index=None)

def find_countrywise_import(read_file_data):
    out_df = np.array(('Recipient','VWT'), dtype=object).reshape(1, -1)

    for i in range(len(read_file_data)):
        # print(out_df)
        idx_trade = np.argwhere(out_df[:, 0] == read_file_data[i, 2]).reshape(-1)
        if(len(idx_trade)==0):
            temp_array = np.array(['country', 0.0], dtype=object)
            temp_array[0] = read_file_data[i, 2]
            temp_array[1] = read_file_data[i, -2]
            out_df = np.vstack((out_df, temp_array.reshape(1, -1)))
        else:
            try:    
                out_df[idx_trade, -1] = np.nansum([out_df[idx_trade,-1], read_file_data[i, -2]])
            except:
                if(out_df[idx_trade, -1] == 'nan'):
                    out_df[idx_trade, -1] = read_file_data[i, -2]

    percent_column = np.copy(out_df[:, -1])
    percent_column[1:] = out_df[1:, -1]*100/np.nansum(out_df[1:, -1])

    out_df = np.hstack((out_df, percent_column.reshape(-1, 1)))

    pd.DataFrame(out_df).to_csv('.\\calculated_trade_footprint\\Recipient_VWT.csv', header=None, index=None)

find_net_links(read_file_data)
find_countrywise_export(read_file_data)
find_countrywise_import(read_file_data)