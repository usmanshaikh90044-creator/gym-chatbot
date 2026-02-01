# -------------------- IMPORTS --------------------
import pandas as pd
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -------------------- LOAD DATASET --------------------
df = pd.read_csv("megaGymDataset.csv")


# -------------------- COMBINE COLUMNS --------------------
df['combined_text'] = (
    "Exercise Name: " + df['Title'].astype(str) + ". " +
    "Description: " + df['Desc'].astype(str) + ". " +
    "Type: " + df['Type'].astype(str) + ". " +
    "Body Part: " + df['BodyPart'].astype(str) + ". " +
    "Equipment: " + df['Equipment'].astype(str) + ". " +
    "Difficulty Level: " + df['Level'].astype(str) + ". " +
    "Rating: " + df['Rating'].astype(str) + ". " +
    "Rating Details: " + df['RatingDesc'].astype(str)
)


# -------------------- CLEAN TEXT --------------------
def clean_text(text):
    text = text.lower()                    # lowercase
    text = re.sub(r'\s+', ' ', text)       # remove extra spaces
    text = text.strip()                    # trim edges
    return text

df['combined_text_clean'] = df['combined_text'].apply(clean_text)


# -------------------- TF-IDF VECTORIZATION --------------------
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined_text_clean'])


def format_chat_response(results_df):
    response = "Here are some exercises that match your request:\n\n"
    
    for idx, row in results_df.iterrows():
        response += f"🏋️ Exercise: {row['Title']}\n"
        response += f"• Body Part: {row['BodyPart']}\n"
        response += f"• Equipment: {row['Equipment']}\n"
        response += f"• Level: {row['Level']}\n"
        response += f"• Description: {row['Desc']}\n\n"
    
    return response

#creating a search function
def search_exercises(query, top_k=5):
    # Convert user query to TF-IDF vector
    query_vec = tfidf.transform([query])
    
    # Compute cosine similarity
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    
    # Get top-k most similar indices
    top_indices = similarities.argsort()[-top_k:][::-1]
    
    # Return matching rows
    return df.iloc[top_indices][
        ['Title', 'BodyPart', 'Equipment', 'Level', 'Desc']
    ]

import streamlit as st

# -------------------- STREAMLIT UI --------------------
st.set_page_config(page_title="Gym Chatbot 💪", layout="centered")

st.title("🏋️ Gym Exercise Chatbot")
st.write("Ask me about workouts, muscles, equipment, or difficulty levels.")

# User input
user_query = st.text_input(
    "Enter your workout query:",
    placeholder="e.g. beginner chest workout at home"
)

# Run search when user enters a query
if user_query:
    results = search_exercises(user_query)
    chat_response = format_chat_response(results)
    
    st.text(chat_response)

