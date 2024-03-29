
#@author: ie017
 
# Data preprocessing
#Importing the libraries
 
from re import X
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
from sklearn.impute import SimpleImputer #sklearn is amazing librarie to make ML models
#from sklearn we have preprocessing library that contains a lot of classes methodes to preprocess any data set
# finaly we have Imputer class willallow us to take care of those missing data

#importing the data set-------------------------------------------------------------------

dataset = pd.read_csv(r"C:\Users\ie\Myenvpy\ML_Preprocessing_Data\Data.csv")
X = dataset.iloc[:, :-1].values # Select the values of the specify matrix X from dataset
Y = dataset.iloc[:, 3].values # Select the values of the specify Matrix y from dataset

#Missing data------------------------------------------------------------------------------

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

#Encode categorical data------------------------------------------------------------------
labelEncoder_X = LabelEncoder()
X[:, 0] = labelEncoder_X.fit_transform(X[:, 0])
ct = ColumnTransformer([("encoder", OneHotEncoder(), [0])], remainder = 'passthrough')
X = ct.fit_transform(X)
print(X)
labelEncoder_Y = LabelEncoder()
Y = labelEncoder_Y.fit_transform(Y)
print(Y)

#Splitting the dataset into training dataset and testing dataset
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size= 0.2, random_state = 0)

# Feature scalling 
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)





