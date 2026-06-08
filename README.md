# 🛍️ Amazon Fashion Sentiment Analysis

## Overview

This project is an end-to-end Sentiment Analysis system built using Amazon Fashion Reviews. The application predicts whether a customer review is **Positive**, **Negative**, or **Neutral** using Machine Learning techniques.

The project includes:

* Data Cleaning & Preprocessing
* NLP Pipeline
* TF-IDF Feature Engineering
* Model Training & Evaluation
* FastAPI Backend
* Streamlit Frontend

---

## Dataset

**Amazon Fashion Reviews Dataset**

* Approximately 2.3 Million customer reviews
* Fields used:

  * Rating
  * Title
  * Review Text
  * Verified Purchase
  * Helpful Votes

The dataset is not included in this repository due to its large size.

---

## Project Workflow

1. Data Cleaning
2. Text Preprocessing
3. Sentiment Label Creation
4. TF-IDF Vectorization
5. Model Training
6. Model Evaluation
7. API Development using FastAPI
8. Interactive UI using Streamlit

---

## Models Evaluated

| Model                   | Accuracy |
| ----------------------- | -------- |
| Multinomial Naive Bayes | 85%      |
| Logistic Regression     | 87%      |

**Final Selected Model:** Logistic Regression

---

## Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-Learn
* NLTK

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit

### Model Persistence

* Joblib

---

## Project Structure

```text
amazon-fashion-sentiment-analysis/
│
├── backend/
│   ├── app.py
│   ├── sentiment_model.pkl
│   └── tfidf.pkl
│
├── frontend/
│   └── streamlit_app.py
│
├── notebooks/
│   └── main.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd amazon-fashion-sentiment-analysis
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Backend

```bash
cd backend
uvicorn app:app --reload
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Running the Frontend

```bash
cd frontend
streamlit run streamlit_app.py
```

Application URL:

```text
http://localhost:8501
```

---

## Features

* Real-time sentiment prediction
* Confidence score display
* Interactive user interface
* FastAPI REST API
* Streamlit dashboard
* Trained Logistic Regression model
* Large-scale Amazon Fashion review dataset

---

## Sample Prediction

**Input Review**

```text
This dress fits perfectly and the quality is amazing.
```

**Prediction**

```text
Sentiment: Positive
Confidence: 97%
```

---

## Future Improvements

* Batch CSV Review Analysis
* Sentiment Distribution Dashboard
* Word Cloud Visualization
* BERT-based Sentiment Analysis
* Model Deployment on Cloud

---

## Author

Aniket

Machine Learning | NLP | FastAPI | Data Analytics
