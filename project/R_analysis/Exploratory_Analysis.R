rm(list=ls())
Df <- read.csv('df_cluster_unscaled_noco.csv')
Clust_0_Df <-Df[which(Df$cluster==0),]
Clust_1_Df <-Df[which(Df$cluster==1),]
Clust_2_Df <-Df[which(Df$cluster==2),]
Clust_3_Df <-Df[which(Df$cluster==3),]
Clust_4_Df <-Df[which(Df$cluster==4),]
Clust_5_Df <-Df[which(Df$cluster==5),]
Clust_6_Df <-Df[which(Df$cluster==6),]
Clust_7_Df <-Df[which(Df$cluster==7),]
Features <-c("1980 Population","Population Change","1980 Per capita Income","Per capita Income change",
             "Avg. Livestock numbers","Avg. Irrg. Agri.","Mean Annual Temperature","Temperature seasonality",
             "Mean Annual Rainfall","Rainfall Seasonality")

#Plotting
png(filename="Unclustered_boxplots.png",width=750,height=1000)
par(mfrow = c(4,3))
TempDf = Df
for (j in 3:12){
  boxplot(TempDf[,j],ylab=Features[j-2],cex.axis=1.6,cex.lab=1.6,ylim=c(min(Df[,j]),max(Df[,j])))
}
dev.off()

png(filename="Clust_0_boxplots.png",width=750,height=1000)
par(mfrow = c(4,3))
TempDf = Clust_0_Df
for (j in 3:12){
  boxplot(TempDf[,j],ylab=Features[j-2],cex.axis=1.6,cex.lab=1.6,ylim=c(min(Df[,j]),max(Df[,j])))
}
dev.off()

png(filename="Clust_1_boxplots.png",width=750,height=1000)
par(mfrow = c(4,3))
TempDf = Clust_1_Df
for (j in 3:12){
  boxplot(TempDf[,j],ylab=Features[j-2],cex.axis=1.6,cex.lab=1.6,ylim=c(min(Df[,j]),max(Df[,j])))
}
dev.off()

png(filename="Clust_2_boxplots.png",width=750,height=1000)
par(mfrow = c(4,3))
TempDf = Clust_2_Df
for (j in 3:12){
  boxplot(TempDf[,j],ylab=Features[j-2],cex.axis=1.6,cex.lab=1.6,ylim=c(min(Df[,j]),max(Df[,j])))
}
dev.off()

png(filename="Clust_3_boxplots.png",width=750,height=1000)
par(mfrow = c(4,3))
TempDf = Clust_3_Df
for (j in 3:12){
  boxplot(TempDf[,j],ylab=Features[j-2],cex.axis=1.6,cex.lab=1.6,ylim=c(min(Df[,j]),max(Df[,j])))
}
dev.off()

png(filename="Clust_4_boxplots.png",width=750,height=1000)
par(mfrow = c(4,3))
TempDf = Clust_4_Df
for (j in 3:12){
  boxplot(TempDf[,j],ylab=Features[j-2],cex.axis=1.6,cex.lab=1.6,ylim=c(min(Df[,j]),max(Df[,j])))
}
dev.off()

png(filename="Clust_5_boxplots.png",width=750,height=1000)
par(mfrow = c(4,3))
TempDf = Clust_5_Df
for (j in 3:12){
  boxplot(TempDf[,j],ylab=Features[j-2],cex.axis=1.6,cex.lab=1.6,ylim=c(min(Df[,j]),max(Df[,j])))
}
dev.off()

png(filename="Clust_6_boxplots.png",width=750,height=1000)
par(mfrow = c(4,3))
TempDf = Clust_6_Df
for (j in 3:12){
  boxplot(TempDf[,j],ylab=Features[j-2],cex.axis=1.6,cex.lab=1.6,ylim=c(min(Df[,j]),max(Df[,j])))
}
dev.off()

png(filename="Clust_7_boxplots.png",width=750,height=1000)
par(mfrow = c(4,3))
TempDf = Clust_7_Df
for (j in 3:12){
  boxplot(TempDf[,j],ylab=Features[j-2],cex.axis=1.6,cex.lab=1.6,ylim=c(min(Df[,j]),max(Df[,j])))
}
dev.off()

