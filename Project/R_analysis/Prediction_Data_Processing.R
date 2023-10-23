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

Yearly_Pop      = array(data=NA,dim=c(dim(clusters)[1],22))
Yearly_Income   = array(data=NA,dim=c(dim(clusters)[1],22))
Yearly_Ag       = array(data=NA,dim=c(dim(clusters)[1],22))
Yearly_Liv      = array(data=NA,dim=c(dim(clusters)[1],22))
Yearly_Pcp      = array(data=NA,dim=c(dim(clusters)[1],22))
Yearly_Tavg     = array(data=NA,dim=c(dim(clusters)[1],22))
Yearly_Clusters = array(data=NA,dim=c(dim(clusters)[1],22))

#For population
Yearly_Pop[,1] = clusters$Geo_FIPS
for(i in 1:dim(clusters)[1]){
  
}