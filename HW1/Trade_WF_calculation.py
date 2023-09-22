import pandas as pd
import numpy as np
import os
import pickle as pkl
import matplotlib.pyplot as plt

def read_WF_dataset(file_name, is_agri_data = 0):   ##### Reading and saving data to numpy arrays
    df_read = pd.read_excel(file_name, header=None, sheet_name=1)

    if(is_agri_data == 1):
        data_arr = df_read.iloc[6:, :].to_numpy()
        country_row = df_read.iloc[3, :].to_numpy()
        label_row = df_read.iloc[4, :].to_numpy()
    else:
        data_arr = df_read.iloc[4:, :].to_numpy()
        country_row = df_read.iloc[2, :].to_numpy()
        label_row = df_read.iloc[3, :].to_numpy()


    return data_arr, country_row, label_row

def find_WF(product, country_export, country_import, data_arr, country_row, product_type):
    if(product in list(data_arr[:, 3]) or product in list(data_arr[:, 2])): ##### Check if the product esists in the description
        product_found = 1   ############ product_type=1: Agri products, product_type=0: Animal products
        if(product_type == 1):    
            product_idx = np.argwhere(data_arr[:, 3]==product).reshape(-1)[0]   ### Matching the description with the dictionary term
        else:
            product_idx = np.argwhere(data_arr[:, 2]==product).reshape(-1)[0]
        
        ### Exporters Footprint
        country_export_idx = np.argwhere(country_row==country_export).reshape(-1)[-1] ### Last Column is country average
        
        if(product_type==1): #### Crops and Agri    
            WF_export = np.nansum([data_arr[product_idx, country_export_idx],data_arr[product_idx+1, country_export_idx]]) ### Adding green and blue
        else:
            WF_export = data_arr[product_idx, country_export_idx+3] ### Taking Weighted avg
        
        ### Importers Footprint
        if(product_type==0 and country_import == "Occupied Palestinian Territory"):
            country_import_temp = "Israel"
            country_import_idx = np.argwhere(country_row==country_import_temp).reshape(-1)[-1] ### Last Column is country average
        else:
            country_import_idx = np.argwhere(country_row==country_import).reshape(-1)[-1] ### Last Column is country average

        if(product_type==1): #### Crops and Agri    
            WF_import = data_arr[product_idx, country_import_idx]+data_arr[product_idx+1, country_import_idx] ### Adding green and blue
        else:
            WF_import = data_arr[product_idx, country_import_idx+3] ### Taking Weighted 

    else:
        product_found = 0
        WF_export, WF_import = 0, 0
    return product_found, WF_export, WF_import

def append_EU_data(data_arr, product_type, country_row, EU_countries): ########## Appending EU average data to the datasets
    
    column_arr = np.full((len(data_arr[:, 0]), len(EU_countries)), np.nan)
    
    for i in range(len(EU_countries)):
        nation_idx = np.argwhere(country_row == EU_countries[i]).reshape(-1)[-1]
        if(product_type == 1):
            column_arr[:, i] = np.copy(data_arr[:, nation_idx])
        else:
            column_arr[:, i] = np.copy(data_arr[:, nation_idx+3])

    if(product_type==1):    ############ product_type=1: Agri products, product_type=0: Animal products
        data_arr = np.hstack((data_arr, np.nanmean(column_arr, axis = 1).reshape(-1, 1)))
    else:
        data_arr = np.hstack((data_arr, np.nanmean(column_arr, axis = 1).reshape(-1, 1)*np.ones((len(data_arr[:, 0]), 4))))
    country_row = np.hstack((country_row, np.array(['European Community'], dtype=object)))

    return data_arr, country_row

def pie_chart(sizes, legends, save_file_name, save_loc = '.\\'): ### To plot the product-wise pie-chart
    
    temp_arr = np.hstack((sizes.reshape(-1, 1), legends.reshape(-1, 1)))

    temp_arr = temp_arr[temp_arr[:, 0].argsort()]
    
    # print(np.nansum(temp_arr[:, 0]))

    temp_arr[-6, 1] = 'Others'
    temp_arr[-6, 0] = np.nansum(temp_arr[:-5, 0])
    
    def absolute_value(val):
        a  = np.round((val/100)*np.nansum(temp_arr[-6:, 0]), 2)
        return a
    # print(temp_arr[-6:, :])
    
    plt.figure()
    plt.pie(temp_arr[-6:, 0], labels=temp_arr[-6:, 1], autopct=absolute_value) #autopct='%1.1f%%'
    plt.savefig(save_loc+save_file_name+'.png')
    plt.close()

#####################################################################################

agri_data = '.\\Report47-Appendix\\Report47-Appendix-II\\Report47-Appendix-II.xlsx'
animal_data = '.\\Report48-Appendix-V\\Report48-Appendix-V.xlsx'

trade_yr = [2005] #### Considering 2005 data

