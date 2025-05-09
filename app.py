import streamlit as st
import pandas as pd
import pickle
import xgboost

with open('HR.sav', 'rb') as file:
    data = pickle.load(file)

st.title("HR Employee Attrition")
st.image("https://miro.medium.com/v2/resize:fit:1100/format:webp/1*hVmDd7kBxo2z2FmH8Auvlg.png", width=500)
st.header("Fill in the Employee Information")

# --- Personal Info ---
with st.expander("🧍 Personal Information"):
    c1, c2, c3 = st.columns(3)
    age = c1.number_input("Age", 18, 60)
    gender_selected = c2.selectbox("Gender", ['Female', 'Male'])
    gender_selected_id = {'Female': 0, 'Male': 1}[gender_selected]
    MaritalStatus_selected = c3.selectbox("Marital Status", ['Single', 'Married', 'Divorced'])
    MaritalStatus_selected_id = {'Single': 2, 'Married': 1, 'Divorced': 0}[MaritalStatus_selected]

# --- Education & Experience ---
with st.expander("🎓 Education & Experience"):
    c1, c2, c3 = st.columns(3)
    Education = c1.number_input("Education", 1, 5)
    EducationField_selected = c2.selectbox("Education Field", ['Human Resources', 'Life Sciences', 'Marketing', 'Medical', 'Technical Degree', 'Other'])
    EducationField_selected_id = dict(zip(['Human Resources','Life Sciences','Marketing','Medical','Technical Degree','Other'], [0,1,2,3,5,4]))[EducationField_selected]
    NumCompaniesWorkedCategory_selected = c3.selectbox("Num Companies Worked", ['<= 2', '<= 4', '<= 6', '<= 8', '> 10'])
    NumCompaniesWorkedCategory_selected_id = {'<= 2': 0, '<= 4': 1, '<= 6': 2, '<= 8': 3, '> 10': 4}[NumCompaniesWorkedCategory_selected]

# --- Job Details ---
with st.expander("💼 Job Information"):
    c1, c2, c3 = st.columns(3)
    Department_selected = c1.selectbox("Department", ['Human Resources', 'Research & Development', 'Sales'])
    Department_selected_id = {'Human Resources': 0, 'Research & Development': 1, 'Sales': 2}[Department_selected]
    
    JobRole_selected = c2.selectbox("Job Role", ['Healthcare Representative','Human Resources','Laboratory Technician','Manager','Manufacturing Director','Research Director','Research Scientist','Sales Executive','Sales Representative'])
    JobRole_selected_id = dict(zip(JobRole_selected.splitlines(), range(9)))[JobRole_selected]
    
    BusinessTravel_selected = c3.selectbox("Business Travel", ['Non-Travel', 'Travel_Frequently', 'Travel_Rarely'])
    BusinessTravel_selected_id = {'Non-Travel': 0, 'Travel_Frequently': 1, 'Travel_Rarely': 2}[BusinessTravel_selected]

    c4, c5, c6 = st.columns(3)
    JobLevel = c4.number_input("Job Level", 1, 5)
    JobInvolvement = c5.number_input("Job Involvement", 1, 5)
    OverTime_selected = c6.selectbox("Over Time", ['No', 'Yes'])
    OverTime_selected_id = {'No': 0, 'Yes': 1}[OverTime_selected]

# --- Satisfaction & Ratings ---
with st.expander("📊 Satisfaction & Ratings"):
    c1, c2, c3 = st.columns(3)
    JobSatisfaction = c1.number_input("Job Satisfaction", 1, 5)
    EnvironmentSatisfaction = c2.number_input("Environment Satisfaction", 1, 5)
    RelationshipSatisfaction = c3.number_input("Relationship Satisfaction", 1, 5)

    c4, c5, c6 = st.columns(3)
    WorkLifeBalance = c4.number_input("Work Life Balance", 1, 5)
    PerformanceRating = c5.number_input("Performance Rating", 1, 5)
    StockOptionLevel = c6.number_input("Stock Option Level", 1, 5)

# --- Financial & Other Categorical ---
with st.expander("💰 Financial & Work History"):
    c1, c2, c3 = st.columns(3)
    HourlyRate = c1.number_input("Hourly Rate", 30, 100, step=20)
    DailyRate_selected = c2.selectbox("Daily Rate Category", ['<= 400', '<= 600', '<= 800', '<= 1000', '<= 1200','> 1200'])
    DailyRate_selected_id = dict(zip(['<= 400', '<= 600', '<= 800', '<= 1000', '<= 1200','> 1200'], [2, 3, 4, 0, 1, 5]))[DailyRate_selected]
    MonthlyIncomeCategory_selected = c3.selectbox("Monthly Income", ['<= 2500', '<= 5000', '<= 7500', '<= 10000', '<= 12500', '<= 15000', '> 15000'])
    MonthlyIncomeCategory_selected_id = dict(zip(MonthlyIncomeCategory_selected.splitlines(), [3, 4, 5, 0, 1, 2, 6]))[MonthlyIncomeCategory_selected]

