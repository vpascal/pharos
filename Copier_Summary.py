import pandas as pd
import glob

files = glob.glob("*.csv")

myheader = ['Copier', 'User', 'Cost Center', 'Total Copies', 'Color Copies', 'Cost']
cols = [6] + list(range(18, 23))
df = pd.concat((pd.read_csv(f, encoding = 'latin1', header = None, usecols = cols, names = myheader) for f in files))
df.Cost = df.Cost.replace('[\$,]', '', regex = True).astype(float)

df = df.fillna("N/A")
grouped = df.groupby(['Copier', 'User', 'Cost Center'], as_index = False)['Total Copies', 'Color Copies', 'Cost'].sum()

for printer in grouped.Copier.unique():
  grouped[grouped["Copier"] == printer].to_excel((printer + ".xlsx")[10: ], index = False)

print("Done!")
