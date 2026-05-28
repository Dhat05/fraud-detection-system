from datetime import datetime
import random
import csv

log_file = open("logs/fraud.log", "a")

csv_file = open("data/transactions.csv", "a", newline="")

writer = csv.writer(csv_file)

print("\n🏦 BANK FRAUD DETECTION SYSTEM STARTED\n")

fraud_count = 0
safe_count = 0

for i in range(10):

    transaction_id = random.randint(1000, 9999)

    amount = random.randint(1000, 100000)

    time = datetime.now()

    if amount > 50000:
        status = "FRAUD"
        fraud_count += 1
    else:
        status = "SAFE"
        safe_count += 1

    writer.writerow([time, transaction_id, amount, status])

    message = f"{time} | Transaction ID: {transaction_id} | Amount: ₹{amount} | {status}"

    print(message)

    log_file.write(message + "\n")

log_file.close()

csv_file.close()

print("\n✅ Scan Completed")

print("\n📊 FINAL REPORT")
print(f"🚨 Fraud Transactions: {fraud_count}")
print(f"✅ Safe Transactions: {safe_count}")






