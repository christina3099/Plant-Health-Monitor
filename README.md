# 🌱 Plant Health Diagnosis & AI Care Recommendation System

## Deep Learning + LLM-Powered Plant Care Assistant

This project is an end-to-end AI system that diagnoses plant leaf conditions from images and generates personalized care recommendations using a Large Language Model (LLM).It is designed as a small-scale version of real-world agriculture-health AI systems.

##  Features
### 1. Plant Disease Classification (CNN Model)

Classifies plant leaf images into:
- Healthy
- Rusty
- Powdery

Built using TensorFlow/Keras
Uses augmentation & normalization for improved generalization
Trained on Kaggle dataset

###  2. FastAPI Inference Backend

Accepts image uploads (/predict)
Runs preprocessing + model inference
Returns:
- Predicted class
- Confidence score

### 3. LLM-based Plant Care Suggestions (In Progress)

Integrates GPT to generate:
- Treatment steps
- Watering schedule
- Preventive measures
- Nutrient recommendations

### 4. Frontend Web App (In Progress)

Built with Streamlit
Allows drag-and-drop image upload
Shows model prediction + AI-generated recommendations

## Tech Stack

| Layer          | Technology                                   |
| -------------- | -------------------------------------------- |
| Model Training | Python, TensorFlow, Keras, NumPy, Matplotlib |
| Serving        | FastAPI, Uvicorn                             |
| Deployment     | Docker, Azure/GCP (Upcoming)                 |
| Frontend       | React.js (In Progress)                       |
| AI Reasoning   | GPT API (In Progress)                        |


## 📂 Project Structure

<img width="578" height="336" alt="image" src="https://github.com/user-attachments/assets/2ab6e66c-002b-43ba-a0ca-a5d505c899f5" />

## 📦 Installation
### 1. Clone the repository

git clone https://github.com/<your-username>/plant-health-ai.git
cd plant-health-ai

### 2. Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

### 3. Install dependencies

pip install -r requirements.txt

### 4. Running the FastAPI Server

Start the API:
uvicorn api.main:app --reload

Access the API Docs:
http://127.0.0.1:8000/docs

### Example Prediction (API)

Send a POST request:

curl -X POST "http://127.0.0.1:8000/predict" \
  -F "file=@leaf.jpg"

Response:
{
  "prediction": "Rusty",
  "confidence": 97%
}


## 🔜 Upcoming Enhancements

 - Add LLM-based care recommendation module
 - Deploy FastAPI with Docker
 - Launch frontend UI
 - Add user authentication
 - GPU training pipeline

 ## 📘 Dataset

Kaggle Plant Disease Dataset
(Healthy, Rusty, Powdery classes)
Dataset not included in repo due to size. 

## 📄 License

MIT License
