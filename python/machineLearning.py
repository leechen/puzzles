""" /*
Question
You're analyzing a dataset of customer information, and you want to identify the customers who are most likely to churn 
(i.e., stop doing business with the company). The dataset contains the following columns:
customer_id (unique identifier for each customer)
age (customer's age)
tenure (number of months the customer has been with the company)
monthly_spend (average monthly spend of the customer)
churn (binary indicator: 1 if the customer has churned, 0 otherwise)
Task
Train a simple logistic regression model to predict the probability of a customer churning based on their age, tenure, and monthly_spend.
 Then, use the model to identify the top 10 customers with the highest predicted probability of churning.
Assumptions
You can use a Python library like scikit-learn to train the logistic regression model.
You have a basic understanding of logistic regression and its assumptions.
Please respond with your approach and any relevant code or pseudo-code
(Note: I'll provide guidance and hints as needed, just like before!) """

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Split data into training and testing sets (30% for training)
train_data, test_data = train_test_split(df, test_size=0.3, random_state=42)

# Scale input features
scaler = StandardScaler()
train_data[['age', 'tenure', 'monthly_spend']] = scaler.fit_transform(train_data[['age', 'tenure', 'monthly_spend']])
test_data[['age', 'tenure', 'monthly_spend']] = scaler.transform(test_data[['age', 'tenure', 'monthly_spend']])

# Train logistic regression model
model = LogisticRegression()
model.fit(train_data[['age', 'tenure', 'monthly_spend']], train_data['churn'])

# Evaluate model performance on testing data
y_pred = model.predict(test_data[['age', 'tenure', 'monthly_spend']])
print("Accuracy:", accuracy_score(test_data['churn'], y_pred))
print("Classification Report:")
print(classification_report(test_data['churn'], y_pred))

# Predict probabilities for the testing data
y_result = model.predict_proba(test_data[['age', 'tenure', 'monthly_spend']])

# Get the probability of the positive class (churn=1)
prob_churn = y_result[:, 1]

# Sort by probability in descending order and get top 10
top_10 = test_data.iloc[prob_churn.argsort()[-10:]].copy()

# Add the predicted probability to the top 10 DataFrame
top_10['prob_churn'] = prob_churn[prob_churn.argsort()[-10:]]
