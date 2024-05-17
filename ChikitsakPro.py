import streamlit as st
import os

def run_python_file(file_name):
    os.system(f"streamlit run {file_name}")

st.title("Welcome to Chikitsak Pro!")
st.write("Select a topic to explore:")

# Create clickable links for each category
if st.button("Detailed Prakriti Analysis"):
    run_python_file("prakriti.py")

if st.button("Ask Chikitsak Chatbot about Ayurveda"):
    run_python_file("chatbot.py")

if st.button("Ayurvedic Home Remedies"):
    run_python_file("remedies.py")
