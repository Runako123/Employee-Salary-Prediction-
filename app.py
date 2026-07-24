import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Employee Salary Analytics Dashboard",
    page_icon="💼",
    layout="wide"
)

# ======================================================
# LOAD DATA
# ======================================================

df = pd.read_csv("data/salary_data.csv").dropna()

model = joblib.load("model/salary_model.pkl")
education_encoder = joblib.load("model/education_encoder.pkl")
gender_encoder = joblib.load("model/gender_encoder.pkl")
job_encoder = joblib.load("model/job_encoder.pkl")

feature_df = pd.read_csv("model/feature_importance.csv")

# ======================================================
# HEADER
# ======================================================

st.title("💼 Employee Salary Analytics Dashboard")

st.write(
    "Predict employee salaries using Machine Learning and explore salary insights."
)

st.divider()

# ======================================================
# KPI CARDS
# ======================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Employees", len(df))

with col2:
    st.metric("Model Accuracy", "94%")

with col3:
    st.metric("Mean Absolute Error", "$8,525")

st.divider()

# ======================================================
# PREDICTION SECTION
# ======================================================

st.header("🤖 Salary Prediction")

left, right = st.columns(2)

with left:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=70,
        value=30
    )

    gender = st.selectbox(
        "Gender",
        sorted(df["Gender"].dropna().unique())
    )

    education = st.selectbox(
        "Education Level",
        sorted(df["Education Level"].dropna().unique())
    )

with right:

    job = st.selectbox(
        "Job Title",
        sorted(df["Job Title"].dropna().unique())
    )

    experience = st.number_input(
        "Years of Experience",
        min_value=0,
        max_value=40,
        value=5
    )

if st.button("💰 Predict Salary"):

    gender_encoded = gender_encoder.transform([gender])[0]
    education_encoded = education_encoder.transform([education])[0]
    job_encoded = job_encoder.transform([job])[0]

    prediction = model.predict([[
        age,
        gender_encoded,
        education_encoded,
        job_encoded,
        experience
    ]])

    st.success(
        f"### Estimated Salary: ${prediction[0]:,.2f}"
    )

st.divider()

# ======================================================
# VISUALIZATIONS
# ======================================================

st.header("📊 Salary Analytics")

chart1, chart2 = st.columns(2)

with chart1:

    fig1 = px.histogram(
        df,
        x="Salary",
        nbins=30,
        title="Salary Distribution"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True,
        key="histogram"
    )

with chart2:

    job_salary = (
        df.groupby("Job Title")["Salary"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig2 = px.bar(
        job_salary,
        x="Job Title",
        y="Salary",
        title="Average Salary by Job Title"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True,
        key="job_bar"
    )

fig3 = px.pie(
    df,
    names="Education Level",
    title="Education Level Distribution"
)

st.plotly_chart(
    fig3,
    use_container_width=True,
    key="education_pie"
)

st.divider()

# ======================================================
# FEATURE IMPORTANCE
# ======================================================

st.header("⭐ Feature Importance")

feature_df = feature_df.sort_values(
    by="Importance",
    ascending=False
)

fig4 = px.bar(
    feature_df,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Model Feature Importance"
)

st.plotly_chart(
    fig4,
    use_container_width=True,
    key="feature_importance"
)

st.divider()

st.caption("Developed using Python • Streamlit • Scikit-Learn • Plotly")