# Social, economic, and environmental factors influencing the basic reproduction number of COVID-19 across countries

### Jude Dzevela Kong, Edward Tekwa, Sarah Gignoux-Wolfsohn

To reference the data or methods here, please cite the manuscript. Contact Jude Kong with questions at jdkong@yorku.ca.

## Overview

This repository contains:

* A Python script that uses non-linear least squares to fit  a logistic model  to reported COVID-19 daily case numbers across countries. The aim is to 
estimate the intrinsic growth rate and theoretical epidemic size without intervention. 

* An R script to perfom a fixed effect and a mixed effect generalized additive model (GAM) regression analysis. 
The aim is  to study the association between pre-existing country characteristics and COVID-19 Basic reproduction number.

The repository is organized as follows:

* *Data* contains  two .csv file: variables.csv and COVID_cases.csv.  
    * *variables.csv*  contains data on predictors for each of the countries studied from seven categories (demographics, disease, economics, environmental, habitat, health, and social) 
    from publicly available databases (cited in Table 1 of the manuscript). For each predictor, we used the most recent available data, which ranged from 2000-2019.
    When appropriate, data reported in absolute numbers were divided by total population to obtain per capita figures. 
    Data with highly skewed distributions were log-transformed and all distributions were centred and standardized before regression.
    It also contain  the estimated growth rates, and the basic reproduction numbers for each country.   
    
    * *COVID_cases.csv* contain  COVID-19 daily cases.

* *scripts* contains all code to analyze or transform data. In particular: 

     * *exponential_growth.py*:  A Python script that uses non-linear least squares to fit  a logistic model  to reported COVID-19 daily case numbers across countries. The aim is to 
estimate the intrinsic growth rate and theoretical epidemic size without intervention. 

     * *GAM.r*: An R script to perfom a fixed effect and a mixed effect generalized additive model (GAM) regression analysis. 
The aim is  to study the association between pre-existing country characteristics and COVID-19 Basic reproduction number.

## Instructions

Scripts should be run in the following order:

1) *exponential_growth.py*: import COVID_cases.csv and use the data set to estimate the initial growth rate of COVID-19 for each country. In addition, it plots a  graph of  daily cases averaged over a 7-day window, and the fitted curve

2) *GAM.r*: import variable.csv and used it to perform a fixed effect and a mixed effect generalized additive model (GAM) regression analysis. It also plot the graph the association between the covariates and the response variable (basic reproduction number)


## Computational requirements

Analyses were conducted in RStudio 1.2.5033 on a MacBook Pro (16-inch, 2019)  with the following specifications: Processor 2.6 GHz 6-Core Intel Core i7, 
Memory 16 GB 2667 MHz DDR4, Startup Disk Macintosh HD, Graphics Intel UHD Graphics 630 1536 MB.


## Use, problems, and feedback

If you encounter any errors or problems, please create an Issue here. Likewise, please consider starting an Issue for any questions so that others can view conversations about the analysis and code. Again, don't hesitate to contact us at jdkong@yorku.ca

