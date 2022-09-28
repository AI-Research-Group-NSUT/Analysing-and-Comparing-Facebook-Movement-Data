# -*- coding: utf-8 -*-
"""maharashtra_mobility.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cm5kW_V2RaZk2Q5hb1vj2OUZ1CGTOMOB
"""

from zipfile import ZipFile
import pandas as pd
pd.set_option('display.max_columns', None)
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,3)

state = "Delhi"

all_state_mobility_zip = ZipFile("/content/drive/MyDrive/mobility_covid/mobility.zip")
mh_mobility_df = pd.read_csv(all_state_mobility_zip.open("content/{}.csv".format(state)))
covid_cases = pd.read_csv("/content/drive/MyDrive/mobility_covid/phased_districts.csv")

mh_mobility_df.head()

covid_cases["Date"] = pd.to_datetime(covid_cases["Date"])
covid_cases.head()

covid_working_1 = covid_cases[covid_cases['Date']>="2020-08-13"][covid_cases["State"]==state].groupby(["Date","Phase"],as_index=False)["Confirmed"].sum()
covid_working_1["Daily"] = covid_working_1[["Date","Confirmed"]].diff()["Confirmed"]
covid_working_1

working_data_1 = mh_mobility_df[["date_time","length_km","n_crisis","n_baseline","n_difference","percent_change","z_score","start_lat","start_lon","end_lat","end_lon"]].fillna("")

working_data_1['date'] = pd.to_datetime(working_data_1['date_time']).dt.date
working_data_1['time'] = pd.to_datetime(working_data_1['date_time']).dt.time
# working_data_1['perc_change_distance'] = working_data_1['length']
working_data_1.head()

mean_km = working_data_1.groupby("date", as_index=False)['length_km','z_score'].mean()
mean_km['date'] = pd.to_datetime(mean_km['date'])
mean_km['7daymean_distance'] = mean_km['length_km'].rolling(window=7).mean()
mean_km['7daymean_z_score'] = mean_km['z_score'].rolling(window=7).mean()
mean_km['perc_change_distance'] = mean_km['length_km'].pct_change()
mean_km

# (list(set(covid_working_1["Date"])-set(mean_km['date']))[0])

# temp = pd.DataFrame({
#     "date":[pd.to_datetime("2021-07-03")],
#     "length_km":[np.nan],
#     "7daymean_distance":[np.nan],
# })
# mean_km = mean_km.append(temp).sort_values("date").reset_index(drop = True)
mean_km["daily_cases"] = covid_working_1["Daily"]
mean_km["phase"] = covid_working_1["Phase"]
mean_km['length_km'] = mean_km['length_km'].astype(float)
mean_km

max_cases = mean_km['daily_cases'].max()

plt.rcParams["figure.figsize"] = (20,3)
ax1 = plt.plot()
plt.plot(mean_km["date"].values,mean_km["7daymean_distance"].values,c='b')
plt.ylabel('7daymean of covered distance',color='b')

ax2 = plt.gca().twinx()
ax2.plot(mean_km["date"].values,mean_km["daily_cases"].values,c='r')
plt.ylabel('daily covid cases',color='r')
plt.axvspan(pd.to_datetime("2020-08-13"),pd.to_datetime("2020-11-09"), alpha=0.3, color='c')
plt.text(pd.to_datetime("2020-09-13"),max_cases,'wave 1', size=10)
plt.axvspan(pd.to_datetime("2020-11-10"),pd.to_datetime("2021-03-21"), alpha=0.3, color='m')
plt.text(pd.to_datetime("2020-12-13"),max_cases,'transition', size=10)
plt.axvspan(pd.to_datetime("2021-03-22"),pd.to_datetime("2021-07-06"), alpha=0.3, color='y')
plt.text(pd.to_datetime("2021-05-13"),max_cases,'wave 2', size=10)
plt.axvspan(pd.to_datetime("2021-07-07"),pd.to_datetime("2021-10-31"), alpha=0.3, color='g')
plt.text(pd.to_datetime("2021-08-13"),max_cases,'post 2', size=10)
plt.axvspan(pd.to_datetime("2021-04-05"),pd.to_datetime("2021-06-15"), alpha=0.5, color='palegreen')
plt.text(pd.to_datetime("2021-04-06"),0000,'Lockdown', size=10)
plt.title("Daily Trend of New Cases and Average Movement in "+state)

plt.rcParams["figure.figsize"] = (20,3)
ax1 = plt.plot()
plt.plot(mean_km["date"].values,mean_km["perc_change_distance"].values,c='b')
plt.ylabel('percent change in distance covered',color='b')

