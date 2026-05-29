import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/transactions.csv",
    header=None,
    names=["Timestamp", "Transaction_ID", "Amount", "Status"]
)

fraud_df = df[df["Status"] == "FRAUD"]
safe_df = df[df["Status"] == "SAFE"]

fraud_count = len(fraud_df)
safe_count = len(safe_df)

print("\n===== FRAUD ANALYSIS REPORT =====")

print(f"Total Transactions : {len(df)}")
print(f"Fraud Transactions : {fraud_count}")
print(f"Safe Transactions  : {safe_count}")

print("\n===== STATISTICS =====")

print(f"Maximum Amount     : ₹{df['Amount'].max()}")
print(f"Minimum Amount     : ₹{df['Amount'].min()}")
print(f"Average Amount     : ₹{df['Amount'].mean():.2f}")
print(f"Total Fraud Amount : ₹{fraud_df['Amount'].sum()}")

plt.figure(figsize=(6,4))
plt.bar(["Fraud", "Safe"], [fraud_count, safe_count])

plt.title("Fraud Detection Analysis")
plt.xlabel("Transaction Type")
plt.ylabel("Count")

plt.savefig("screenshots/fraud_chart.png")

plt.figure(figsize=(6,6))
plt.pie(
    [fraud_count, safe_count],
    labels=["Fraud", "Safe"],
    autopct="%1.1f%%"
)

plt.title("Fraud vs Safe Transactions")
plt.savefig("screenshots/fraud_pie_chart.png")

print("\nCharts saved successfully!")
print("screenshots/fraud_chart.png")
print("screenshots/fraud_pie_chart.png")