trade_file_loc = '.\\WFP-0000018924\\Historical Data Files\\Tonnage & IRMAs IRMA Energy IRMAt Energy FINAL\\'

product_dict = '.\\Dictionary_Products.csv' ### Product Dictionary file

product_dict_data = pd.read_csv(product_dict, header=None).to_numpy()[1:, 1:]

ignore_donors = ['NGOs', 'OTHER', 'WFP', 'PRIVATE', 'UNITED NATIONS'] ## Ignoring these donors

########### Saving the datasets into binary files to speed up the code

save_binary = 0
if(save_binary==1):
    os.makedirs('.\\binary_files\\', exist_ok=True)
    agri_data_arr, agri_country_row, agri_label_row = read_WF_dataset(agri_data, is_agri_data=1)
    animal_data_arr, animal_country_row, animal_label_row = read_WF_dataset(animal_data, is_agri_data=0)

    with open('.\\binary_files\\agri_data_arr.pkl', 'wb') as pkl_file:
        pkl.dump(agri_data_arr, pkl_file)
    with open('.\\binary_files\\agri_country_row.pkl', 'wb') as pkl_file:
        pkl.dump(agri_country_row, pkl_file)
    with open('.\\binary_files\\agri_label_row.pkl', 'wb') as pkl_file:
        pkl.dump(agri_label_row, pkl_file)
    
    with open('.\\binary_files\\animal_data_arr.pkl', 'wb') as pkl_file:
        pkl.dump(animal_data_arr, pkl_file)
    with open('.\\binary_files\\animal_country_row.pkl', 'wb') as pkl_file:
        pkl.dump(animal_country_row, pkl_file)
    with open('.\\binary_files\\animal_label_row.pkl', 'wb') as pkl_file:
        pkl.dump(animal_label_row, pkl_file)

######## Reads the binary file

with open('.\\binary_files\\agri_data_arr.pkl', 'rb') as pkl_file:
    agri_data_arr = pkl.load(pkl_file)
with open('.\\binary_files\\agri_country_row.pkl', 'rb') as pkl_file:
    agri_country_row = pkl.load(pkl_file)
with open('.\\binary_files\\agri_label_row.pkl', 'rb') as pkl_file:
    agri_label_row = pkl.load(pkl_file)

with open('.\\binary_files\\animal_data_arr.pkl', 'rb') as pkl_file:
    animal_data_arr = pkl.load(pkl_file)
with open('.\\binary_files\\animal_country_row.pkl', 'rb') as pkl_file:
    animal_country_row = pkl.load(pkl_file)
with open('.\\binary_files\\animal_label_row.pkl', 'rb') as pkl_file:
    animal_label_row = pkl.load(pkl_file)

########## Taking average for the European Union countries

EU_countries = ['Germany', 'France', 'Italy', 'Netherlands', 'Belgium', 'Luxembourg', 
                'Denmark', 'Ireland', 'United Kingdom', 'Greece', 'Spain', 'Portugal', 
                'Austria', 'Finland', 'Sweden', 'Czech Republic', 'Cyprus', 'Estonia', 'Latvia', 
                'Lithuania', 'Hungary', 'Malta', 'Poland', 'Slovenia', 'Slovakia']

agri_data_arr, agri_country_row = append_EU_data(agri_data_arr, 1, agri_country_row, EU_countries)
animal_data_arr, animal_country_row = append_EU_data(animal_data_arr, 0, animal_country_row, EU_countries)

###############

