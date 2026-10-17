import random
import pandas as pd

LAST_NAME = "Tojot"
SEED_NUM = 5
FAVORITE_ARTIST = "NFRealMusic"

random.seed(SEED_NUM)

print("=== 1. GENERATED TEST DATA ===")
sources = [f"{LAST_NAME}_T1", f"{LAST_NAME}_T2", f"{LAST_NAME}_T3", f"{LAST_NAME}_T4", f"{LAST_NAME}_T5"]
categories = ["TEMPERATURE", "VOLTAGE", "CURRENT", "PRESSURE", "SPEED"]

eng_records = []
for _ in range(10):
    src = random.choice(sources)
    cat = random.choice(categories)
    val = round(random.uniform(10.0, 500.0) + len(FAVORITE_ARTIST), 2)
    eng_records.append({"Test_Source": src, "Measurement_Category": cat, "Recorded_Value": val})

repeated_record = {"Test_Source": sources[0], "Measurement_Category": categories[0], "Recorded_Value": 123.45}
eng_records.append(repeated_record)
eng_records.append(repeated_record)

df_eng = pd.DataFrame(eng_records)
print(df_eng.head(5).to_string())

print("\n=== 2. ORGANIZED TEST DATA ===")
df_organized = df_eng.sort_values(by=["Test_Source", "Measurement_Category"])
print(df_organized.head(5).to_string())

print("\n=== 3. REPEATED & DISTINCT DATA ===")
df_eng_cleaned = df_eng.drop_duplicates()
print(f"Total original rows: {len(df_eng)} | Distinct rows: {len(df_eng_cleaned)}")
print("Identified Duplicates:")
print(df_eng[df_eng.duplicated(keep=False)].head(3).to_string())

print("\n=== 4. NUMERICAL AND CATEGORICAL SUMMARIES ===")
summary_numerical = df_eng_cleaned.groupby("Measurement_Category")["Recorded_Value"].agg(['mean', 'min', 'max', 'count']).reset_index()
print(summary_numerical.to_string())

print("\n=== 5. PROCESSED RESULTS ===")
print(df_eng_cleaned.head(5).to_string())

print("\n=== 6. ORDERED RESULTS ===")
df_ordered = df_eng_cleaned.sort_values(by="Recorded_Value", ascending=False)
print(df_ordered.head(5).to_string())

print("\n=== 7. FINAL SUMMARY ===")
final_summary = df_eng_cleaned.sort_values(by=["Test_Source", "Recorded_Value"], ascending=[True, False])
print(final_summary.head(5).to_string())