# --- Work Years ---
with st.expander("📅 Work Years Info"):
    c1, c2, c3 = st.columns(3)
    DistanceFromHome_selected = c1.selectbox("Distance From Home", ['<= 5','<= 10', '<= 15', '<= 20', '<= 25',  '> 25'])
    DistanceFromHome_selected_id = {'<= 5': 4,'<= 10': 0, '<= 15': 1, '<= 20': 2, '<= 25': 3,  '> 25': 5}[DistanceFromHome_selected]
    
    TotalWorkingYearsCategory_selected = c2.selectbox("Total Working Years", ['<= 5','<= 10', '<= 15', '<= 20', '<= 25', '<= 30',  '> 30'])
    TotalWorkingYearsCategory_selected_id = {'<= 5': 5, '<= 10': 0, '<= 15': 1, '<= 20': 2, '<= 25': 3, '<= 30': 4, '> 30': 6}[TotalWorkingYearsCategory_selected]

    TrainingTimesLastYear = c3.number_input("Training Times Last Year", 0, 6)

    c4, c5, c6 = st.columns(3)
    YearsAtCompanyCategory_selected = c4.selectbox("Years At Company", ['<= 5','<= 10', '<= 15', '<= 20',  '> 20'])
    YearsAtCompanyCategory_selected_id = {'<= 5': 3, '<= 10': 0, '<= 15': 1, '<= 20': 2, '> 20': 4}[YearsAtCompanyCategory_selected]

    YearsInCurrentRoleCategory_selected = c5.selectbox("Years In Current Role", ['<= 3', '<= 6', '<= 9', '<= 12', '> 12'])
    YearsInCurrentRoleCategory_selected_id = {'<= 3': 1, '<= 6': 2, '<= 9': 3, '<= 12': 0, '> 12': 4}[YearsInCurrentRoleCategory_selected]

    YearsSinceLastPromotionCategory_selected = c6.selectbox("Years Since Last Promotion", ['<= 3', '<= 6', '<= 9', '<= 12', '> 12'])
    YearsSinceLastPromotionCategory_selected_id = {'<= 3': 1, '<= 6': 2, '<= 9': 3, '<= 12': 0, '> 12': 4}[YearsSinceLastPromotionCategory_selected]

    YearsWithCurrManagerCategory_selected = st.selectbox("Years With Current Manager", [ '<= 3', '<= 6', '<= 9','<= 12', '> 12'])
    YearsWithCurrManagerCategory_selected_id = {'<= 3': 1, '<= 6': 2, '<= 9': 3,'<= 12': 0, '> 12': 4}[YearsWithCurrManagerCategory_selected]

# --- Prediction ---
selected_items = pd.DataFrame({
    "Age": [age],
    "BusinessTravel": [BusinessTravel_selected_id],
    "Department": [Department_selected_id],
    "Education": [Education],
    "EducationField": [EducationField_selected_id],
    "EnvironmentSatisfaction": [EnvironmentSatisfaction],
    "Gender": [gender_selected_id],
    "HourlyRate": [HourlyRate],
    "JobInvolvement": [JobInvolvement],
    "JobLevel": [JobLevel],
    "JobRole": [JobRole_selected_id],
    "JobSatisfaction": [JobSatisfaction],
    "MaritalStatus": [MaritalStatus_selected_id],
    "OverTime": [OverTime_selected_id],
    "PerformanceRating": [PerformanceRating],
    "RelationshipSatisfaction": [RelationshipSatisfaction],
    "StockOptionLevel": [StockOptionLevel],
    "TrainingTimesLastYear": [TrainingTimesLastYear],
    "WorkLifeBalance": [WorkLifeBalance],
    "DailyRateCategory": [DailyRate_selected_id],
    "DistanceFromHomeCategory": [DistanceFromHome_selected_id],
    "MonthlyIncomeCategory": [MonthlyIncomeCategory_selected_id],
    "NumCompaniesWorkedCategory": [NumCompaniesWorkedCategory_selected_id],
    "TotalWorkingYearsCategory": [TotalWorkingYearsCategory_selected_id],
    "YearsAtCompanyCategory": [YearsAtCompanyCategory_selected_id],
    "YearsInCurrentRoleCategory": [YearsInCurrentRoleCategory_selected_id],
    "YearsSinceLastPromotionCategory": [YearsSinceLastPromotionCategory_selected_id],
    "YearsWithCurrManagerCategory": [YearsWithCurrManagerCategory_selected_id]
}, index=[0])

if st.button("Predict attrition"):
    pre = data.predict(selected_items)
    result = "Yes" if pre[0] == 1 else "No"
    st.success(f"🔍 Expected to leave: **{result}**")
