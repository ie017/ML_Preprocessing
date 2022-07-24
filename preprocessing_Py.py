
#@author: ie017
 
# Data preprocessing
#Importing the libraries
 
from re import X
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer #sklearn is amazing librarie to make ML models
#from sklearn we have preprocessing library that contains a lot of classes methodes to preprocess any data set
# finaly we have Imputer class willallow us to take care of those missing data

#importing the data set
dataset = pd.read_csv(r"C:\Users\ie\Myenvpy\ML_Missing_Data\Data.csv")
X = dataset.iloc[:, :-1].values # Select the values of the specify matrix X from dataset
Y = dataset.iloc[:, 3].values # Select the values of the specify Matrix y from dataset

#Make object of Imputer class
imputer = SimpleImputer(missing_values= np.nan, strategy= 'mean', verbose=0)
#strategy specify the method how we correct the missing value par default mean
#verbose specify what we should take culmns or rows to apply the strategy

#fit the strategy with the culmns 1 and 2
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
#here fit method will calculate the required parameters (In this case mean)
#and store it in the impute object

#imputer.transform will actually do the work of replacement of nan with mean.
#This can be done in one step using fit_transform
print(X)

