# Importing Pandas and Pandas Profiling 
import pandas as pd
from ydata_profiling import ProfileReport

# storing the csv data in a dataframe
df = pd.read_csv('titanic.csv') #chnage 'titanic.csv' to your file name or location
print(df)

# generating the report 
report = ProfileReport(df, minimal=True)
report.to_file(output_file="titanic_report.html")
