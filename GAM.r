#Packages
library(lme4)
library(plyr)
library(car)
library(MuMIn)
library(optimx)
library(MCMCglmm)
library(lmerTest)
library(AICcmodavg)
library(leaps)
library(mgcv)
library(gamm4)
library(dplyr)
library(visreg)
library(plyr)
library(ggplot2)

covid.test<-read.csv(file.choose(), header=T)

#######################################################
#FIRST STEP IS SCALE ALL THE VARIABLES

number.var<-names(which(sapply(covid.test, class) == "integer" | sapply(covid.test, class) == "numeric"))
covid.data.scale<-covid.test[,number.var]

#apply scale function to num and int
covid.data.scale<-as.data.frame(apply(covid.data.scale,2,scale))
#add random variables as well as dependent variable
ovid.data.scale$Available_data_bin<-covid.test$Available_data_bin
covid.data.scale$Total_Population_bin<-covid.test$Total_Population_bin
covid.data.scale$GDP_bin<-covid.test$GDP_bin
covid.data.scale$Under_reproted_bin<-covid.test$Under_reproted_bin
covid.data.scale$Days_to_30_case_bin<-covid.test$Days_to_30_case_bin
covid.data.scale$R0<-covid.test$R0
covid.data.scale$country<-covid.test$country
covid.data.scale$Region<-covid.test$Region
###### ######Potential model fixed effect model
#GAM fixed effects model
modfin_fixed<-gam(R0~s(Youth, bs = 'cr', k = 3)+s(Total_Pop, bs = 'cr', k = 3)+s(City, bs = 'cr', k = 3)+
s(Urbanization, bs = 'cr', k = 3)+s(Air_Transport, bs = 'cr', k = 3)+s(Temperature, bs = 'cr', k = 3)+s(Precipitation, bs = 'cr', k = 3)+s(GHS, bs = 'cr', k = 3)+s(Mort_Resp, bs = 'cr', k = 3)+s(Mort_Infect, bs = 'cr', k = 3)+s(Nurses, bs = 'cr', k = 3)+
s(Social_Media, bs = 'cr', k = 3)+s(Internet_Filtering, bs = 'cr', k = 3)+s(GINI, bs = 'cr', k = 3)+s(Pollution, bs = 'cr', k = 3)+s(Business, bs = 'cr', k = 3), data= covid.data.scale)
ar(font.axis=18, cex.axis=4)
visreg(modfin_fixed, gg=TRUE,  ylab="Basic reproduction number", cex.lab=18, points=list(size=5, pch=16))
plotdata <- visreg(modfin_fixed, type = "contrast", plot = FALSE)
plot(modfin_fixed,residuals=TRUE, pers=TRUE,shade.col="gray")
#mixed effects model
modfin_mixed<-gam(R0~s(Pop_bw20_34, bs = 'cr', k = 3)+s(logPop_tot, bs = 'cr', k = 3)+s(Pop_Urban, bs = 'cr', k = 3)+
                s(Urban_pop, bs = 'cr', k = 3)+s(log_Air_trans, bs = 'cr', k = 3)+s(Temp, bs = 'cr', k = 3)+s(logPercip, bs = 'cr', k = 3)+s(GHS, bs = 'cr', k = 3)+s(logMort_resp, bs = 'cr', k = 3)+s(logMort_infect , bs = 'cr', k = 3)+s(logNurses, bs = 'cr', k = 3)+
                s(Social_media, bs = 'cr', k = 3)+s(logInternet_filtering, bs = 'cr', k = 3)+s(GINI_index, bs = 'cr', k = 3)+s(logPollution, bs = 'cr', k = 3)+s(Business, bs = 'cr', k = 3)+s(region_sim,bs='re')+s(days_30cases_bin,bs='re')+s(Per_reported_bin,bs='re')+s(Log10GDP_bin,bs='re')+s(days_timeseries_bin,bs='re'), data= covid.data.scale)
summary(modfin_mixed)

plot(modfin_mixed,residuals=TRUE,shade=TRUE,shade.col="gray")
