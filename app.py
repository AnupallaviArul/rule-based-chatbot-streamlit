import streamlit as st
import nltk
import random
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download tokenizer (runs once)
nltk.download('punkt')

# Initialize stemmer
stemmer = PorterStemmer()

# Intent data
intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey"],
        "responses": ["Hello!", "Hi there!", "Hey!"]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you"],
        "responses": ["Goodbye!", "See you later!", "Take care!"]
    },
    "thanks": {
        "patterns": ["thanks", "thank you"],
        "responses": ["You're welcome!", "No problem!", "Anytime!"]
    }
}

# Chatbot logic
def chatbot_response(user_input):
    tokens = word_tokenize(user_input.lower())
    stemmed_tokens = [stemmer.stem(word) for word in tokens]

    for intent, data in intents.items():
        for pattern in data["patterns"]:
            pattern_stem = stemmer.stem(pattern.split()[0])
            if pattern_stem in stemmed_tokens:
                return random.choice(data["responses"])

    return "I'm sorry, I didn't understand that."

# ---------------- STREAMLIT UI ---------------- #

st.set_page_config(page_title="Simple Chatbot", page_icon="🤖")

st.title("🤖 Simple Rule-Based Chatbot")
st.write("This chatbot uses NLTK, stemming, and intent matching.")

# User input
user_input = st.text_input("You:", placeholder="Type your message here...")

# Button
if st.button("Send"):
    if user_input.strip() != "":
        response = chatbot_response(user_input)
        st.markdown(f"**Bot:** {response}")
    else:
        st.warning("Please enter a message.")