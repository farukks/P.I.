import pandas as pd

df=pd.read_csv('C:\\Users\\akdem\OneDrive - marun.edu.tr\\Masaüstü\\country_vaccination_stats.csv')
df = df.fillna(0)#fill missing data with 0

df["daily_vaccinations"]=pd.to_numeric(df["daily_vaccinations"])#converting
country=df.groupby("country")

medians=country["daily_vaccinations"].median()#computing median

highest_median=medians.nlargest(3)#find top 3 countries with highest median daily vac

print("top 3 highest median ", highest_median)
