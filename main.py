import os
import json
import datetime
import streamlit as st
import random
import re

file_path = os.path.abspath("./intents.json")

def normalize_text(text):
    return re.sub(r'[^a-z0-9 ]', '', text.lower().strip())

def load_intents_json(file_path):
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump([], file)
        return {}
    
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            translations = {}
            for entry in data:
                if "English words" in entry and "French words" in entry:
                    english_sentence = normalize_text(entry["English words"].get("sentences", ""))
                    french_sentence = entry["French words"].get("sentences", "")
                    if english_sentence and french_sentence:
                        translations.setdefault(english_sentence, []).append(french_sentence)
            return translations
        except json.JSONDecodeError:
            return {}

intents = load_intents_json(file_path)

def translate_text(user_input):
    normalized_input = normalize_text(user_input)
    translations = intents.get(normalized_input, [])
    return random.choice(translations) if translations else "Translation not found."

def chatbot(user_input):
    try:
        return translate_text(user_input)
    except Exception as e:
        return f"Sorry, I couldn't process that. Error: {e}"

# Streamlit UI
def main():
    st.title("Language Translator Bot")

    menu = ["Home", "Translation History", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.write("Welcome! Type an English sentence below to get the French translation.")

        user_input = st.text_input("Enter text in English:")

        if user_input:
            response = chatbot(user_input)
            st.text_area("Translation (French):", value=response, height=120)

            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(file_path, 'r+', encoding='utf-8') as file:
                try:
                    log_data = json.load(file)
                except json.JSONDecodeError:
                    log_data = []
                log_data.append({"English": user_input, "French": response, "Timestamp": timestamp})
                file.seek(0)
                json.dump(log_data, file, indent=4)

    elif choice == "Translation History":
        st.header("Translation History")
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    log_data = json.load(file)
                    for entry in log_data:
                        if "English" in entry and "French" in entry:
                            st.text(f"English: {entry['English']}")
                            st.text(f"French: {entry['French']}")
                            st.text(f"Timestamp: {entry['Timestamp']}")
                            st.markdown("---")
                except json.JSONDecodeError:
                    st.write("Error reading translation history.")
        else:
            st.write("No translation history found.")

    elif choice == "About":
        st.write("This chatbot translates English text into French using a JSON-based lookup.")
        st.subheader("Features:")
        st.write("""
        1. Direct lookup from JSON for fast and accurate translations.
        2. Interactive web interface using Streamlit.
        """)

if __name__ == '__main__':
    main()
