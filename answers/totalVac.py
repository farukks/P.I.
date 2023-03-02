
import pandas as pd
df=pd.read_csv('C:\\Users\\akdem\OneDrive - marun.edu.tr\\Masaüstü\\country_vaccination_stats.csv')
df=df.fillna(0)

df["daily_vaccinations"]=pd.to_numeric(df["daily_vaccinations"])#converting
date="2021-01-06"
df_date=df[df["date"]==date]

total_vac=df["daily_vaccinations"].sum()

print("total vaccinations on ",date, ":", total_vac )