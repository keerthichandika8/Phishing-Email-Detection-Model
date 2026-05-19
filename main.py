import pandas as pd
import pickle
import re
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# -----------------------------
# Load Dataset
# -----------------------------
data = pd.read_csv("dataset/phishing_emails.csv")

# Rename columns
data.columns = ['label', 'email_text']

# Convert labels into numbers
data['label'] = data['label'].map({
    'phishing': 1,
    'safe': 0
})

# Remove null values
data = data.dropna()

# Features and Target
X = data['email_text']
y = data['label']

# -----------------------------
# Convert Text to Numerical Data
# -----------------------------
vectorizer = TfidfVectorizer(stop_words='english')

X_vectorized = vectorizer.fit_transform(X)

# -----------------------------
# Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
model = MultinomialNB()

model.fit(X_train, y_train)

# -----------------------------
# Test Model
# -----------------------------
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# -----------------------------
# Save Model
# -----------------------------
pickle.dump(model, open("models/phishing_model.pkl", "wb"))

print("\nModel saved successfully!")

# -----------------------------
# URL Analysis Function
# -----------------------------
def analyze_url(text):

    safe_domains = [
        "google.com",
        "amazon.in",
        "microsoft.com",
        "github.com"
    ]

    url_pattern = r'https?://\S+|www\.\S+'

    urls = re.findall(url_pattern, text)

    if not urls:
        print("\nNo URL Detected")
        return

    for url in urls:

        trusted = False

        for domain in safe_domains:

            if domain in url:
                trusted = True
                break

        if trusted:
            print("\nTrusted URL Detected!")
        else:
            print("\nSuspicious URL Detected!")

# -----------------------------
# Runtime Email Input
# -----------------------------
user_email = input("\nEnter Email Content: ")

# Analyze URL
analyze_url(user_email)

# Convert Input Email
sample = [user_email]

sample_vector = vectorizer.transform(sample)

# Predict
prediction = model.predict(sample_vector)

# Prediction Probabilities
probabilities = model.predict_proba(sample_vector)[0]

safe_prob = probabilities[0] * 100
phishing_prob = probabilities[1] * 100

# -----------------------------
# Prediction Result
# -----------------------------
if prediction[0] == 1:
    print("\nPrediction: Phishing Email")
else:
    print("\nPrediction: Safe Email")

print(f"\nSafe Probability: {safe_prob:.2f}%")
print(f"Phishing Probability: {phishing_prob:.2f}%")

# -----------------------------
# Dynamic Probability Graph
# -----------------------------
labels = ['Safe', 'Phishing']
values = [safe_prob, phishing_prob]

plt.figure(figsize=(6, 4))

plt.bar(labels, values)

plt.ylabel("Probability (%)")
plt.title("Email Classification Probability")

plt.ylim(0, 100)

plt.show()

plt.close()