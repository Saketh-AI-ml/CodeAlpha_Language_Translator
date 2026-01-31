import streamlit as st
from deep_translator import GoogleTranslator

# Page title
st.set_page_config(page_title="Language Translator")

st.title("🌍 Language Translation Tool")

# User input
text = st.text_area("Enter text to translate")

# Language options
languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "French": "fr",
    "German": "de"
}

source_lang = st.selectbox("Source Language", languages.keys())
target_lang = st.selectbox("Target Language", languages.keys())

# Translate button
if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        translated_text = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("Translated Text:")
        st.write(translated_text)
