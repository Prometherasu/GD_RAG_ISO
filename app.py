# app.py
import streamlit as st
import requests

st.title("Chat avec Falcon-7B (vLLM)")

user_input = st.text_input("Entrez votre question :")

if st.button("Envoyer"):
    if user_input:
        response = requests.post(
            "http://localhost:8000/v1/chat/completions",
            headers={"Content-Type": "application/json"},
            json={
                "model": "falcon",  # ce nom peut varier selon ce que vLLM retourne
                "messages": [
                    {"role": "user", "content": user_input}
                ],
                "temperature": 0.7
            }
        )

        if response.ok:
            result = response.json()
            message = result["choices"][0]["message"]["content"]
            st.markdown(f"**Falcon :** {message}")
        else:
            st.error(f"Erreur : {response.status_code} - {response.text}")

