import pandas as pd
import glob

files = glob.glob("*.csv")

myheader = ['Printer', 'User', 'Cost Center', 'Total Pages', 'Color Pages', 'Sheets', 'Cost']
cols = [5, 21, 22] + list(range(26, 30))
df = pd.concat((pd.read_csv(f, encoding = 'latin1', header = None, usecols = cols, names = myheader) for f in files))
df.Cost = df.Cost.replace('[\$,]', '', regex = True).astype(float)


df = df.fillna("N/A")
grouped = df.groupby(['Printer', 'User', 'Cost Center'], as_index = False)['Total Pages', 'Color Pages', 'Sheets', 'Cost'].sum()


for printer in grouped.Printer.unique():
    grouped[grouped["Printer"] == printer].to_excel((printer + ".xlsx")[8: ], index = False)

print("Done!")