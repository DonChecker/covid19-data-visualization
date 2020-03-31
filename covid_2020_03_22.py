# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates

import math

country_plots = False
world_log_plot = True


covid_data = pd.read_csv('covid_19_data_2020_03_31.csv')
print(covid_data.info())
print(covid_data["Country/Region"].describe())
#print(covid_data["ObservationDate"].describe())
#print(covid_data[["Deaths","Province/State","ObservationDate"]].head(1000))

df=pd.DataFrame(covid_data)
df1 = df.groupby(["ObservationDate"], as_index=False).sum()
print(df1)



x_values = [datetime.datetime.strptime(d,"%m/%d/%Y").date() for d in df1["ObservationDate"]]
ax = plt.gca()
ax.xaxis_date()

formatter = mdates.DateFormatter("%Y-%m-%d")

ax.xaxis.set_major_formatter(formatter)

locator = mdates.DayLocator()
#ax.xaxis.set_major_locator(locator)

if country_plots:

    plt.subplot(2,1,1)
    plt.title("Whole World")
    plt.plot(x_values,df1["Deaths"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(x_values,df1["Confirmed"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()
    
    """
    Without China
    """
    
    df2 = df[df["Country/Region"] != "Mainland China"]
    df2 = df2.groupby(["ObservationDate"], as_index=False).sum()
    
    plt.subplot(2,1,1)
    plt.title("Without China")
    plt.plot(x_values,df2["Deaths"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(x_values,df2["Confirmed"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()
    
    """
    China vs Rest
    """
    
    df2 = df[df["Country/Region"] != "Mainland China"]
    df2 = df2.groupby(["ObservationDate"], as_index=False).sum()
    
    plt.subplot(2,1,1)
    plt.title("China vs Rest of the World")
    plt.plot(x_values,df2["Deaths"])
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(x_values,df2["Confirmed"])
    plt.xticks(rotation=45)
    
    df2 = df[df["Country/Region"] == "Mainland China"]
    df2 = df2.groupby(["ObservationDate"], as_index=False).sum()
    
    plt.subplot(2,1,1)
    plt.plot(x_values,df2["Deaths"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(x_values,df2["Confirmed"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()
    
    
    """
    US vs China vs Rest
    """
    
    df2 = df[df["Country/Region"] != "Mainland China"]
    df2 = df2[df2["Country/Region"] != "US"]
    df2 = df2.groupby(["ObservationDate"], as_index=False).sum()
    
    plt.subplot(2,1,1)
    plt.title("US vs China vs Rest")
    plt.plot(x_values,df2["Deaths"])
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(x_values,df2["Confirmed"])
    plt.xticks(rotation=45)
    
    df2 = df[df["Country/Region"] == "Mainland China"]
    df2 = df2.groupby(["ObservationDate"], as_index=False).sum()
    plt.subplot(2,1,1)
    plt.plot(x_values,df2["Deaths"])
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(x_values,df2["Confirmed"])
    plt.xticks(rotation=45)
    
    df2 = df[df["Country/Region"] == "US"]
    df2 = df2.groupby(["ObservationDate"], as_index=False).sum()
    plt.subplot(2,1,1)
    plt.plot(x_values,df2["Deaths"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(x_values,df2["Confirmed"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()
    
    
    """
    US vs China vs Italy
    """
    
    df2 = df[df["Country/Region"] == "Italy"]
    df2 = df2.groupby(["ObservationDate"], as_index=False).sum()
    x_values = [datetime.datetime.strptime(d,"%m/%d/%Y").date() for d in df2["ObservationDate"]]
    
    plt.subplot(2,1,1)
    plt.title("US vs China vs Italy")
    plt.plot(x_values,df2["Deaths"])
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(x_values,df2["Confirmed"])
    plt.xticks(rotation=45)
    
    
    df2 = df[df["Country/Region"] == "Mainland China"]
    df2 = df2.groupby(["ObservationDate"], as_index=False).sum()
    x_values = [datetime.datetime.strptime(d,"%m/%d/%Y").date() for d in df2["ObservationDate"]]
    plt.subplot(2,1,1)
    plt.plot(x_values,df2["Deaths"])
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(x_values,df2["Confirmed"])
    plt.xticks(rotation=45)
    
    df2 = df[df["Country/Region"] == "US"]
    df2 = df2.groupby(["ObservationDate"], as_index=False).sum()
    x_values = [datetime.datetime.strptime(d,"%m/%d/%Y").date() for d in df2["ObservationDate"]]
    plt.subplot(2,1,1)
    plt.plot(x_values,df2["Deaths"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(x_values,df2["Confirmed"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()
    
    
    
    df3=df[df["Country/Region"] == "South Korea"].groupby(["ObservationDate"], as_index=False).sum()
    plt.subplot(2,1,1)
    plt.title("South Korea")
    plt.plot(x_values,df3["Deaths"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(x_values,df3["Confirmed"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()
    #print(df3["Country/Region"].unique())
    
    
    df4=df[df["Country/Region"] == "Italy"].groupby(["ObservationDate"], as_index=False).sum()
    x_values = [datetime.datetime.strptime(d,"%m/%d/%Y").date() for d in df4["ObservationDate"]]
    plt.subplot(2,1,1)
    plt.title("Italy")
    plt.plot(x_values,df4["Deaths"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(x_values,df4["Confirmed"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()
    #print(df4["Deaths"])
    
    
    df4=df[df["Country/Region"] == "Germany"].groupby(["ObservationDate"], as_index=False).sum()
    x_values = [datetime.datetime.strptime(d,"%m/%d/%Y").date() for d in df4["ObservationDate"]]
    plt.subplot(2,1,1)
    plt.title("Germany vs US")
    plt.plot(x_values,df4["Deaths"])
    #plt.grid()
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(x_values,df4["Confirmed"])
    #plt.grid()
    plt.xticks(rotation=45)
    
    
    df4=df[df["Country/Region"] == "US"].groupby(["ObservationDate"], as_index=False).sum()
    x_values = [datetime.datetime.strptime(d,"%m/%d/%Y").date() for d in df4["ObservationDate"]]
    plt.subplot(2,1,1)
    plt.plot(x_values,df4["Deaths"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(x_values,df4["Confirmed"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()
    
    df4=df[df["Country/Region"] == "Germany"].groupby(["ObservationDate"], as_index=False).sum()
    x_values = [datetime.datetime.strptime(d,"%m/%d/%Y").date() for d in df4["ObservationDate"]]
    plt.subplot(2,1,1)
    plt.title("Germany")
    plt.plot(x_values,df4["Deaths"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(x_values,df4["Confirmed"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()
    
    df4=df[df["Country/Region"] == "US"].groupby(["ObservationDate"], as_index=False).sum()
    x_values = [datetime.datetime.strptime(d,"%m/%d/%Y").date() for d in df4["ObservationDate"]]
    plt.subplot(2,1,1)
    plt.title("US")
    plt.plot(x_values,df4["Deaths"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(x_values,df4["Confirmed"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()
    
    df4=df[df["Country/Region"] == "Finland"].groupby(["ObservationDate"], as_index=False).sum()
    x_values = [datetime.datetime.strptime(d,"%m/%d/%Y").date() for d in df4["ObservationDate"]]
    plt.subplot(2,1,1)
    plt.title("Finland vs Sweden")
    plt.plot(x_values,df4["Deaths"])
    #plt.grid()
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(x_values,df4["Confirmed"])
    #plt.grid()
    plt.xticks(rotation=45)
    
    
    df4=df[df["Country/Region"] == "Sweden"].groupby(["ObservationDate"], as_index=False).sum()
    x_values = [datetime.datetime.strptime(d,"%m/%d/%Y").date() for d in df4["ObservationDate"]]
    plt.subplot(2,1,1)
    plt.plot(x_values,df4["Deaths"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.subplot(2,1,2)
    plt.plot(x_values,df4["Confirmed"])
    plt.grid()
    plt.xticks(rotation=45)
    plt.show()


if world_log_plot:

    countries = df["Country/Region"].unique()
    countries = countries[countries != "Diamond Princess"]
    countries = countries[countries != "Others"]
    data_type = "Deaths"
    days=5
    countries_remarkables=[]
    
    for country in countries:
        df5=df[df["Country/Region"] == country].groupby(["ObservationDate"], as_index=False).sum()
        datapoints = math.floor((len(df5)-1)/days)
        offset = (len(df5)-1) % days
            
        case_increase=[]
        cases=[]
        for i in range(datapoints):
            if df5.iloc[(i+1)*days+offset][data_type] > 100:
                case_increase.append(df5.iloc[(i+1)*days+offset][data_type]-df5.iloc[i*days+offset][data_type])
                cases.append(df5.iloc[(i+1)*days+offset][data_type])
            #print(df6)
        if len(cases) > 0:  
            plt.loglog(cases,case_increase)
            plt.plot(cases[-1],case_increase[-1],'x')
            #if (case_increase[-1] < cases[-1]*0.2 and cases[-1] > 1000) or cases[-1] > 20000:
            countries_remarkables.append(country)
            plt.text(cases[-1],case_increase[-1],country)
        plt.title('Word overview: '+data_type+' cases')
    plt.grid()
    plt.xlabel(data_type+' Cases')
    plt.ylabel('Increase within '+str(days)+' days.')
    plt.savefig('test.svg')
    plt.show()
    
    
    for country in countries_remarkables:
        df5=df[df["Country/Region"] == country].groupby(["ObservationDate"], as_index=False).sum()
        datapoints = math.floor((len(df5)-1)/days)
        offset = (len(df5)-1) % days
            
        case_increase=[]
        cases=[]
        for i in range(datapoints):
            if df5.iloc[i*days+offset][data_type] > 100:
                case_increase.append(df5.iloc[(i+1)*days+offset][data_type]-df5.iloc[i*days+offset][data_type])
                cases.append(df5.iloc[(i+1)*days+offset][data_type])
            #print(df6)
        if len(cases) > 0:  
            plt.loglog(cases,case_increase)
            plt.plot(cases[-1],case_increase[-1],'x')
            if country == 'Japan':
                print('Japan - Previous Cases: '+str(cases[-2])+' , Increase: '+str(case_increase[-1])+' , New Cases: '+str(cases[-1]))
            plt.text(cases[-1],case_increase[-1],country)
    plt.title('Remarkable countries: '+data_type+' cases'+' , Country: '+str(country))
    plt.grid()
    plt.xlabel(data_type+' Cases')
    plt.ylabel('Increase within '+str(days)+' days.')
    plt.show()
    
    
