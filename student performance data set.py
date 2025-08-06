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
print(f"The rows and columns used in the project are \n {students_training.shape}")

##to see columns mentioned in dataset
print(f"The columns available are\n {students_training.columns}")

##to find out datatypes of columns 
print(f"The datatypes of the columns are as follows \n {students_training.dtypes}")


##to filter desired columns
student_performance = students_training.loc [:,("sex","studytime","traveltime","romantic","G1","G2","G3")]

print (student_performance.columns)

##statistics
##to find the highest grade in G1 

print(f"The best grade in the first term was {student_performance["G1"].max()}")

##Best grade in G2
print(f"The best grade in the second term was {student_performance["G2"].max()}")

##Best grade in G3
print(f"The best grade in the third term was {student_performance["G3"].max()}")

##correlation matrix to identify the feature with the most impact

correlation_matrix = student_performance.corr (numeric_only = True)
print(correlation_matrix)


##visualize correlation
matrix_plot = px.scatter_matrix(student_performance, dimensions=["G1","G2","G3","traveltime","studytime"])

matrix_plot.show()

