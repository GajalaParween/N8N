import streamlit as st
import requests

WEBHOOK_URL = "https://innogajala.app.n8n.cloud/webhook-test/dbf7282d-560e-46fc-bd0e-d6231e5e2b97"   # paste your webhook URL

st.title("Language Translation")

text = st.text_area("Enter text to translate")

languages = [ "Hindi", "English", "Bengali", "Telugu", "Marathi", "Tamil", "Urdu", "Gujarati", "Kannada",
    "Odia", "Malayalam", "Punjabi", "Assamese", "Maithili", "Santali",

    "French", "Spanish", "German", "Chinese", "Japanese", "Korean",
    "Russian", "Portuguese", "Arabic", "Italian", "Turkish", "Dutch",
    "Swedish", "Polish", "Danish", "Finnish", "Norwegian"]

option = st.selectbox("Select language", languages)

if st.button("Submit"):
    payload = {
        "input": text,
        "language": option
    }

    response = requests.post(WEBHOOK_URL, json=payload)
    result = response.json()

    st.write("Translated Output:", result[0]["output"])
