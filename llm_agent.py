import pandas as pd
import ollama

# Load dataset
df = pd.read_csv("data/financial_anomaly_data.csv")

# Basic statistics
total_txns = len(df)
total_amount = df["Amount"].sum()
avg_amount = df["Amount"].mean()
max_amount = df["Amount"].max()

unique_accounts = df["AccountID"].nunique()
unique_merchants = df["Merchant"].nunique()
unique_locations = df["Location"].nunique()

# Top merchants
top_merchants = (
    df["Merchant"]
    .value_counts()
    .head(5)
    .to_dict()
)

# Top locations
top_locations = (
    df["Location"]
    .value_counts()
    .head(5)
    .to_dict()
)

prompt = f"""
You are a Senior Financial Risk Consultant working for a global conglomerate.

Analyze the transaction dataset and generate executive-level business insights.

DATASET SUMMARY

Total Transactions: {total_txns:,}

Total Transaction Amount: {total_amount:,.2f}

Average Transaction Amount: {avg_amount:,.2f}

Maximum Transaction Amount: {max_amount:,.2f}

Unique Accounts: {unique_accounts}

Unique Merchants: {unique_merchants}

Unique Locations: {unique_locations}

Top Merchants:
{top_merchants}

Top Locations:
{top_locations}

Columns Available:
- Timestamp
- TransactionID
- AccountID
- Amount
- Merchant
- TransactionType
- Location

Provide the following sections:

1. EXECUTIVE SUMMARY

Provide a concise overview of the transaction landscape and major observations.

2. KEY RISKS

Identify:
- Fraud Risks
- Merchant Risks
- Geographic Risks
- Operational Risks
- Transaction Monitoring Risks
- Financial Risks

Support observations with numbers wherever possible.

3. BUSINESS QUESTIONS & ANSWERS

Generate important management-level questions that arise from the data and provide business answers based on the dataset statistics.

4. ROOT CAUSE ANALYSIS

Provide likely explanations behind the identified risks and anomalies.

5. RECOMMENDATIONS

Provide:
- Immediate Actions
- Medium-Term Improvements
- Long-Term Controls

6. BUSINESS IMPACT

Explain the impact on:
- Revenue
- Compliance
- Fraud Exposure
- Operations
- Reputation

7. DASHBOARD INSIGHTS

Recommend 5 KPIs that should be appear on an Executive Power BI Dashboard.

Use professional consulting language suitable for:
- CFO
- CRO
- COO
- Board Members

Focus on business impact, trends, concentrations, anomalies and risk exposure.

Do not provide technical code.
"""

print("Generating AI Risk Report...")
print()

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response["message"]["content"])