def get_next_screening(age, cancer_type, risk_level):
    interval_years = {
        "Breast": {"Low": 3, "Medium": 2, "High": 1},
        "Cervical": {"Low": 5, "Medium": 3, "High": 1},
        "Colorectal": {"Low": 10, "Medium": 5, "High": 1},
    }
    return interval_years[cancer_type][risk_level]
