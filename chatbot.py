import streamlit as st
import os
import google.generativeai as genai

# Initialize Gemini-Pro 
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Gemini uses 'model' for assistant; Streamlit uses 'assistant'
def role_to_streamlit(role):
  if role == "model":
    return "assistant"
  else:
    return role

# Add a Gemini Chat history object to Streamlit session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])

# Display Form Title
st.title("Ask Me Anything about Prakriti, Ayurveda, or Doshas!")

# Display chat messages from history above current input box
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Accept user's next message, add to context, resubmit context to Gemini
if prompt := st.chat_input("Ask me anything about Prakriti, Ayurveda, or Doshas"):
    # Display user's last message
    st.chat_message("user").markdown(prompt)
    
    # Check if the prompt is a greeting or related to Ayurveda
    if any(greeting in prompt.lower() for greeting in ["hello", "hi", "hey"]) or any(ayurveda_term in prompt.lower() for ayurveda_term in ["ayurveda", "prakriti", "doshas", "vata", "pitta", "kapha", "dosha", "ayurvedic", "medicines", "vatta", "pitta", "khapha"]):
        # Send user entry to Gemini and read the response
        response = st.session_state.chat.send_message(prompt) 
        
        # Display last 
        with st.chat_message("assistant"):
            st.markdown(response.text)
    else:
        with st.chat_message("assistant"):
            st.markdown("Sorry, I can only answer questions about Ayurveda and related terms.")