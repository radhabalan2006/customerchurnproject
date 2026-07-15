# 📊 Customer Churn Prediction using Machine Learning

## 📌 About the Project

Customer retention is one of the biggest challenges for subscription-based businesses. Losing existing customers is often more expensive than acquiring new ones. This project focuses on predicting whether a customer is likely to leave a company (customer churn) based on their demographic information, account details, and service usage.

The goal of this project was not only to build a machine learning model but also to understand the complete workflow of a real-world data science project—from data preprocessing to model evaluation.

---

## 🎯 Project Objective

The objective of this project is to predict customer churn using machine learning techniques. By identifying customers who are at risk of leaving, businesses can take proactive steps to improve customer satisfaction and retention.

---

## 📂 Dataset

**Dataset:** Telco Customer Churn Dataset

The dataset contains customer information such as:

- Customer ID
- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure
- Internet Service
- Contract Type
- Payment Method
- Monthly Charges
- Total Charges
- Churn Status

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

---

## 📈 Project Workflow

### 1. Data Collection

Loaded the Telco Customer Churn dataset into Python using Pandas.

---

### 2. Data Exploration

Explored the dataset to understand:

- Number of rows and columns
- Data types
- Missing values
- Statistical summary

Used:

```python
df.head()
df.info()
df.describe()
```

---

### 3. Data Cleaning

- Converted `TotalCharges` into numeric format
- Handled missing values
- Prepared the dataset for machine learning

---

### 4. Data Visualization

Created visualizations to understand customer churn distribution.

Example:

- Customer Churn Count
- Churn Distribution

---

### 5. Data Preprocessing

Since machine learning models cannot understand text values directly, categorical columns were converted into numerical values using Label Encoding.

---

### 6. Feature Selection

Separated the dataset into:

- Features (X)
- Target Variable (y)

---

### 7. Train-Test Split

Split the dataset into:

- 80% Training Data
- 20% Testing Data

---

### 8. Model Building

Implemented the Logistic Regression algorithm to predict customer churn.

---

### 9. Model Evaluation

Evaluated model performance using:

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 📊 Sample Output

The project predicts whether a customer is likely to churn or not.

Example:

```
Prediction:
Customer Churn = Yes
```

or

```
Prediction:
Customer Churn = No
```

---

## 📁 Project Structure

```
CustomerChurnPrediction/
│
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── customer_churn.py
├── customer_churn_model.pkl
├── README.md
└── screenshots/
```

---

## 🚀 How to Run

Clone the repository

```bash
git clone <repository-link>
```

Navigate to the project folder

```bash
cd CustomerChurnPrediction
```

Install dependencies

```bash
pip install pandas numpy matplotlib scikit-learn
```

Run the project

```bash
python customer_churn.py
```

---

## 📚 What I Learned

Working on this project helped me strengthen my understanding of:

- Data preprocessing
- Handling missing values
- Feature engineering
- Exploratory Data Analysis (EDA)
- Machine Learning workflow
- Logistic Regression
- Model evaluation techniques
- Python libraries used in data science

More importantly, it gave me hands-on experience in solving a practical business problem using machine learning.

---

## 🔮 Future Improvements

Some improvements that can be added in future versions include:

- Testing multiple machine learning algorithms
- Hyperparameter tuning
- Feature importance analysis
- Deployment using Flask or Streamlit
- Interactive dashboard using Power BI

---

## 👨‍💻 Author

**Radha B**

B.Tech – Artificial Intelligence and Data Science

Passionate about Machine Learning, Data Science, and Full Stack Development.

---

## ⭐ If you found this project useful

If you like this project, consider giving it a ⭐ on GitHub. It motivates me to continue building and sharing more projects.
