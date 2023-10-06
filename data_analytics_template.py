import pandas as pd

#read in the csv as a data frame. We are using American Health Rankings dataset from Google Public Datasets
ahr_df = pd.read_csv('american_health_rankings.csv')

#Print first 5 rows to look at data structure
ahr_df.head()

#Get summary statistics for data frame
ahr_df.describe(include='all')

#Investigate data types. OBJECT is STRING or MIXED data type
ahr_df.dtypes

#Investigate Missing Values #here we do not need records that have a value = NULL. The value is what we will be analyzing. Can remove those records in next step
ahr_df.isnull().sum()

# Drop NaN values from 'value'
ahr_df.dropna(subset=['value'], inplace=True)

#find outliers for variables of interest (in this case, "value")
import matplotlib.pyplot as plt
plt.hist(ahr_df['value'],bins = 5)
plt.show() # you can see most values fall in btw 0-20,000 and a couple thousand fall in between 20,000-40,000

#Looking at values per state - WIP
import plotly.express as px
ahr_df["subpopulation"] = ahr_df["subpopulation"].astype(str)
fig = px.bar(ahr_df, x="measure_name", y="value", color="subpopulation", title="Who were more probable to be able-bodied - Males or Females")
fig.show()
