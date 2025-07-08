import pandas as pd

def assess_risk(row):
    risk = 0
    if row["FamilyHistory"] == "Yes":
        risk += 2
    if row["Smoking"] == "Yes":
        risk += 1
    if row["Alcohol"] == "Yes":
        risk += 1
    if row["Exercise"] in ["None", "No"]:
        risk += 1
    if row["Age"] > 50:
        risk += 2
    return "High" if risk >= 4 else "Medium" if risk >= 2 else "Low"

def run_risk_assessment(input_path):
    df = pd.read_csv(input_path)
    df["RiskLevel"] = df.apply(assess_risk, axis=1)
    return df
