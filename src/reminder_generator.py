from datetime import datetime
from src.screening_schedule import get_next_screening

def generate_reminders(df):
    current_year = datetime.now().year
    df["NextScreeningInYears"] = df.apply(
        lambda row: get_next_screening(row["Age"], row["CancerType"], row["RiskLevel"]), axis=1)
    df["NextScreeningYear"] = current_year + df["NextScreeningInYears"]
    return df[["PatientID", "CancerType", "RiskLevel", "NextScreeningYear"]]
