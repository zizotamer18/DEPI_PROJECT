# DEPI_PROJECT
This Python-based tool processes employee data to uncover insights and generate predictive analytics. Designed for HR professionals and team leads, it helps identify key factors influencing organizational dynamics.

Overview
• This project aims to predict employee attrition (whether employees are likely to leave the company) using machine learning techniques. By analyzing various factors such as job roles, income, tenure, and more, the project helps organizations identify at-risk employees and implement retention strategies.

Dataset

  • The project uses the IBM HR Analytics Employee Attrition & Performance dataset, which contains 1470 entries with 35 columns. The dataset includes employee demographics, job-related factors, performance ratings, and other relevant information.
Key Steps

Data Loading and Exploration
  -	Loaded the dataset and displayed basic information to understand its structure and contents.
  -	Generated summary statistics to get an overview of numerical features.

Data Visualization

  •	Employee Attrition Count: Visualized the distribution of attrition (employees who stayed vs. left).
  •	Numerical Features vs Attrition: Compared numerical features (e.g., age, income) between employees who stayed and those who left.
  •	Categorical Features by Attrition: Analyzed how categorical features (e.g., department, job role) relate to attrition.
  •	Correlation Heatmap: Identified correlations between different features and attrition.
  •	Monthly Income vs Total Working Years by Attrition: Explored the relationship between income, tenure, and attrition.
  •	Attrition Count by Department: Compared attrition rates across different departments.
  •	Age Distribution by Attrition: Analyzed how age distribution differs between employees who stayed and those who left.
  •	Job Role Distribution by Gender and Attrition: Examined job roles and gender in relation to attrition.
  •	Attrition Breakdown by Department and Job Role: Provided a hierarchical view of attrition by department and job role.

Data Preprocessing

  •	Removed unnecessary columns and encoded categorical variables to prepare the data for model training.

Model Training and Evaluation

  •	Used XGBoost to train a predictive model for employee attrition.
  •	Applied SMOTE (Synthetic Minority Over-sampling Technique) to address class imbalance in the dataset.
  •	Evaluated the model using accuracy, classification report, and confusion matrix.


  -	XGBoost: Chosen for its efficiency and effectiveness in handling tabular data, especially with class imbalance. It builds an ensemble of decision trees to improve prediction accuracy.
  -	SMOTE: Used to balance the dataset by generating synthetic samples for the minority class, reducing bias and improving model performance on the minority class.
Results

  • The final model achieved an accuracy of 84.35%, providing valuable insights for employee retention strategies.


License
  - This project is licensed under the MIT License.
