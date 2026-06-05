import pandas as pd

df = pd.read_csv("data/financial_anomaly_data.csv")

# to clean missing rows
df = df.dropna()

# to duplicatehigh value transactions
high_amount = df[df["Amount"] > 90000]

# to duplicate transaction IDs
duplicates = df[df.duplicated("TransactionID")]

# find merchant concentration
merchant_counts = df["Merchant"].value_counts()

# find top merchant
top_merchant = merchant_counts.index[0]
top_merchant_count = merchant_counts.iloc[0]

print("TOTAL TRANSACTIONS:", len(df))
print("HIGH VALUE TRANSACTIONS:", len(high_amount))
print("DUPLICATE TRANSACTIONS:", len(duplicates))
print("TOP MERCHANT:", top_merchant)
print("TOP MERCHANT COUNT:", top_merchant_count)