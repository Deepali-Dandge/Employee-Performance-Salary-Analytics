import csv
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# -------------------------------------------------
# Output File Name
# -------------------------------------------------
file_name = "Data_Analysis_Python_Pandas_Task_01.csv"

# -------------------------------------------------
# Sample Data
# -------------------------------------------------
department = ["IT", "HR", "Sales", "Finance", "Marketing"]

job_roles = {
    "IT": ["Data Analyst", "Developer", "Software Engineer", "System Administrator"],
    "HR": ["HR Executive", "Recruiter", "HR Manager", "Talent Acquisition Specialist"],
    "Sales": ["Sales Executive", "Sales Manager", "Business Development Executive"],
    "Finance": ["Finance Manager", "Accountant", "Financial Analyst", "Auditor"],
    "Marketing": ["Marketing Executive", "Digital Marketer", "SEO Specialist", "Marketing Manager"]
}

attrition = ["Yes", "No"]

# -------------------------------------------------
# Male and Female Names
# -------------------------------------------------
male_names = [
    "Amit", "Rahul", "Vikas", "Rohit", "Sagar",
    "Akash", "Rakesh", "Nitin", "Sachin", "Deepak",
    "Tejas", "Lakshya", "Karan", "Manav","Akash","Aman",
    "Abhay", "Arman", "Kalpesh", "Karan", "Yash", "Rohan", "Tanmay",
    "Pravin", "Samarth", "Raju", "Nilesh", "Samarth", "Siddharth"
]

female_names = [
    "Sneha", "Pooja", "Neha", "Anjali", "Priya",
    "Kiran", "Meena", "Komal", "Swati", "Riya",
    "Sailee", "Roshni", "Farhana", "Rubina", "Deepali",
    "Divya", "Smita", "Nandini", "Manvi", "Preeti", "Komal",
    "Tanvi", "Sakshi", "Anvi", "Sandhya", "Pragati", "Swati"
]

last_names = [
    "Sharma", "Patil", "Deshmukh", "Joshi", "Verma",
    "Singh", "Pawar", "Gupta", "Kulkarni", "Yadav",
    "Kapoor", "Bhatt", "Dube", "Johare", "Lokhande",
    "Shinde", "Wahi", "More", "Dandge", "Chaudhary",
    "Sinha", "Kaushal", "Malhotra", "Advani", "Shetty"
]

# ----------------------------------------------------
# CSV Header
# ----------------------------------------------------
header = [
    "Employee ID",
    "Employee Name",
    "Department",
    "Job Role",
    "Gender",
    "Age",
    "Experience Years",
    "Monthly Salary",
    "Performance Score",
    "Projects Completed",
    "Training Hours",
    "Joining Date",
    "Attrition"
]

# ------------------------------------------------------
# Generate 1000 Employees
# ------------------------------------------------------
with open(file_name, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)
    writer.writerow(header)

    start_date = datetime(2025, 1, 1)

    for i in range(1, 1001):

        employee_id = f"E{i:04}"

        # Select name and matching gender
        if random.choice([True, False]):
            first_name = random.choice(male_names)
            gender = "Male"
        else:
            first_name = random.choice(female_names)
            gender = "Female"

        employee_name = first_name + " " + random.choice(last_names)

        department_name = random.choice(department)
        job_role = random.choice(job_roles[department_name])

        age = random.randint(21, 60)
        experience_year = random.randint(1, 9)
        performance_score = random.randint(1, 10)
        project_completed = random.randint(1, 10)
        training_hours = random.randint(10, 120)
        monthly_salary = random.randrange(20000, 150001, 1000)

        joining_date = start_date + timedelta(days=random.randint(0, 364))

        attritionn = random.choice(attrition)

        writer.writerow([
            employee_id,
            employee_name,
            department_name,
            job_role,
            gender,
            age,
            experience_year,
            monthly_salary,
            performance_score,
            project_completed,
            training_hours,
            joining_date.strftime("%d-%m-%Y"),
            attritionn
        ])

print("=============================================================")
print("Data_Analysis_Python_Pandas_Task_01.csv Created Successfully!")
print("Total Records : 1000")
print("=============================================================")
