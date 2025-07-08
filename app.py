import pandas as pd
from src.risk_assessment import run_risk_assessment
from src.screening_schedule import get_next_screening
from src.reminder_generator import generate_reminders
from src.guideline_engine import check_guideline_compliance

input_file = "data/sample_patients.csv"
df = run_risk_assessment(input_file)

df["NextScreeningInYears"] = df.apply(
    lambda row: get_next_screening(row["Age"], row["CancerType"], row["RiskLevel"]), axis=1)

df["CompliantWithGuideline"] = df.apply(
    lambda row: check_guideline_compliance(row["Age"], row["CancerType"]), axis=1)

reminders = generate_reminders(df)

print("📢 Screening Reminders:\n")
print(reminders)
