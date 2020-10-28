getwd()
setwd("C:/Users/eanna/OneDrive/Desktop/Data Analytics/Projects/Cleaning Data in R")
library(readxl) # load package to read excel file
brooklyn <- read_excel("rollingsales_brooklyn.xls", skip = 4) # save dataframe of brooklyn borough sales beginning from row 5 of excel file

library(tidyverse)# load package
glimpse(brooklyn)# provide glimpse of dataframe

mean(brooklyn$`SALE PRICE`) #show mean sales price

brooklyn_csv <- read.csv("rollingsales_brooklyn_.csv", skip = 4) # compare dataframe of csv file
glimpse(brooklyn_csv) #provide glimpse of dataframe


brooklyn <- read_excel("rollingsales_brooklyn.xls", skip = 4)
bronx <- read_excel("rollingsales_bronx.xls", skip = 4)
staten_island <- read_excel("rollingsales_statenisland.xls", skip = 4)
queens <- read_excel("rollingsales_queens.xls", skip = 4) #load 4 dataframes

# Bind all dataframes into one, save as "NYC_property_sales"
NYC_property_sales <-bind_rows(mutate_all(brooklyn, as.character), mutate_all(bronx, as.character), mutate_all(staten_island, as.character), mutate_all(queens, as.character))
glimpse(NYC_property_sales)

library(magrittr) # load package
colnames(NYC_property_sales) %<>% str_replace_all("\\s", "_") %<>% tolower() # take column names of NYC dataframe, and then update all column names to replace all spaces with underscores, and then update all column names to lower case
colnames(NYC_property_sales)

NYC_property_sales %>% glimpse() # Take dataframe, and then, glimpse



