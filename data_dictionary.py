import pandas as pd

df = pd.read_csv("data/financial_anomaly_data.csv")

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns)

print("\nDATA TYPES")
print(df.dtypes)

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nSAMPLE DATA")
print(df.head())

print("\nCOLUMN LIST")
print(df.columns.tolist())