# After removing values exceeding 1.5.IQR
for(j in 3:12){
  Up_lim = as.numeric(quantile(Df[,j],0.75)+1.5*IQR(Df[,j]))
  Down_lim = as.numeric(quantile(Df[,j],0.25)-1.5*IQR(Df[,j]))
  Df[which(Df[,j]>Up_lim),j]=NA
  Df[which(Df[,j]<Down_lim),j]=NA
}
Cleaned_Df = na.omit(Df)
Clust_0_Cleaned_Df <-Cleaned_Df[which(Cleaned_Df$cluster==0),]
Clust_1_Cleaned_Df <-Cleaned_Df[which(Cleaned_Df$cluster==1),]
Clust_2_Cleaned_Df <-Cleaned_Df[which(Cleaned_Df$cluster==2),]
Clust_3_Cleaned_Df <-Cleaned_Df[which(Cleaned_Df$cluster==3),]
Clust_4_Cleaned_Df <-Cleaned_Df[which(Cleaned_Df$cluster==4),]
Clust_5_Cleaned_Df <-Cleaned_Df[which(Cleaned_Df$cluster==5),]
Clust_6_Cleaned_Df <-Cleaned_Df[which(Cleaned_Df$cluster==6),]
Clust_7_Cleaned_Df <-Cleaned_Df[which(Cleaned_Df$cluster==7),]

#Plotting
png(filename="Unclustered_Cleaned_boxplots.png",width=750,height=1000)
par(mfrow = c(4,3))
TempDf = Cleaned_Df
for (j in 3:12){
  boxplot(TempDf[,j],ylab=Features[j-2],cex.axis=1.6,cex.lab=1.6,ylim=c(min(Cleaned_Df[,j]),max(Cleaned_Df[,j])))
}
dev.off()

png(filename="Clust_0_Cleaned_boxplots.png",width=750,height=1000)
par(mfrow = c(4,3))
TempDf = Clust_0_Cleaned_Df
for (j in 3:12){
  boxplot(TempDf[,j],ylab=Features[j-2],cex.axis=1.6,cex.lab=1.6,ylim=c(min(Cleaned_Df[,j]),max(Cleaned_Df[,j])))
}
dev.off()

png(filename="Clust_1_Cleaned_boxplots.png",width=750,height=1000)
par(mfrow = c(4,3))
TempDf = Clust_1_Cleaned_Df
for (j in 3:12){
  boxplot(TempDf[,j],ylab=Features[j-2],cex.axis=1.6,cex.lab=1.6,ylim=c(min(Cleaned_Df[,j]),max(Cleaned_Df[,j])))
}
dev.off()

png(filename="Clust_2_Cleaned_boxplots.png",width=750,height=1000)
par(mfrow = c(4,3))
TempDf = Clust_2_Cleaned_Df
for (j in 3:12){
  boxplot(TempDf[,j],ylab=Features[j-2],cex.axis=1.6,cex.lab=1.6,ylim=c(min(Cleaned_Df[,j]),max(Cleaned_Df[,j])))
}
dev.off()

png(filename="Clust_3_Cleaned_boxplots.png",width=750,height=1000)
par(mfrow = c(4,3))
TempDf = Clust_3_Cleaned_Df
for (j in 3:12){
  boxplot(TempDf[,j],ylab=Features[j-2],cex.axis=1.6,cex.lab=1.6,ylim=c(min(Cleaned_Df[,j]),max(Cleaned_Df[,j])))
}
dev.off()

png(filename="Clust_4_Cleaned_boxplots.png",width=750,height=1000)
par(mfrow = c(4,3))
TempDf = Clust_4_Cleaned_Df
for (j in 3:12){
  boxplot(TempDf[,j],ylab=Features[j-2],cex.axis=1.6,cex.lab=1.6,ylim=c(min(Cleaned_Df[,j]),max(Cleaned_Df[,j])))
}
dev.off()

png(filename="Clust_5_Cleaned_boxplots.png",width=750,height=1000)
par(mfrow = c(4,3))
TempDf = Clust_5_Cleaned_Df
for (j in 3:12){
  boxplot(TempDf[,j],ylab=Features[j-2],cex.axis=1.6,cex.lab=1.6,ylim=c(min(Cleaned_Df[,j]),max(Cleaned_Df[,j])))
}
dev.off()

png(filename="Clust_6_Cleaned_boxplots.png",width=750,height=1000)
par(mfrow = c(4,3))
TempDf = Clust_6_Cleaned_Df
for (j in 3:12){
  boxplot(TempDf[,j],ylab=Features[j-2],cex.axis=1.6,cex.lab=1.6,ylim=c(min(Cleaned_Df[,j]),max(Cleaned_Df[,j])))
}
dev.off()

png(filename="Clust_7_Cleaned_boxplots.png",width=750,height=1000)
par(mfrow = c(4,3))
TempDf = Clust_7_Cleaned_Df
for (j in 3:12){
  boxplot(TempDf[,j],ylab=Features[j-2],cex.axis=1.6,cex.lab=1.6,ylim=c(min(Cleaned_Df[,j]),max(Cleaned_Df[,j])))
}
dev.off()