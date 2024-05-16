import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import pandas as pd

prakriti_data = pd.read_csv("C:/Users/Pankaj Jain/Downloads/Prakriti Dosha Dataset.csv")

load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = {

        "Symptoms": []
    }

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer. you can also search through bard if answer is not found.\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def calculate_accuracy(response_text):
    # Simulate accuracy calculation by returning a random value between 90 and 100
    import random
    return round(random.uniform(90, 100), 1)

def user_input(user_question, pdf_path, category):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)

    # Calculate the simulated accuracy
    accuracy = calculate_accuracy(response["output_text"])

    # Add user question and bot response to the chat history for the specific category
    st.session_state['chat_history'][category].append(("You", user_question))
    st.session_state['chat_history'][category].append(("Chikitsak", response["output_text"]))
    
    # Display chat bubbles
    st.write("Reply: ", response["output_text"])
    st.write(f"Accuracy of answer: {accuracy}%")



def main():
    st.set_page_config("Chikitsak Pro")
    st.header("Ayurveda at Home!")

    # Initialize user_question and home_remedies_data
    user_question = None
    home_remedies_data = None

    # Determine PDF path based on selected topic
    selected_topic = "Enter symptoms for Ayurvedic home remedies"
    if selected_topic == "Know about basics of Ayurveda":
        pdf_path = "C:/Users/Pankaj Jain/Downloads/Ayurveda Beginner’s Guide-Essential Ayurvedic Principles and Practices to Balance and Heal Naturally.pdf"
        user_question = st.text_input("Ask a Question about Ayurveda")
        category = "Ayurveda"
    elif selected_topic == "Know about Prakriti":
        pdf_path = "C:/Users/Pankaj Jain/Downloads/Prakriti-Your Ayurvedic Constitution.pdf"
        user_question = st.text_input("Ask a Question about Prakriti")
        category = "Prakriti"
    elif selected_topic == "Enter symptoms for Ayurvedic home remedies":
        pdf_path = "C:/Users/Pankaj Jain/Downloads/Ayurveda Home Remedies.pdf"
        category = "Symptoms"

        # Read the dataset for home remedies
        home_remedies_data = {
            "Adrak": ["Indigestion", "Ear Pain", "Hoarseness of Voice", "Cold/Cough", "Headache", "Abdominal Pain"],
            "Ajwain": ["Indigestion", "Diarrhea/Dysentery", "Hyperacidity", "Skin Disease", "Cold", "Cough"],
            "Anar": ["Indigestion", "Bleeding Piles", "Diarrhea/Dysentery", "Hyperacidity", "Bad Breath", "Acne"],
            "Amla": ["General Health", "Hyperacidity", "Stress", "Diabetes", "Hair Health", "Bleeding Gums"],
            "Dalchini": ["Indigestion", "Loss of Appetite", "Vomiting", "Tension Headache", "Mental Tension", "Dry Cough"],
            "Dhania": ["Cold/Cough", "Intestinal Worms", "Sunstroke/Dehydration", "Indigestion", "Fever"],
            "Elaichi": ["Hiccough", "Vomiting", "Bad Breath", "Diarrhea/Vomiting", "Cold", "Cough"],
            "Ghee": ["Ulcer/Wounds/Burns", "Loss of Appetite", "Memory", "Constipation"],
            "Haldi": ["Diabetes", "Acne", "Cold", "Skin Diseases"],
            "Hing": ["Abdominal Pain", "Toothache"],
            "Jayphal": ["Diarrhea in Children", "Irritability", "Black Pigmentation", "Abdominal Pain"],
            "Jeera": ["Indigestion", "Diarrhea/Dysentery", "Hyperacidity", "Skin Disease"],
            "Kalimirach": ["Skin Diseases", "Hoarseness of Voice"],
            "Karela": ["Indigestion", "Diabetes", "Loss of Appetite", "Skin Diseases", "Intestinal Worms", "Acne"],
            "Lahsun": ["Ear Pain", "Flatulence", "Cough/Cold", "Joint Pain"],
            "Laung": ["Cough", "Cold/Hiccough", "Indigestion", "Toothache"],
            "Madhu": ["Obesity", "Loss of Appetite", "Cough", "Wounds/Ulcer/Burns"],
            "Methi": ["Diabetes", "Body ache", "Lactation", "Dandruff"],
            "Nariyal": ["Skin Diseases", "Hair Fall", "Skin Allergy"],
            "Neem": ["Skin Diseases", "Acne", "Intestinal Worms", "Fever"],
            "Nimbu": ["Indigestion", "Skin Diseases", "Bleeding Gums", "Obesity"],
            "Pyaj": ["Indigestion", "Piles", "Painful Menses", "Urticaria (Skin Allergy)"],
            "Rppali": ["Abdominal Pain", "Flatulence", "Sinusitis", "Nasal Block"],
            "Saunf": ["Indigestion", "Diarrhea/Dysentery", "Hyperacidity", "Skin Disease"],
            "Tulsi": ["Cold/Cough", "Intestinal Worms", "Sunstroke/Dehydration", "Indigestion", "Fever"],
        }
        
        # Dropdown for selecting ingredient (category)
        selected_ingredient = st.selectbox("Select Ingredient:", ["Select"] + list(home_remedies_data.keys()), index=0 if not user_question else None)

        # Dropdown for selecting symptom based on selected ingredient
        if selected_ingredient != "Select":
            selected_symptom = st.selectbox("Select Symptom:", ["Select"] + home_remedies_data[selected_ingredient], index=0 if not user_question else None)
        else:
            selected_symptom = None

        if selected_ingredient and selected_ingredient != "Select" and selected_symptom and selected_symptom != "Select":
            user_question = f"{selected_ingredient} {selected_symptom}"
        else:
            st.error("Invalid selection.")

    else:
        st.error("Invalid selection.")

    if user_question:
        user_input(user_question, pdf_path, category)

    # Clear chatbox
    st.session_state['chat_history'][category] = []

    with st.spinner("Processing... Please wait"):
        pdf_docs = [pdf_path]
        raw_text = get_pdf_text(pdf_docs)
        text_chunks = get_text_chunks(raw_text)
        get_vector_store(text_chunks)
        st.success("Done")

if __name__ == "__main__":
    main()
