import streamlit as st
import random
import time


st.title("📝 Quiz Application")

# Define quiz questions, options, and answer in the form of a list of dictionaries
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"],
        "answer": "Islamabad",
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": [
            "Allama Iqbal",
            "Liaquat Ali Khan",
            "Muhammad Ali Jinnah",
            "Benazir Bhutto",
        ],
        "answer": "Muhammad Ali Jinnah",
    },
    {
        "question": "Which is the national language of Pakistan?",
        "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
        "answer": "Urdu",
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Taka", "Riyal"],
        "answer": "Rupee",
    },
    {
        "question": "Which city is known as the City of Lights in Pakistan?",
        "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"],
        "answer": "Karachi",
    },
    {
        "question": "Which is the national animal of Pakistan?",
        "options": ["Markhor", "Lion", "Elephant", "Tiger"],
        "answer": "Markhor"
    },
    {
        "question": "Which is the highest mountain in Pakistan?",
        "options": ["K2", "Nanga Parbat", "Mount Everest", "Rakaposhi"],
        "answer": "K2"
    },
    {
        "question": "Which river is the longest in Pakistan?",
        "options": ["Chenab", "Ravi", "Indus", "Jhelum"],
        "answer": "Indus"
    },
    {
        "question": "What is the national sport of Pakistan?",
        "options": ["Cricket", "Football", "Hockey", "Squash"],
        "answer": "Hockey"
    },
    {
        "question": "Which city is known as the Heart of Pakistan?",
        "options": ["Islamabad", "Lahore", "Karachi", "Multan"],
        "answer": "Lahore"
    },
    {
        "question": "Which dam is the largest in Pakistan?",
        "options": ["Tarbela Dam", "Mangla Dam", "Warsak Dam", "Diamer-Bhasha Dam"],
        "answer": "Tarbela Dam"
    },
    {
        "question": "Which Pakistani scientist won the Nobel Prize in Physics?",
        "options": ["Abdus Salam", "Dr. Abdul Qadeer Khan", "Ishfaq Ahmad", "Salimuzzaman Siddiqui"],
        "answer": "Abdus Salam"
    },
    {
        "question": "What is the total number of provinces in Pakistan?",
        "options": ["2", "3", "4", "5"],
        "answer": "4"
    }
]

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question
st.subheader(question["question"])

selected_option = st.radio("Select your answer", question["options"], key= "answer")

if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct Answer!")
        st.balloons()
    else:
        st.error("❌ Incorrect! the correct answer is " + question["answer"])

    time.sleep(3)
    st.session_state.current_question = random.choice(questions)
    
    st.rerun()