for i in range(len(trade_yr)):
    trade_data = pd.read_csv(trade_file_loc+str(trade_yr[i])+' Tonnage & IRMAt.csv', header=0).to_numpy()

    write_str = np.array(['year', 'country_export', 'country_import', 'Product', 'Commodity Cereals Non Cereals', 'Tonnage', 
                          'Exporter Footprint (per unit)', 'Importers Footprint (per unit)', 'Water Footprint Traded (m3)', 
                          'Water Saved (m3)'], dtype=object).reshape(1, -1)
    for ii in range(len(trade_data[:, 0])):
        
        if(trade_data[ii, 5] == 'Direct Transfer' and trade_data[ii, 1] not in ignore_donors):
            country_export = trade_data[ii, 1]
            country_import = trade_data[ii, 2]

            print(country_export, country_import)
            
            country_export_temp = country_export.split(',') #### Extracting countries which are named as 'Country_name, the'
            country_import_temp = country_import.split(',') #### Extracting countries which are named as 'Country_name, the'
            try:
                if(country_export_temp[1] == ' the'):
                    country_export = country_export_temp[0]
            except:
                pass
            
            try:
                if(country_import_temp[1] == ' the'):
                    country_import = country_import_temp[0]
            except:
                pass

            ##### Matching the names of the countries across the databases

            if(country_import == "Democratic People's Republic of Korea (DPRK)"):
                country_import = "Korea, Democratic People's Republic of"
            elif(country_import == "Democratic Republic of the Congo (DRC)"):
                country_import = "Congo, Democratic Republic of the"
            elif(country_import == "São Tomé and Principe"):
                country_import = "Sao Tome and Principe"
            elif(country_import == "Central African Republic "):
                country_import = "Central African Republic"
            elif(country_import == "Timor-Leste"):
                country_import = "East Timor"
            elif(country_import == "Republic of Moldova"): #, the
                country_import = "Moldova"
            
            if(country_export == "Lybian Arab Jamahiriya"):
                country_export = "Libyan Arab Jamahiriya"
            elif(country_export=="Taiwan, Province of China"):
                country_export = "China"
            elif(country_export == "Democratic Republic of the Congo (DRC)"):
                country_export = "Congo, Democratic Republic of the"
            elif(country_export == "Republic of Korea"): ## , the
                country_export = "Korea, Republic of"

            ###########################

            tonnage = trade_data[ii, 9]

            cereal_non_cereal = trade_data[ii, 7]

            Product_name = trade_data[ii, 6]

            idx_product = np.argwhere(product_dict_data[:, 0]==Product_name).reshape(-1)[0] ##### Matching the Product names with the Annexes

            ##### Removing nan values from the dictionary
            
            idx_nan = np.argwhere(pd.isna(product_dict_data[idx_product])==True).reshape(-1)
            
            product_idx_temp = np.copy(product_dict_data[idx_product])
            product_idx_temp = np.delete(product_idx_temp, idx_nan)
            
            ###################

            ######### Finding the water footprint of the commodities

            WF_export_temp = []
            WF_import_temp = []
            
            for kk in range(1, len(product_idx_temp)):
                
                product_found, WF_export, WF_import = find_WF(product_idx_temp[kk], country_export, country_import, 
                                                            agri_data_arr, agri_country_row, 1)
                
                if(product_found==0):
                    product_found, WF_export, WF_import = find_WF(product_idx_temp[kk], country_export, country_import, 
                                                            animal_data_arr, animal_country_row, 0)
                WF_export_temp.append(WF_export)
                WF_import_temp.append(WF_import)

            try:
                WF_export = np.nanmedian(WF_export_temp) ### Taking the median to account for skewed data
                WF_import = np.nanmedian(WF_import_temp) ### Taking the median to account for skewed data

                # WF_export = np.nanmean(WF_export_temp) ### mean can also be considered
                # WF_import = np.nanmean(WF_import_temp) ### mean can also be considered
            except:
                product_found, WF_export, WF_import = 0, 0, 0

            ##### Saving data into an array

            write_str = np.vstack((write_str, np.array([trade_yr[i], country_export, country_import, Product_name,
                                                        cereal_non_cereal, tonnage, WF_export, WF_import, WF_export*tonnage,
                                                        (WF_import-WF_export)*tonnage], dtype=object).reshape(1, -1)))

    ######## Outputting array as a csv file
    os.makedirs('.\\calculated_trade_footprint\\', exist_ok = True)
    pd.DataFrame(write_str).to_csv('.\\calculated_trade_footprint\\Trade_footprint_'+str(trade_yr[i])+'.csv', header=None, index=None)

    footprint_data = pd.read_csv('.\\calculated_trade_footprint\\Trade_footprint_'+str(trade_yr[i])+'.csv', header=0).to_numpy()

    #### Creating the product-wise footprint and water savings pie-chart
    unique_products = np.unique(footprint_data[:, 3])

    product_water_footprint = np.full((len(unique_products)), np.nan)
    product_water_savings = np.full((len(unique_products)), np.nan)

    zero_footprints = np.argwhere(np.logical_or(footprint_data[:, -3]==0, footprint_data[:, -4]==0)).reshape(-1)
    nan_footprints = np.argwhere(np.logical_or(pd.isna(footprint_data[:, -3])==True, pd.isna(footprint_data[:, -4])==True)).reshape(-1)

    #### Removing the missing values from the data
    water_saved_data = np.copy(footprint_data[:, -1]).reshape(-1, 1)
    water_saved_data[zero_footprints, :] = np.nan
    water_saved_data[nan_footprints, :] = np.nan

    for iii in range(len(unique_products)):
        idx_unique_product = np.argwhere(footprint_data[:, 3] == unique_products[iii]).reshape(-1)

        product_water_footprint[iii] = np.nansum(footprint_data[idx_unique_product, -2])
        product_water_savings[iii] = np.nansum(water_saved_data[idx_unique_product, 0])
    
    # print(unique_products, product_water_footprint/1e9, product_water_savings/1e9)

    pie_chart(product_water_footprint/1e9, unique_products, 'water_footprint_products', '.\\calculated_trade_footprint\\')
    pie_chart(product_water_savings/1e9, unique_products, 'water_savings_products', '.\\calculated_trade_footprint\\')