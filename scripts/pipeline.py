
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("smart traffic data.csv")
df.head()

df.info()
df.describe()
df.isnull().sum()

#for duplicate rows
duplicates = df.duplicated().sum()
print("Duplicates:", duplicates)

print(df["Warehouse"].unique())

print(df.dtypes)

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

text_cols = df.select_dtypes(include="object").columns
for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.lower()

df["price"] = (
    df["price"]
    .astype(str)
    .str.replace(r"[^0-9.]", "", regex=True)
)
df["price"] = pd.to_numeric(df["price"], errors="coerce")

df["price"].fillna(df["price"].median(), inplace=True)

df.drop_duplicates(inplace=True)

df = df[df["price"] >= 0]

print(df.info())

print(df.isnull().sum())

print(df.describe())

failure_counts = df.isnull().sum()
print(failure_counts)

hub_activity = df.groupby("warehouse")["quantity"].sum()
hub_activity.sort_values(ascending=False).plot(kind="bar")
plt.show()

error_rate = df.groupby("category").apply(
    lambda x: x.isnull().sum().sum()
)
print(error_rate)

df.to_csv("cleaned smart traffic data.csv",
    index=False)