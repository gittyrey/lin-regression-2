##student performance dataset

##required data libraries
import pandas as pd
import numpy as np 

## required for plotting graphs
import plotly.express as px


#required for creating and training model
import keras

##the data is contained in a csv file and will be read using the pandas library.  

students_training = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv")

##Include a pandas code to tell us number of rows and columns (respectively)
print(students_training.shape)

##to see columns mentioned in dataset
print(students_training.columns)

##to find out datatypes of columns 
print(students_training.dtypes)


##to filter desired columns

students_training_dataset = students_training.loc[:,('traveltime','studytime','failures','freetime','paid')]

print(students_training_dataset.head(10))

