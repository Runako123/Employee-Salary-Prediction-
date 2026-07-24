# 💼 Employee Salary Prediction & Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-orange?logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-blueviolet?logo=plotly)

## 📌 Project Overview

The **Employee Salary Prediction & Analytics Dashboard** is an interactive Machine Learning application developed using **Python**, **Scikit-learn**, **Pandas**, **Plotly**, and **Streamlit**.

The application predicts an employee's estimated salary based on important professional and demographic characteristics while also providing an interactive analytics dashboard for exploring workforce salary trends.

This project demonstrates the complete Data Science workflow—from data preprocessing and machine learning model development to deployment in a professional web dashboard.

---

## 🎯 Objectives

* Predict employee salaries using Machine Learning.
* Analyze salary trends across different employee groups.
* Visualize workforce data through interactive dashboards.
* Demonstrate practical Data Science and Informatics skills.
* Provide an easy-to-use web application for salary estimation.

---

# 🚀 Key Features

### 🤖 Machine Learning Salary Prediction

Predicts employee salaries using:

* Age
* Gender
* Education Level
* Job Title
* Years of Experience

The model instantly estimates an employee's expected salary based on the selected inputs.

---

### 📊 Interactive Analytics Dashboard

The dashboard presents important workforce statistics including:

* 👥 Total Employees
* 🎯 Model Accuracy
* 📉 Mean Absolute Error (MAE)
* 💰 Average Salary

---

### 📈 Interactive Data Visualizations

The dashboard includes multiple interactive charts such as:

* Salary Distribution
* Average Salary by Job Title
* Education Level Distribution
* Feature Importance Analysis

These visualizations help users understand salary patterns and the factors influencing salary prediction.

---

### 📁 Employee Dataset Explorer

Users can browse and search the employee dataset directly within the application.

Features include:

* Search employees by Job Title
* Interactive data table
* Fast filtering
* Easy data exploration

---

## 🧠 Machine Learning Workflow

The project follows a complete Machine Learning pipeline:

### 1. Data Collection

Employee salary dataset containing demographic and employment information.

### 2. Data Cleaning

* Missing value removal
* Data validation
* Feature preparation

### 3. Data Preprocessing

Categorical variables encoded using **LabelEncoder**.

Encoded features include:

* Gender
* Education Level
* Job Title

---

### 4. Feature Selection

The model is trained using:

* Age
* Gender
* Education Level
* Job Title
* Years of Experience

Target Variable:

* Salary

---

### 5. Model Training

Algorithm used:

**Random Forest Regressor**

Reasons for selection:

* High prediction accuracy
* Handles nonlinear relationships
* Resistant to overfitting
* Excellent performance on structured tabular datasets

---

### 6. Model Evaluation

Performance Metrics:

* ✅ Model Accuracy (R² Score): **94%**
* ✅ Mean Absolute Error (MAE): **8,525**

These metrics indicate that the model provides strong predictive performance while maintaining a relatively low prediction error.

---

## 📊 Technologies Used

| Technology   | Purpose                    |
| ------------ | -------------------------- |
| Python       | Programming Language       |
| Streamlit    | Interactive Web Dashboard  |
| Pandas       | Data Processing            |
| NumPy        | Numerical Computation      |
| Scikit-learn | Machine Learning           |
| Plotly       | Interactive Visualizations |
| Matplotlib   | Data Visualization         |
| Joblib       | Model Serialization        |

---

## 📂 Project Structure

```text
EmployeeSalaryPrediction/
│
├── app.py
├── train_model.py
├── requirements.txt
│
├── data/
│   └── salary_data.csv
│
├── model/
│   ├── salary_model.pkl
│   ├── education_encoder.pkl
│   ├── gender_encoder.pkl
│   ├── job_encoder.pkl
│   └── feature_importance.csv
│
├── pages/
│
├── screenshots/
│
└── README.md
```

---

# 📸 Application Screenshots

# 💰 Employee Salary Prediction

An interactive Streamlit web app that predicts employee salary using Machine Learning.

## 📸 Screenshots


### Dashboard
![Dashboard](https://raw.githubusercontent.com/Runako123/Employee-Salary-Prediction-/main/screenshots/app_dashboard.png)

### Salary Prediction Page
![Salary Prediction](https://raw.githubusercontent.com/Runako123/Employee-Salary-Prediction-/main/screenshots/app_Salary_Prediction.png)

### Feature Importance
![Feature Importance](https://raw.githubusercontent.com/Runako123/Employee-Salary-Prediction-/main/screenshots/Feature_Importance.png)

### Average Salary by Job Title
![Average Salary](https://raw.githubusercontent.com/Runako123/Employee-Salary-Prediction-/main/screenshots/Average_SalarybyJobTitle.png)

### Education Level Distribution
![Education](https://raw.githubusercontent.com/Runako123/Employee-Salary-Prediction-/main/screenshots/EducationLevelDistribution_Visualisation.png)

### Salary Distribution
![Salary Distribution](https://raw.githubusercontent.com/Runako123/Employee-Salary-Prediction-/main/screenshots/Salary_Distribution_Visualisation.png)


## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
# ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/EmployeeSalaryPrediction.git
```

Navigate into the project:

```bash
cd EmployeeSalaryPrediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 🎯 Skills Demonstrated

This project demonstrates practical knowledge in:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Data Visualization
* Feature Engineering
* Machine Learning
* Model Evaluation
* Predictive Analytics
* Dashboard Development
* Python Programming
* Interactive Web Applications

---

# 📈 Future Improvements

Planned enhancements include:

* Dark Mode Business Dashboard
* Custom CSS Styling
* Executive KPI Cards
* Additional Machine Learning Algorithms
* Model Comparison Dashboard
* Prediction Confidence Intervals
* Download Prediction Reports
* Cloud Deployment
* User Authentication
* REST API Integration

---

# 👨‍💻 Author

**Runakorwashe Padera**

Data Science | Informatics | Machine Learning | Python Development

Passionate about developing intelligent data-driven applications that transform raw data into actionable insights.

---

