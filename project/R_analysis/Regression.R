rm(list=ls())
df_pop    = read.csv("df_pop.csv")
df_income = read.csv("df_income.csv")
df_ag     = read.csv("df_ag.csv")
df_liv    = read.csv("df_liv.csv")
df_water  = read.csv("water_use_yearly.csv")
df_pcp    = read.csv("df_pcp_annual.csv")
df_tavg    = read.csv("df_tavg_annual.csv")
clusters  = read.csv("cluster_analysis_scaled_noco.csv")
#Removing one row from clusters which is not in df_water
clusters[1478,]=NA
clusters=na.omit(clusters)

#Predictors-Predictand 1995-2000
#First finding common GeoFIPS for which we have clusters
Pop_change_95_00    = numeric(dim(clusters)[1])
Income_change_95_00 = numeric(dim(clusters)[1])
Ag_change_95_00     = numeric(dim(clusters)[1])
Livstk_change_95_00 = numeric(dim(clusters)[1])
Avg_Rain_95_00      = numeric(dim(clusters)[1])
Avg_Temp_95_00      = numeric(dim(clusters)[1])
Water_change_95_00  = numeric(dim(clusters)[1])
cluster             = numeric(dim(clusters)[1])
for (i in 1:dim(clusters)[1]){
  Pop_1995         = (df_pop$population_1990[which(df_pop$Geo_FIPS==clusters$Geo_FIPS[i])]+df_pop$population_2000[which(df_pop$Geo_FIPS==clusters$Geo_FIPS[i])])/2
  Pop_2000         = df_pop$population_2000[which(df_pop$Geo_FIPS==clusters$Geo_FIPS[i])]
  Pop_change_95_00[i]    = Pop_2000 - Pop_1995
  Income_1995      = (df_income$income_per_capita_1990[which(df_income$Geo_FIPS==clusters$Geo_FIPS[i])]+df_income$income_per_capita_2000[which(df_income$Geo_FIPS==clusters$Geo_FIPS[i])])/2
  Income_2000      = df_income$income_per_capita_2000[which(df_income$Geo_FIPS==clusters$Geo_FIPS[i])]
  Income_change_95_00[i] = Income_2000 - Income_1995
  Ag_change_95_00[i]     = df_ag$X2002_ag[which(df_ag$Geo_FIPS==clusters$Geo_FIPS[i])]-df_ag$X1997_ag[which(df_ag$Geo_FIPS==clusters$Geo_FIPS[i])]
  Livstk_change_95_00[i] = df_liv$X2000_livestock[which(df_liv$Geo_FIPS==clusters$Geo_FIPS[i])] - df_liv$X1995_livestock[which(df_liv$Geo_FIPS==clusters$Geo_FIPS[i])]
  Avg_Rain_95_00[i] = mean(as.numeric(df_pcp[which(df_pcp$Geo_FIPS==clusters$Geo_FIPS[i]),19:23]))
  Avg_Temp_95_00[i] = mean(as.numeric(df_tavg[which(df_tavg$Geo_FIPS==clusters$Geo_FIPS[i]),19:23]))
  Water_change_95_00[i]  = df_water$TW_2000[which(df_water$Geo_FIPS==clusters$Geo_FIPS[i])] - df_water$TW_1995[which(df_water$Geo_FIPS==clusters$Geo_FIPS[i])]
  cluster[i]       = clusters$cluster[i]
}

#Predictors-Predictand 2000-2005
Pop_change_00_05    = numeric(dim(clusters)[1])
Income_change_00_05 = numeric(dim(clusters)[1])
Ag_change_00_05     = numeric(dim(clusters)[1])
Livstk_change_00_05 = numeric(dim(clusters)[1])
Avg_Rain_00_05      = numeric(dim(clusters)[1])
Avg_Temp_00_05      = numeric(dim(clusters)[1])
Water_change_00_05  = numeric(dim(clusters)[1])
cluster             = numeric(dim(clusters)[1])
for (i in 1:dim(clusters)[1]){
  Pop_2005         = (df_pop$population_2010[which(df_pop$Geo_FIPS==clusters$Geo_FIPS[i])]+df_pop$population_2000[which(df_pop$Geo_FIPS==clusters$Geo_FIPS[i])])/2
  Pop_2000         = df_pop$population_2000[which(df_pop$Geo_FIPS==clusters$Geo_FIPS[i])]
  Pop_change_00_05[i]    = Pop_2005 - Pop_2000
  Income_2005      = (df_income$income_per_capita_2010[which(df_income$Geo_FIPS==clusters$Geo_FIPS[i])]+df_income$income_per_capita_2000[which(df_income$Geo_FIPS==clusters$Geo_FIPS[i])])/2
  Income_2000      = df_income$income_per_capita_2000[which(df_income$Geo_FIPS==clusters$Geo_FIPS[i])]
  Income_change_00_05[i] = Income_2005 - Income_2000
  Ag_change_00_05[i]     = df_ag$X2007_ag[which(df_ag$Geo_FIPS==clusters$Geo_FIPS[i])]-df_ag$X2002_ag[which(df_ag$Geo_FIPS==clusters$Geo_FIPS[i])]
  Livstk_change_00_05[i] = df_liv$X2005_livestock[which(df_liv$Geo_FIPS==clusters$Geo_FIPS[i])] - df_liv$X2000_livestock[which(df_liv$Geo_FIPS==clusters$Geo_FIPS[i])]
  Avg_Rain_00_05[i] = mean(as.numeric(df_pcp[which(df_pcp$Geo_FIPS==clusters$Geo_FIPS[i]),24:28]))
  Avg_Temp_00_05[i] = mean(as.numeric(df_tavg[which(df_tavg$Geo_FIPS==clusters$Geo_FIPS[i]),24:28]))
  Water_change_00_05[i]  = df_water$TW_2005[which(df_water$Geo_FIPS==clusters$Geo_FIPS[i])] - df_water$TW_2000[which(df_water$Geo_FIPS==clusters$Geo_FIPS[i])]
  cluster[i]       = clusters$cluster[i]
}

