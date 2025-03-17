**Language Translator Bot**

## Introduction
The Language Translator Bot is a simple English-to-French translation tool built using Python and Streamlit. It utilizes a JSON-based lookup system to provide translations and maintains a translation history.

## Features
- Direct lookup from JSON for fast and accurate translations.
- User-friendly interface with Streamlit.
- Maintains translation history with timestamps.
- Error handling for missing translations.

## Installation
1. Clone the repository:
   ```sh
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```sh
   cd language-translator-bot
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   streamlit run app.py
   ```

## Implementation Details

### Dependencies
- Python
- Streamlit
- JSON
- OS Module
- Regex
- Datetime
- Random

### Code Overview

#### 1. **Loading Translation Data**
- The bot loads translations from `intents.json`.
- If the file does not exist or is empty, it initializes an empty JSON structure.
- Normalizes input text to ensure consistency.
- Translations are stored in a dictionary format for fast retrieval.

#### 2. **Translation Functionality**
- The `translate_text()` function retrieves the French translation based on the normalized English input.
- If no translation is found, it returns "Translation not found."

#### 3. **Chatbot Functionality**
- The chatbot function interacts with users and provides translations.
- Handles exceptions to ensure a smooth user experience.

#### 4. **User Interface (Streamlit)**
- Provides a sidebar menu with three options: `Home`, `Translation History`, and `About`.
- `Home` allows users to input English text and receive translations.
- `Translation History` displays previous translations along with timestamps.
- `About` provides details about the bot and its features.

#### 5. **Translation History**
- Stores user input, translated output, and timestamp in `intents.json`.
- Displays past translations in the `Translation History` section.

## License
This project is licensed under the MIT License.

