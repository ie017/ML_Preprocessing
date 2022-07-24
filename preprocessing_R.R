#@author: ie017

# Data preprocessing
# Importing the dataset
dataset = read.csv('C:/Users/ie/Myenvpy/ML_Missing_Data/Data.csv')

# Taking care of missing data
dataset$Age = ifelse(is.na(dataset$Age), ave(dataset$Age, FUN = function(x)
  mean(x,na.rm = TRUE)), dataset$Age)
# Applique FUN à chaque sous-ensemble de x définis par des facteurs
# Fait référence au paramètre logique qui indique à la fonction de 
# supprimer ou non les valeurs NA du calcul

dataset$Salary = ifelse(is.na(dataset$Salary), ave(dataset$Salary, FUN = 
  function(x)  mean(x,na.rm = TRUE)), dataset$Salary)
print(dataset)
