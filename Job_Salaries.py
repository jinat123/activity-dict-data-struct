jobssalaries = {
    "Software Engineer": 120000,
    "Data Scientist": 115000,
    "Graphic Designer": 60000,
    "Project Manager": 95000,
    "Accountant": 70000,
    "Nurse": 75000,
    "Teacher": 50000,
    "Marketing Manager": 90000,
    "Web Developer": 85000,
    "Sales Manager": 100000
}

entire_dict_jobs = jobssalaries

third_job = list(jobssalaries.keys())[2]
third_job_salary = jobssalaries[third_job]

seventh_job = list(jobssalaries.keys())[6]
jobssalaries[seventh_job] = 55000  # Updated salary

ninth_job = list(jobssalaries.keys())[8]
del jobssalaries[ninth_job]

last_key_value_pair_jobs = list(jobssalaries.items())[-1]