rm(list=ls())
library(igraph)
library(network)
library(qgraph)
Data=read.csv("./AWF_agg.csv")

#No of nodes: is the number of unique countries participating in trade
Nodes = unique(c(unique(Data$country_export),unique(Data$country_import)))
NoOfNodes = length(Nodes)
#Strength (Volume of water going in or coming out of a node)
Strength_In  = 0; Strength_Out = 0; Strength_Tot = 0
#Analysing for each node using a for loop
for(i in 1:NoOfNodes){
  #Extracting a subset of the main data containing countries 
  #receiving virtual water from the selected node
  Subset_Out = Data[which(Data$country_export==Nodes[i]),]
  #Extracting a subset of the main data containing countries 
  #sending virtual water to the selected node
  Subset_In  = Data[which(Data$country_import==Nodes[i]),]
  #Summing over the volume of virtual water received by a node
  Strength_In[i] = sum(Subset_In$Actual.WF..m3.)
  #Summing over the volume of virtual water sent by a node
  Strength_Out[i] = sum(Subset_Out$Actual.WF..m3.)
  #Total strength is the summation of received and sent virtual water
  Strength_Tot[i] = Strength_In[i] + Strength_Out[i]
}
OutputMatrix = data.frame(Country = Nodes,Strength_In,Strength_Out,Strength_Tot)
#Converting the data of trades into a graph
#The output is a list with 113 elements (I.e., one element for each node)
#The value in the list is the nodes that that node is connected to
Data_Graph = graph.data.frame(Data[,c(2:4)])
#Getting the betweeness centrality for each node
Centrality = betweenness(Data_Graph,directed = F)

#Plotting betweeness against total strength 
For_Regression = data.frame(y=log(Strength_Tot),x=log(Centrality))
For_Regression$y[which(For_Regression$y==-Inf)] = NA
For_Regression$x[which(For_Regression$x==-Inf)] = NA
For_Regression = na.omit(For_Regression)
#Showing normality of variables
qqnorm(For_Regression$y)
qqline(For_Regression$y)
qqnorm(For_Regression$x)
qqline(For_Regression$x)
#Plotting scatterplot
plot(For_Regression$x,For_Regression$y,xlab="log(Betweenness)",ylab="log(Strength)",pch=16)
#Creating a regression between log(Centrality) and log(Strength_tot)
model <- lm(y ~ x, data = For_Regression)
#Adding regression line to scatterplot
abline(model,col="steelblue",lwd=2)
#Checking if the OLS regression is statistically significant
summary(model)