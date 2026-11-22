import csv
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

df=pd.read_csv("Data_Analysis_Python_Pandas_Task_01.csv")
print(df)
#TASK 1
print("============================TASK 1===============================")
print("First 10 and Last 5 records:")
print(df.head(10))
print(df.tail(5))
print("===========================================================")
print("Number of rows and columns:")
print(df.shape)
print("===========================================================")
print("Column names and data types:")
print(df.dtypes)
print("===========================================================")
print("Statistical summary using describe():")
print(df.describe())

#TASK 2
print("===========================TASK 2================================")
print("Identifying And Removing Duplicated Records:")
print(df.duplicated().sum())
print(df.drop_duplicates)
print("===========================================================")
print("Missing Values:")
print(df.isnull().sum())
print("===========================================================")
print("Converting Joining Date to DateTime Format:")
Joining_Date=pd.to_datetime(df["Joining Date"],dayfirst=True,errors="coerce")
print(Joining_Date)
print("===========================================================")
Monthly_Salary=(df["Monthly Salary"]<0)
print("Negative Salaries:")
print(Monthly_Salary.head(10))
print("============================================================")
Performance_Score=(df["Performance Score"]<1)|(df["Performance Score"]>10)
print("Invalid Performance Score:")
print(Performance_Score)
#TASK 3
print("=========================TASK 3===================================")
print("Annual Salary Column:")
df["Annual_Salary"]=(df["Monthly Salary"]*12)
print(df)
print("============================================================")
print("Experience Level Column:")
df["Experience_Level"]=np.where(df["Experience Years"]<=2,"Fresher",
                                np.where(df["Experience Years"]>=7,"Senior","Mid level"))
print(df[["Experience Years","Experience_Level"]])
print("============================================================")
print("Performance Score Column")
df["Performance_Category"]=np.where(df["Performance Score"]<=2,"Low",
                                    np.where(df["Performance Score"]>=7,"High","Average"))
print(df.head(10))
print("============================================================")
print("Create Salary Band")
df["Salary_Band"]=np.where(df["Monthly Salary"]<=30000,"Low",
                           np.where(df["Monthly Salary"]>=60000,"High","Avereage"))
print(df[["Monthly Salary","Salary_Band"]])
print("============================================================")
print("Years In Company")
current_date=pd.Timestamp.today()
df["Years_In_Company"]=((current_date-Joining_Date).dt.days/365.25).round(1)
print(df[["Employee Name","Years_In_Company"]])

#TASK 4
print("===========================TASK 4================================")
print("Average Salary By Department:")
Average_sal_by_dept=(df.groupby("Department")["Monthly Salary"].mean().sort_values(ascending=False))
print(Average_sal_by_dept)
print("=============================================================")
print("Highest Paid Employee is:")
highest_paid=df.loc[df["Monthly Salary"].idxmax()]
print(highest_paid)
print("=============================================================")
print("Top 10 Employees By Performance Score:")
top_10_perf=(df[["Employee ID","Employee Name","Department","Job Role","Performance Score"]].sort_values("Performance Score",ascending=False).head(10))
print(top_10_perf)
print("==============================================================")
print("Average Salary By Job Role:")
Avg_sal_by_job_role=(df.groupby("Job Role")["Monthly Salary"].mean().sort_values(ascending=False))
print(Avg_sal_by_job_role)
print("==============================================================")
print("Average Experience Across Departments:")
avg_exp_by_dept=(df.groupby("Department")["Experience Years"].mean().sort_values(ascending=False))
print(avg_exp_by_dept)
print("==============================================================")
print("Calculate Employee Attrition Percentage:")
att_count=(df["Attrition"]=="Yes").sum()
total_emp=len(df)
att_per=(att_count/total_emp)*100
print("Total Employees:",total_emp)
print("Employees Left:",att_count)
print("Attrition Percentage:",round(att_per,2),"%")
print("===============================================================")
print("Employees With High Salaries But Low Performance:")
avg_sal=df["Monthly Salary"].mean()
High_sal_low_perf=df[(df["Monthly Salary"]> avg_sal)&(df["Performance Score"]<5)]
print(High_sal_low_perf[["Employee ID","Department","Job Role","Monthly Salary","Performance Score"]])

