# Phishing Email Detection Model

## Overview
The Phishing Email Detection Model is a Machine Learning based cybersecurity project developed using Python and Scikit-learn. The main objective of this project is to detect whether an email is a phishing email or a legitimate safe email by analyzing textual content, suspicious keywords, and URLs.

Phishing emails are commonly used by attackers to steal sensitive information such as usernames, passwords, banking credentials, and personal data. This project helps in identifying such malicious emails using Natural Language Processing (NLP) and Machine Learning techniques.

---

## Features
- Train the model using phishing and safe email datasets
- Analyze email textual content
- Detect suspicious and trusted URLs
- Extract important keywords using TF-IDF Vectorization
- Classify emails as:
  - Phishing Email
  - Safe Email
- Display model accuracy
- Generate confusion matrix
- Show classification probabilities using graphs
- Runtime email input prediction
- Save trained Machine Learning model

---

## Technologies Used
- Python
- Pandas
- Scikit-learn
- NumPy
- Matplotlib
- Seaborn
- Regular Expressions (Regex)

---

## Machine Learning Concepts Used

### 1. TF-IDF Vectorization
TF-IDF converts email text into numerical vectors so that Machine Learning algorithms can process textual data effectively.

### 2. Naive Bayes Algorithm
The Multinomial Naive Bayes algorithm is used for classification. It predicts whether an email is phishing or safe based on learned patterns from the dataset.

### 3. NLP (Natural Language Processing)
The project uses NLP techniques to analyze suspicious words, email content, and URL patterns.

---

## Dataset

The dataset contains:
- Phishing emails
- Legitimate safe emails
- Suspicious URLs
- Trusted URLs

### Example Phishing Keywords
- verify
- urgent
- click here
- password reset
- security alert

### Example Safe Keywords
- meeting
- project
- schedule
- report

---

## Project Workflow

### Step 1: Load Dataset
The CSV dataset containing phishing and safe emails is loaded using Pandas.

### Step 2: Data Preprocessing
- Remove null values
- Convert labels into numerical format
- Extract email content

### Step 3: Feature Extraction
TF-IDF Vectorization converts text into numerical features.

### Step 4: Train Machine Learning Model
The Naive Bayes classifier is trained using the processed dataset.

### Step 5: Evaluate Model
The project displays:
- Accuracy
- Confusion Matrix
- Classification Report

### Step 6: Runtime Email Prediction
Users can enter custom email content during runtime to test whether the email is phishing or safe.

### Step 7: URL Analysis
The system checks whether URLs are:
- Trusted URLs
- Suspicious URLs

### Step 8: Probability Visualization
A probability graph is displayed showing the likelihood of an email being phishing or safe.

---

## Folder Structure

```text
phishing-email-detector/
│
├── dataset/
│   └── phishing_emails.csv
│
├── models/
│   └── phishing_model.pkl
│
├── screenshots/
│   ├── accuracy_output.png
│   ├── phishing_prediction.png
│   ├── safe_prediction.png
│   ├── graph_output.png
│   └── folder_structure.png
│
├── phishing_detector.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone YOUR_REPOSITORY_LINK
```

### Navigate to Project Folder

```bash
cd phishing-email-detector
```

### Install Required Libraries

```bash
pip install pandas scikit-learn numpy matplotlib seaborn
```

---

## Run the Project

```bash
python phishing_detector.py
```

---

## Example Runtime Input

### Example 1

#### Input

```text
Verify your bank account immediately http://fakebank-login.com
```

#### Output

```text
Suspicious URL Detected!
Prediction: Phishing Email
```

---

### Example 2

#### Input

```text
Visit https://www.google.com
```

#### Output

```text
Trusted URL Detected!
Prediction: Safe Email
```

---

## Output Screens

The project generates:
- Accuracy output
- Classification report
- Confusion matrix
- Runtime predictions
- Probability graphs

---

## Future Improvements
- Large real-world email datasets
- Deep Learning integration
- Real-time email scanning
- Flask web application
- Email attachment analysis
- Advanced URL reputation analysis

---

## Applications
- Email security systems
- Spam filtering
- Banking security
- Enterprise cybersecurity
- Threat detection systems

---

## Screenshots

### 1. Accuracy and Classification Report
This output shows the model accuracy, confusion matrix, and classification report generated after testing the Machine Learning model.

![Accuracy Output](screenshots/accuracy_output.png)

---

### 2. Phishing Email Prediction
This screenshot demonstrates the detection of a phishing email containing suspicious keywords and malicious URLs.

![Phishing Prediction](screenshots/phishing_prediction.png)

---

### 3. Safe Email Prediction
This screenshot demonstrates the detection of a legitimate safe email containing trusted URLs.

![Safe Prediction](screenshots/safe_prediction.png)

---

### 4. Probability Graph
This graph displays the probability of an email being classified as phishing or safe.

![Probability Graph](screenshots/graph_output.png)

---

### 5. Project Folder Structure
This screenshot shows the overall folder structure and organization of the project files.

![Folder Structure](screenshots/folder_structure.png)

---

## Conclusion

This project successfully demonstrates how Machine Learning and NLP techniques can be used to detect phishing emails based on textual content and URL analysis. The system classifies emails as phishing or safe with high accuracy and provides graphical visualization for better understanding.

---

## Author
Hansika Allamsetty
