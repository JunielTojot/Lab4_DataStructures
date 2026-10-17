import random
import pandas as pd

LAST_NAME = "Tojot"
SEED_NUM = 5
FAVORITE_ARTIST = "NFRealMusic"

random.seed(SEED_NUM)

print("=== 1. GENERATED PERFORMANCE RECORDS ===")
student_names = [f"{LAST_NAME}_Student_{i}" for i in range(1, 6)]
subjects = ["PROGRAMMING", "MATHEMATICS", "ELECTRONICS", "PHYSICS", "ENGLISH"]

def get_performance_category(score):
    if score >= 85: return "Excellent"
    elif score >= 75: return "Good"
    elif score >= 60: return "Passing"
    else: return "Failing"

perf_records = []
for student in student_names:
    for subj in subjects:
        score = round(random.uniform(50.0, 100.0), 2)
        perf_records.append({
            "Student_Name": student,
            "Subject": subj,
            "Score": score,
            "Performance_Category": get_performance_category(score)
        })

repeated_perf = perf_records[0]
perf_records.append(repeated_perf)
incomplete_record = {"Student_Name": student_names[0], "Subject": "PHYSICS", "Score": None, "Performance_Category": "Incomplete"}
perf_records.append(incomplete_record)

df_perf = pd.DataFrame(perf_records)
print(df_perf.head(5).to_string())

print("\n=== 2. ORGANIZED STUDENT/SUBJECT DATA ===")
df_org_perf = df_perf.sort_values(by=["Student_Name", "Subject"])
print(df_org_perf.head(5).to_string())

print("\n=== 3. REPEATED & INCOMPLETE RECORDS ===")
df_perf_cleaned = df_perf.drop_duplicates()
print("Incomplete Records Found:")
print(df_perf_cleaned[df_perf_cleaned["Score"].isnull()].to_string())
print("\nRepeated Records Found (Sample):")
print(df_perf[df_perf.duplicated(keep=False)].head(2).to_string())

print("\n=== 4. PERFORMANCE CATEGORIES SUMMARY ===")
cat_summary = df_perf_cleaned["Performance_Category"].value_counts().reset_index()
cat_summary.columns = ["Performance_Category", "Count"]
print(cat_summary.to_string())

print("\n=== 5. STUDENT AND SUBJECT SUMMARIES ===")
valid_perf = df_perf_cleaned.dropna(subset=["Score"])
student_summary = valid_perf.groupby("Student_Name")["Score"].mean().reset_index()
print("Student Averages:")
print(student_summary.to_string())

subject_summary = valid_perf.groupby("Subject")["Score"].mean().reset_index()
print("\nSubject Averages:")
print(subject_summary.to_string())

print("\n=== 6. ORDERED RESULTS & FINAL REPORT ===")
final_perf_report = valid_perf.sort_values(by=["Student_Name", "Score"], ascending=[True, False])
print(final_perf_report.head(5).to_string())