ax2 = plt.gca().twinx()
ax2.plot(mean_km["date"].values,mean_km["daily_cases"].values,c='r')
plt.ylabel('daily covid cases',color='r')
plt.axvspan(pd.to_datetime("2020-08-13"),pd.to_datetime("2020-11-09"), alpha=0.3, color='c')
plt.text(pd.to_datetime("2020-09-13"),max_cases,'wave 1', size=10)
plt.axvspan(pd.to_datetime("2020-11-10"),pd.to_datetime("2021-03-21"), alpha=0.3, color='m')
plt.text(pd.to_datetime("2020-12-13"),max_cases,'transition', size=10)
plt.axvspan(pd.to_datetime("2021-03-22"),pd.to_datetime("2021-07-06"), alpha=0.3, color='y')
plt.text(pd.to_datetime("2021-05-13"),max_cases,'wave 2', size=10)
plt.axvspan(pd.to_datetime("2021-07-07"),pd.to_datetime("2021-10-31"), alpha=0.3, color='g')
plt.text(pd.to_datetime("2021-08-13"),max_cases,'post 2', size=10)
plt.axvspan(pd.to_datetime("2021-04-05"),pd.to_datetime("2021-06-15"), alpha=0.5, color='palegreen')
plt.text(pd.to_datetime("2021-04-06"),0000,'Lockdown', size=10)
plt.title("Daily Trend of New Cases and Percent Change in Covered Distance in "+state)

plt.rcParams["figure.figsize"] = (20,3)
ax1 = plt.plot()
plt.plot(mean_km["date"].values,mean_km["7daymean_z_score"].values,c='b')
plt.ylabel('7daymean of z score',color='b')

ax2 = plt.gca().twinx()
ax2.plot(mean_km["date"].values,mean_km["daily_cases"].values,c='r')
plt.ylabel('daily covid cases',color='r')
plt.axvspan(pd.to_datetime("2020-08-13"),pd.to_datetime("2020-11-09"), alpha=0.3, color='c')
plt.text(pd.to_datetime("2020-09-13"),max_cases,'wave 1', size=10)
plt.axvspan(pd.to_datetime("2020-11-10"),pd.to_datetime("2021-03-21"), alpha=0.3, color='m')
plt.text(pd.to_datetime("2020-12-13"),max_cases,'transition', size=10)
plt.axvspan(pd.to_datetime("2021-03-22"),pd.to_datetime("2021-07-06"), alpha=0.3, color='y')
plt.text(pd.to_datetime("2021-05-13"),max_cases,'wave 2', size=10)
plt.axvspan(pd.to_datetime("2021-07-07"),pd.to_datetime("2021-10-31"), alpha=0.3, color='g')
plt.text(pd.to_datetime("2021-08-13"),max_cases,'post 2', size=10)
plt.axvspan(pd.to_datetime("2021-04-05"),pd.to_datetime("2021-06-15"), alpha=0.5, color='palegreen')
plt.text(pd.to_datetime("2021-04-06"),0000,'Lockdown', size=10)
plt.title("Daily Trend of New Cases and Z score in "+state)

print("wave 1 mean distance=", mean_km['7daymean_distance'][mean_km['phase']=="wave_1"].mean())
print("wave 2 mean distance=", mean_km['7daymean_distance'][mean_km['phase']=="wave_2"].mean())
print("wave 1 mean percent change in distance=", mean_km['perc_change_distance'][mean_km['phase']=="wave_1"].mean())
print("wave 2 mean percent change in distance=", mean_km['perc_change_distance'][mean_km['phase']=="wave_2"].mean())
print("wave 1 mean z score=", mean_km['7daymean_z_score'][mean_km['phase']=="wave_1"].mean())
print("wave 2 mean z score=", mean_km['7daymean_z_score'][mean_km['phase']=="wave_2"].mean())

plt.rcParams["figure.figsize"] = (10,10)
ax3 = plt.plot()
plt.scatter(mean_km["perc_change_distance"],mean_km["daily_cases"])
# a,b = np.polyfit(mean_km["7daymean"].values,mean_km["daily_cases"].values,1)
# plt.plot(mean_km["7daymean"], a*mean_km["7daymean"].values + b)
plt.ylim([0,max_cases])
plt.ylabel("covid cases")
plt.xlabel("percent change")
plt.title(state+" correlation")

plt.rcParams["figure.figsize"] = (10,10)
ax3 = plt.plot()
plt.scatter(mean_km["7daymean_distance"],mean_km["daily_cases"])
# a,b = np.polyfit(mean_km["7daymean"].values,mean_km["daily_cases"].values,1)
# plt.plot(mean_km["7daymean"], a*mean_km["7daymean"].values + b)
plt.ylim([0,max_cases])
plt.ylabel("covid cases")
plt.xlabel("distance covered in km")
plt.title(state+" correlation")

! pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip

from pandas_profiling import ProfileReport
report=ProfileReport(mean_km)
report

report.to_file("delhi.html")