#Predictors-Predictand 2005-2010
Pop_change_05_10    = numeric(dim(clusters)[1])
Income_change_05_10 = numeric(dim(clusters)[1])
Ag_change_05_10     = numeric(dim(clusters)[1])
Livstk_change_05_10 = numeric(dim(clusters)[1])
Avg_Rain_05_10      = numeric(dim(clusters)[1])
Avg_Temp_05_10      = numeric(dim(clusters)[1])
Water_change_05_10  = numeric(dim(clusters)[1])
cluster             = numeric(dim(clusters)[1])
for (i in 1:dim(clusters)[1]){
  Pop_2005         = (df_pop$population_2010[which(df_pop$Geo_FIPS==clusters$Geo_FIPS[i])]+df_pop$population_2000[which(df_pop$Geo_FIPS==clusters$Geo_FIPS[i])])/2
  Pop_2010         = df_pop$population_2010[which(df_pop$Geo_FIPS==clusters$Geo_FIPS[i])]
  Pop_change_05_10[i]    = Pop_2010 - Pop_2005
  Income_2005      = (df_income$income_per_capita_2010[which(df_income$Geo_FIPS==clusters$Geo_FIPS[i])]+df_income$income_per_capita_2000[which(df_income$Geo_FIPS==clusters$Geo_FIPS[i])])/2
  Income_2010      = df_income$income_per_capita_2010[which(df_income$Geo_FIPS==clusters$Geo_FIPS[i])]
  Income_change_05_10[i] = Income_2010 - Income_2005
  Ag_change_05_10[i]     = df_ag$X2012_ag[which(df_ag$Geo_FIPS==clusters$Geo_FIPS[i])]-df_ag$X2007_ag[which(df_ag$Geo_FIPS==clusters$Geo_FIPS[i])]
  Livstk_change_05_10[i] = df_liv$X2010_livestock[which(df_liv$Geo_FIPS==clusters$Geo_FIPS[i])] - df_liv$X2005_livestock[which(df_liv$Geo_FIPS==clusters$Geo_FIPS[i])]
  Avg_Rain_05_10[i] = mean(as.numeric(df_pcp[which(df_pcp$Geo_FIPS==clusters$Geo_FIPS[i]),29:33]))
  Avg_Temp_05_10[i] = mean(as.numeric(df_tavg[which(df_tavg$Geo_FIPS==clusters$Geo_FIPS[i]),29:33]))
  Water_change_05_10[i]  = df_water$TW_2010[which(df_water$Geo_FIPS==clusters$Geo_FIPS[i])] - df_water$TW_2005[which(df_water$Geo_FIPS==clusters$Geo_FIPS[i])]
  cluster[i]       = clusters$cluster[i]
}

