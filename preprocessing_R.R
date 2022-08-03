#@author: ie017

# Data preprocessing
# Importing the dataset
dataset = read.csv('C:/Users/ie/Myenvpy/ML_Preprocessing_Data/Data.csv')

# Taking care of missing data
dataset$Age = ifelse(is.na(dataset$Age), ave(dataset$Age, FUN = function(x)
  mean(x,na.rm = TRUE)), dataset$Age)
# Applique FUN à chaque sous-ensemble de x définis par des facteurs
# Fait référence au paramètre logique qui indique à la fonction de 
# supprimer ou non les valeurs NA du calcul

dataset$Salary = ifelse(is.na(dataset$Salary), ave(dataset$Salary, FUN = 
  function(x)  mean(x,na.rm = TRUE)), dataset$Salary)
print(dataset)

# Encode categorical data
dataset$Country = factor(dataset$Country,
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1,2,3))
dataset$Purchased = factor(dataset$Purchased,
                         levels = c('No','Yes'),
                         labels = c(0,1))

#Splitting the dataset into training dataset and testing dataset
#install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

#Feature scalling 
training_set[, 2:3] = scale(training_set[, 2:3])
testing_set[, 2:3] = scale(testing_set[, 2:3])