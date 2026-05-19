import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
data = pd.read_csv("dataset.csv")

# Features and labels
x = data["email"]
y = data["label"]

# Convert text into numerical data
vectorizer = CountVectorizer()

x_vector = vectorizer.fit_transform(x)

# Split dataset
x_train, x_test, y_train, y_test = train_test_split(
    x_vector, y, test_size=0.3, random_state=42
)

# Train model
model = MultinomialNB()

model.fit(x_train, y_train)

# Predictions
y_pred = model.predict(x_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Test custom email
email = ["Verify your password immediately"]

email_vector = vectorizer.transform(email)

prediction = model.predict(email_vector)

print("\nEmail Prediction:", prediction[0])