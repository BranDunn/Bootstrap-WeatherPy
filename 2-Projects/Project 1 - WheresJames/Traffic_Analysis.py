# Dependencies\n",
    import pandas as pd
    import requests
    import json
    import matplotlib.pyplot as plt
    import datetime as dt
    
    from fuzzywuzzy import fuzzy
    from fuzzywuzzy import process

# Load in File from resources - data source = https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-traffic-counts\n",
    file = 'MASTER_TRAFFIC_COUNT.csv'

# Read and display preview with pandas\n",
df = pd.read_csv(file)
df_clean = df.dropna(axis=1, how='all')
df_clean = df_clean.drop(['Locator', 'Dir', 'Amount of traffic in the directional movement', 'Unnamed: 20', 'Unnamed: 254'], axis=1)
df_clean.head()

#Avg Weekday Traffic is mostly complete from Nov 2015 to Mar 2011\n",
    #AM and PM are continuous throughout

#covert date column into date time object
df_clean['Last day of the study'].dtype

#convert date column from date string to a date/time object\n",
df_clean['Date Time'] = pd.to_datetime(df_clean['Last day of the study'])

df_clean['Month'] = df_clean['Date Time'].dt.month
df_clean['Month'] = df_clean['Month'].map('{:02d}'.format)
df_clean['Year'] = df_clean['Date Time'].dt.year
df_clean['Year-Month'] = df_clean[\"Year\"].map(str) + '-' + df_clean[\"Month\"].map(str)
df_clean.head()
df_clean['Date Time'].dtype



#how many total sensor locations?\n",
sensor_count = df_clean['Main Location'].nunique()
sensor_nan = df_clean[['Main Location']]
#checking for null values - Master ID had many NaN entries, none observed for Main Location\n",
#df2 = sensor_nan.isnull().any(axis=1)\n",
#df2\n",
print('There are', sensor_count, 'Main sensor locations collecting data in the Denver area')



#aggragate values for line graph\n",
#subset dataframe down to date, am, and pm\n",
am_pm_df = df_clean[['Date Time', 'Morning AM Peak Hourly Volume', 'Evening PM Peak Hourly Volume']]

#groupby the date (not the location)\n",
grouped_df = am_pm_df.groupby(\"Date Time\").sum()
grouped_df.head()

# morn_x_axis = grouped_df['Morning AM Peak Hourly Volume'].sum()
# eve_x_axis = grouped_df['Evening PM Peak Hourly Volume'].sum()

# y_axis = grouped_df['Date Time']

#plt.plot(grouped_df.index, grouped_df['Evening PM Peak Hourly Volume'])
#plt.plot(grouped_df.index, grouped_df['Morning AM Peak Hourly Volume'])"


#check to see if there are more sensors in 2007 than in other years\n",

#subset original to what I need\n",
df_datacheck = df_clean[['Main Location', 'Second Location', 'Year']]\n",

#groupby main loc, second loc, and date time and count #groupby a list this time and .count()\n",
#grouped_dcheck = df_datacheck.groupby(['Second Location', 'Main Location', 'Year'])\n",
#grouped_dcheck['Year'].count().to_csv('grouped_datacheck_count.csv')\n"





#clean location names to eliminate multiple spellings of same Main locations\n",
# main_locations = df_clean['Main Location'].unique()\n",
# main_locations\n",

#Minimizing the data to parse \n",
# mlocations = df_clean['Main Location']

# #mlocations[0:10]\n",

# for location in mlocations:

#     def get_ratio(row):
#         name = row['Main Location']
#         print(fuzz.token_sort_ratio(name, location))
#         return fuzz.token_sort_ratio(name, location)
#     #df_clean.loc[df_clean.apply(get_ratio, axis=1) > 70, \"Main Location\"] = location"


