import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os

# Load dataset
df = pd.read_csv("data/salary_data.csv")

print("First 5 rows:")
print(df.head())

# Remove missing values
df = df.dropna()

# Create Label Encoders
education_encoder = LabelEncoder()
gender_encoder = LabelEncoder()
job_encoder = LabelEncoder()

# Convert text columns into numbers
df["Education Level"] = education_encoder.fit_transform(df["Education Level"])
df["Gender"] = gender_encoder.fit_transform(df["Gender"])
df["Job Title"] = job_encoder.fit_transform(df["Job Title"])

# Select input features
X = df[["Age", "Gender", "Education Level", "Job Title", "Years of Experience"]]

# Target column
y = df["Salary"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate
print("\nModel Performance")
print("------------------------")
print("R² Score:", round(r2_score(y_test, predictions), 3))
print("Mean Absolute Error:", round(mean_absolute_error(y_test, predictions), 2))

# Create model folder if it doesn't exist
os.makedirs("model", exist_ok=True)

# Save model
joblib.dump(model, "model/salary_model.pkl")

feature_importance = {
    "Feature": X.columns,
    "Importance": model.feature_importances_
}

feature_df = pd.DataFrame(feature_importance)
feature_df.to_csv("model/feature_importance.csv", index=False)

joblib.dump(education_encoder, "model/education_encoder.pkl")
joblib.dump(gender_encoder, "model/gender_encoder.pkl")
joblib.dump(job_encoder, "model/job_encoder.pkl")

print("\nModel saved successfully!")