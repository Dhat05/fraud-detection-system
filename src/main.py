import csv

print("=" * 50)
print("      BANK FRAUD DETECTION SYSTEM")
print("=" * 50)

total_transactions = 0
fraud_transactions = 0
safe_transactions = 0

report_file = open("data/fraud_report.csv", "w", newline="")
report_writer = csv.writer(report_file)
report_writer.writerow(["Transaction_ID", "Amount", "Status"])

with open("data/transactions.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        transaction_id = row[1]
        amount = int(row[2])
        status = row[3]

        total_transactions += 1

        if status == "FRAUD":
            fraud_transactions += 1
            print(f"🚨 FRAUD | ID: {transaction_id} | Amount: ₹{amount}")

            report_writer.writerow([
                transaction_id,
                amount,
                status
            ])
        else:
            safe_transactions += 1
            print(f"✅ SAFE  | ID: {transaction_id} | Amount: ₹{amount}")

report_file.close()

print("\n" + "=" * 50)
print("SUMMARY REPORT")
print("=" * 50)

print(f"Total Transactions : {total_transactions}")
print(f"Fraud Transactions : {fraud_transactions}")
print(f"Safe Transactions  : {safe_transactions}")

print("\nFraud report saved to data/fraud_report.csv")
print("Analysis Completed Successfully ✅")
