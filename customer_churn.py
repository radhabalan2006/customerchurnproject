import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import joblib

print("Pandas imported successfully!")
# Load the dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Dataset loaded successfully!")
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)
print(df.isnull().sum())
print(df["TotalCharges"].dtype)
# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print(df["TotalCharges"].dtype)
print(df["Churn"].value_counts())
import matplotlib.pyplot as plt

df["Churn"].value_counts().plot(kind="bar")

plt.title("Customer Churn Count")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.show()
# Create LabelEncoder object
le = LabelEncoder()

# Convert all text columns into numbers
for column in df.columns:
    if df[column].dtype == "object":
        df[column] = le.fit_transform(df[column])

print(df.head())
# Features (Input)
X = df.drop("Churn", axis=1)

# Target (Output)
y = df["Churn"]

print(X.head())
print(y.head())
from sklearn.model_selection import train_test_split

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)
# Create model
model = LogisticRegression(max_iter=1000)

# Train model
model.fit(X_train, y_train)

print("Model Trained Successfully!")
from sklearn.metrics import accuracy_score

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix")
print(cm)
print(classification_report(y_test, y_pred))
joblib.dump(model, "customer_churn_model.pkl")

print("Model Saved Successfully!")