import random
import pandas as pd

LAST_NAME = "Tojot"
SEED_NUM = 5
FAVORITE_ARTIST = "NFRealMusic"

random.seed(SEED_NUM)

print("=== 1. GENERATED TRANSACTION RECORDS ===")
customers = [f"{LAST_NAME}_C{i}" for i in range(1, 6)]
products = {
    "NOTEBOOK": 50.00,
    "PEN": 20.00,
    "USB": 350.00,
    "HEADPHONES": 1200.00,
    "CALCULATOR": 750.00
}

trans_records = []
product_keys = list(products.keys())

for _ in range(12):
    cust = random.choice(customers)
    prod = random.choice(product_keys)
    qty = random.randint(1, len(FAVORITE_ARTIST) + 2)
    price = products[prod]
    total_val = qty * price
    trans_records.append({
        "Customer": cust,
        "Product": prod,
        "Quantity": qty,
        "Unit_Price": price,
        "Total_Value": total_val
    })

repeated_trans = trans_records[0]
trans_records.append(repeated_trans)

df_trans = pd.DataFrame(trans_records)
print(df_trans.head(5).to_string())

print("\n=== 2. ORGANIZED TRANSACTION DATA ===")
df_org_trans = df_trans.sort_values(by=["Customer", "Product"])
print(df_org_trans.head(5).to_string())

print("\n=== 3. REPEATED / DISTINCT TRANSACTIONS ===")
df_trans_cleaned = df_trans.drop_duplicates()
dataset_total = df_trans_cleaned["Total_Value"].sum()
print(f"Overall Dataset Transaction Value: {dataset_total}")
print("Identified Duplicates (Sample):")
print(df_trans[df_trans.duplicated(keep=False)].head(2).to_string())

print("\n=== 4. TRANSACTION VALUES SUMMARY ===")
val_summary = df_trans_cleaned[["Quantity", "Unit_Price", "Total_Value"]].describe().reset_index()
print(val_summary.head(5).to_string())

print("\n=== 5. CUSTOMER AND PRODUCT SUMMARIES ===")
customer_summary = df_trans_cleaned.groupby("Customer")["Total_Value"].sum().reset_index()
print("Customer Total Spending:")
print(customer_summary.to_string())

product_summary = df_trans_cleaned.groupby("Product")["Quantity"].sum().reset_index()
print("\nProduct Total Quantities Sold:")
print(product_summary.to_string())

print("\n=== 6. ORDERED RESULTS ===")
df_ordered_trans = df_trans_cleaned.sort_values(by="Total_Value", ascending=False)
print(df_ordered_trans.head(5).to_string())

print("\n=== 7. FINAL CONSOLIDATED TRANSACTION REPORT ===")
final_trans_report = df_trans_cleaned.sort_values(by=["Customer", "Total_Value"], ascending=[True, False])
print(final_trans_report.head(5).to_string())