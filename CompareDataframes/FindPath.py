import os
import pandas as pd


cp = os. getcwd()
slash = '\\'
filetype = '.csv'
filename = 'threats'
file = cp + slash + filename + filetype
hazards = pd.read_csv(file)
print("Dataframe is created from the following csv in this folder")
print(file)



