# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
data=pd.read_csv(path)
data=data.rename(columns={'Total':'Total_Medals'})
data.columns
#Code starts here



# --------------
#Code starts here

data['Better_Event']= np.where(data.Total_Summer>data.Total_Winter,'Summer','Winter')
data['Better_Event']= np.where(data.Total_Summer==data.Total_Winter,'Both',data.Better_Event.values)
better_event=data.Better_Event.value_counts().argmax()
better_event


# --------------
#Code starts here
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(top_countries.tail(1).index,inplace=True)

def top_ten(top_countries,column):
    countries=top_countries.nlargest(10,str(column))
    country_list=list(countries['Country_Name'])
    return country_list

top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')
common=[x for x in top_10_summer if x in top_10_winter and top_10]
common


# --------------
#Code starts here
summer_df= data[data.Country_Name.isin(top_10_summer)]
winter_df=data[data.Country_Name.isin(top_10_winter)]
top_df=data[data.Country_Name.isin(top_10)]

summer_df.groupby('Country_Name')['Total_Medals'].sum().plot(kind='bar')
winter_df.groupby('Country_Name')['Total_Medals'].sum().plot(kind='bar')
top_df.groupby('Country_Name')['Total_Medals'].sum().plot(kind='bar')




# --------------
#Code starts here
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=summer_df['Golden_Ratio'].max()
summer_country_gold=summer_df[summer_df['Golden_Ratio']==summer_max_ratio]
summer_country_gold=list(summer_country_gold['Country_Name'])[0]


winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=winter_df['Golden_Ratio'].max()
winter_country_gold=winter_df[winter_df['Golden_Ratio']==winter_max_ratio]
winter_country_gold=list(winter_country_gold['Country_Name'])[0]

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=top_df['Golden_Ratio'].max()
top_country_gold=top_df[top_df['Golden_Ratio']==top_max_ratio]
top_country_gold=list(top_country_gold['Country_Name'])[0]
top_country_gold


# --------------
#Code starts here
data.drop(data.tail(1).index,inplace=True)
data_1=data.copy()
data_1['Total_Points']=((data_1['Gold_Total']*3)+(data_1['Silver_Total']*2)+(data_1['Bronze_Total']))
most_points=data_1['Total_Points'].max()
best_country=list(data_1[data_1.Total_Points==most_points]['Country_Name'])[0]



# --------------
#Code starts here
best=data[data.Country_Name==best_country]
best=best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)


