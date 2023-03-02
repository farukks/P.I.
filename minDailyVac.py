
import pandas as pd

df=pd.read_csv('C:\\Users\\akdem\OneDrive - marun.edu.tr\\Masaüstü\\country_vaccination_stats.csv')
df = df.groupby('country').transform(lambda x: x.fillna(x.min()))
df = df.fillna(0)
print(df.to_string())