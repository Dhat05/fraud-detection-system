import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/transactions.csv",
    header=None,
    names=["Timestamp", "Transaction_ID", "Amount", "Status"]
)

fraud_count = (df["Status"] == "FRAUD").sum()
safe_count = (df["Status"] == "SAFE").sum()

print("\n===== FRAUD ANALYSIS REPORT =====")
print(f"Total Transactions : {len(df)}")
print(f"Fraud Transactions : {fraud_count}")
print(f"Safe Transactions  : {safe_count}")

plt.figure(figsize=(6,4))
plt.bar(["Fraud", "Safe"], [fraud_count, safe_count])

plt.title("Fraud Detection Analysis")
plt.xlabel("Transaction Type")
plt.ylabel("Count")

plt.savefig("screenshots/fraud_chart.png")

print("\nChart saved successfully!")
print("Location: screenshots/fraud_chart.png")