#TASK 5
print("============================TASK 5==============================")
print("Using Group Function To Summarize Department Performance:")
dept_perf=(df.groupby("Department")["Performance Score"].mean())
print(dept_perf)
print("=================================================================")
print("Using Aggregate Function To Calculate Multiple Statistics:")
print(df.groupby("Department")["Monthly Salary"].agg(["mean","max","min"]))
print("=================================================================")
print("Using Sort Values To Rank Employees:")
print(df.sort_values("Performance Score",ascending=False).head(10))
print("=================================================================")
print("Using Location and Ilocation Function To Filter Records:")
print("========= Loc:Employees From IT Department ==============")
print(df.loc[df["Department"]=="IT"])
print("========= Iloc:Display First 5 rows==============")
print(df.iloc[0:5])
print("==================================================================")
print("Using Pivot Table To Compare Salary And Performance Score:")
print(pd.pivot_table(df,
                     index="Department",
                     values=["Monthly Salary","Performance Score"],
                     aggfunc="mean"))
print("===================================================================")
print("Using Merge Function To Combine Employee and Department Budget Datasets:")
#Create department Budget Dataset
budget=pd.DataFrame({"Department":["IT","HR","Sales","Finance","Marketing"],
                     "Budget":[500000,200000,300000,400000,250000]})
#Merging Both Dataset
df=pd.merge(df,budget,on="Department",how="left")
print(df[["Employee ID","Department","Budget"]])
print("====================================================================")
print("Using Vectorized operations to classify employees:")
df["Performance_Category"]=np.where(df["Performance Score"]>=8,"High","low")
print(df[["Employee ID","Performance Score","Performance_Category"]])

#TASK 6
print("======================= TASK 6 ===============================")
df.to_excel("cleaned_employee_data.xlsx",index=False)
print("===============================================")
print("Data Is Transformed To Excel Sheet Successfully")
print("===============================================")
#Department Summary
Department_Summary=df.groupby("Department").agg(Employee_Count=("Employee ID","count"),
                                                Average_Salary=("Monthly Salary","mean"),
                                                Average_Performance=("Performance Score","mean")).round(2).reset_index()
print(Department_Summary)
Department_Summary.to_excel("Department_Summary.xlsx",index=False,sheet_name="Department_Summary")
print("==========================================================")
print("Department Summary Is Exported To Excel Sheet Successfully")
print("==========================================================")
#Top 10 Performers
print("Top 10 Performers:")
Top_10_Performers=df.sort_values("Performance Score",ascending=False).head(10)
print(Top_10_Performers)
Top_10_Performers.to_excel("Top_10_Performers.xlsx",index=False,sheet_name="Top_10_Performers")
print("==========================================================")
print("Top 10 Performers Is Exported To Excel Sheet Successfully")
print("==========================================================")
#Business Insights
Insights=pd.DataFrame({"Business Insight":["Total Employees","Average Monthly Salary","Average Performance Score",
                                           "Highest Monthly Salary","Lowest Monthly Salary","Employees In IT",
                                           "Employees In HR","Employees In Sales","Employees In Finance",
                                           "Employees In Marketing","Employees Who Left"],
                       "Result":[len(df),df["Monthly Salary"].mean(),df["Performance Score"].mean(),
                                 df["Monthly Salary"].max(),df["Monthly Salary"].min(),
                                 (df["Department"]=="IT").sum(),(df["Department"]=="HR").sum(),
                                 (df["Department"]=="Sales").sum(),(df["Department"]=="Finance").sum(),
                                 (df["Department"]=="Marketing").sum(),(df["Attrition"]=="Yes").sum()]})
print(Insights)
Insights.to_excel("Insights.xlsx",index=False,sheet_name="Insights")
print("==========================================================")
print("Business Insights Is Exported To Excel Sheet Successfully")
print("==========================================================")