#Predictors-Predictand 2010-2015
Pop_change_10_15    = numeric(dim(clusters)[1])
Income_change_10_15 = numeric(dim(clusters)[1])
Ag_change_10_15     = numeric(dim(clusters)[1])
Livstk_change_10_15 = numeric(dim(clusters)[1])
Avg_Rain_10_15      = numeric(dim(clusters)[1])
Avg_Temp_10_15      = numeric(dim(clusters)[1])
Water_change_10_15  = numeric(dim(clusters)[1])
cluster             = numeric(dim(clusters)[1])
for (i in 1:dim(clusters)[1]){
  Pop_2015         = (df_pop$population_2020[which(df_pop$Geo_FIPS==clusters$Geo_FIPS[i])]+df_pop$population_2010[which(df_pop$Geo_FIPS==clusters$Geo_FIPS[i])])/2
  Pop_2010         = df_pop$population_2010[which(df_pop$Geo_FIPS==clusters$Geo_FIPS[i])]
  Pop_change_10_15[i]    = Pop_2015 - Pop_2010
  Income_2015      = (df_income$income_per_capita_2020[which(df_income$Geo_FIPS==clusters$Geo_FIPS[i])]+df_income$income_per_capita_2010[which(df_income$Geo_FIPS==clusters$Geo_FIPS[i])])/2
  Income_2010      = df_income$income_per_capita_2010[which(df_income$Geo_FIPS==clusters$Geo_FIPS[i])]
  Income_change_10_15[i] = Income_2015 - Income_2010
  Ag_change_10_15[i]     = df_ag$X2017_ag[which(df_ag$Geo_FIPS==clusters$Geo_FIPS[i])]-df_ag$X2012_ag[which(df_ag$Geo_FIPS==clusters$Geo_FIPS[i])]
  Livstk_change_10_15[i] = df_liv$X2015_livestock[which(df_liv$Geo_FIPS==clusters$Geo_FIPS[i])] - df_liv$X2010_livestock[which(df_liv$Geo_FIPS==clusters$Geo_FIPS[i])]
  Avg_Rain_10_15[i] = mean(as.numeric(df_pcp[which(df_pcp$Geo_FIPS==clusters$Geo_FIPS[i]),34:38]))
  Avg_Temp_10_15[i] = mean(as.numeric(df_tavg[which(df_tavg$Geo_FIPS==clusters$Geo_FIPS[i]),34:38]))
  Water_change_10_15[i]  = df_water$TW_2015[which(df_water$Geo_FIPS==clusters$Geo_FIPS[i])] - df_water$TW_2010[which(df_water$Geo_FIPS==clusters$Geo_FIPS[i])]
  cluster[i]       = clusters$cluster[i]
}

# All predictand and predictors
Pop_change_all    = c(Pop_change_95_00,Pop_change_00_05,Pop_change_05_10,Pop_change_10_15)
Income_change_all = c(Income_change_95_00,Income_change_00_05,Income_change_05_10,Income_change_10_15)
Ag_change_all     = c(Ag_change_95_00,Ag_change_00_05,Ag_change_05_10,Ag_change_10_15)
Livstk_change_all = c(Livstk_change_95_00,Livstk_change_00_05,Livstk_change_05_10,Livstk_change_10_15)
Avg_Rain_all      = c(Avg_Rain_95_00,Avg_Rain_00_05,Avg_Rain_05_10,Avg_Rain_10_15)
Avg_Temp_all      = c(Avg_Temp_95_00,Avg_Temp_00_05,Avg_Temp_05_10,Avg_Temp_10_15)
Water_change_all  = c(Water_change_95_00,Water_change_00_05,Water_change_05_10,Water_change_10_15)
cluster_all       = c(cluster,cluster,cluster,cluster)

#Data for regression
All_Regression_Data = cbind.data.frame(Pop_change_all,Income_change_all,Ag_change_all,Livstk_change_all,
                                      Avg_Rain_all,Avg_Temp_all,cluster_all,Water_change_all)
All_Regression_Data = na.omit(All_Regression_Data)
Clust_0_Rgrsn_Data = All_Regression_Data[which(All_Regression_Data$cluster_all==0),]
Clust_1_Rgrsn_Data = All_Regression_Data[which(All_Regression_Data$cluster_all==1),]
Clust_2_Rgrsn_Data = All_Regression_Data[which(All_Regression_Data$cluster_all==2),]
Clust_3_Rgrsn_Data = All_Regression_Data[which(All_Regression_Data$cluster_all==3),]
Clust_4_Rgrsn_Data = All_Regression_Data[which(All_Regression_Data$cluster_all==4),]
Clust_5_Rgrsn_Data = All_Regression_Data[which(All_Regression_Data$cluster_all==5),]
Clust_6_Rgrsn_Data = All_Regression_Data[which(All_Regression_Data$cluster_all==6),]
Clust_7_Rgrsn_Data = All_Regression_Data[which(All_Regression_Data$cluster_all==7),]

#Saving files
write.csv(All_Regression_Data,file="All_Regression_Data.csv")
write.csv(Clust_0_Rgrsn_Data,file="Clust_0_Rgrsn_Data.csv")
write.csv(Clust_1_Rgrsn_Data,file="Clust_1_Rgrsn_Data.csv")
write.csv(Clust_2_Rgrsn_Data,file="Clust_2_Rgrsn_Data.csv")
write.csv(Clust_3_Rgrsn_Data,file="Clust_3_Rgrsn_Data.csv")
write.csv(Clust_4_Rgrsn_Data,file="Clust_4_Rgrsn_Data.csv")
write.csv(Clust_5_Rgrsn_Data,file="Clust_5_Rgrsn_Data.csv")
write.csv(Clust_6_Rgrsn_Data,file="Clust_6_Rgrsn_Data.csv")
write.csv(Clust_7_Rgrsn_Data,file="Clust_7_Rgrsn_Data.csv")