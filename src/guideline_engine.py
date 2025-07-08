def check_guideline_compliance(age, cancer_type):
    min_age = {
        "Breast": 40,
        "Cervical": 21,
        "Colorectal": 50
    }
    return age >= min_age[cancer_type]
