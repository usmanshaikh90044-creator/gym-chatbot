# gym-chatbot
# 🏋️ Gym Exercise Chatbot

An NLP-powered fitness chatbot that recommends gym and home workout exercises based on natural language user queries. The application uses TF-IDF and cosine similarity to match user input with the most relevant exercises and is deployed publicly using Streamlit Cloud.

---

## 🚀 Live Demo
🔗 **https://gym-chatbot-fzbbhk25dgu9jyzembwscr.streamlit.app/**

---


---

## 🧠 Project Overview

The Gym Exercise Chatbot allows users to ask questions such as:
- *“beginner chest workout at home”*
- *“tricep exercises with dumbbells”*
- *“advanced back workouts”*

Based on the query, the chatbot returns a ranked list of exercises with details like:
- Targeted body part  
- Required equipment  
- Difficulty level  
- Exercise description  

The system is built using classic NLP techniques and does **not rely on large language models**, making it fast, lightweight, and explainable.

---

## ⚙️ How It Works

1. **Data Preparation**
   - Exercise metadata is combined into a single text field.
   - Text is cleaned (lowercasing, whitespace normalization).

2. **Vectorization**
   - TF-IDF is used to convert exercise descriptions into numerical vectors.

3. **Similarity Matching**
   - User queries are vectorized using the same TF-IDF model.
   - Cosine similarity is computed to find the most relevant exercises.

4. **Response Formatting**
   - Results are formatted into a clean, chat-style response.

5. **Deployment**
   - The application is deployed using Streamlit Cloud for public access.

---

## 🛠️ Tech Stack

- **Python**
- **Pandas** – data manipulation
- **scikit-learn** – TF-IDF & cosine similarity
- **Streamlit** – web interface & deployment
- **NLP (TF-IDF based search)**

---

## 📂 Project Structure
gym-chatbot/
│
├── app.py # Streamlit application
├── megaGymDataset.csv # Exercise dataset
├── Fitness_chatbot.ipynb # Development notebook
├── requirements.txt # Project dependencies
├── README.md # Project documentation
└── screenshot.png # App screenshot



---

## ▶️ Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/usmanshaikh90044-creator/gym-chatbot.git
   cd gym-chatbot

2.pip install -r requirements.txt

3.streamlit run app.py

