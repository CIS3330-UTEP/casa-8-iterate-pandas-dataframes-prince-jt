import pandas as pd

df = pd.read_csv("./big-mac-full-index.csv")

def line(row):
    print(f"date: {row['date']}, currency: {row['currency_code']}")
    return None

results= df.apply(line, axis=1)

for index, row in df.iterrows():
    print(f"date:{row['date']}, currency: {row['currency_code']}")
