import streamlit as st
import pandas as pd
import datetime
import csv
import os


MOOD_FILE = "mood_log.csv"

def load_mood_data ():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    return pd.read_csv(MOOD_FILE)


def save_mood_data():
    
    with open(MOOD_FILE, "a") as file:
        writer = csv.writer(file)
        writer.writerow([data, mood])

st.title("Mood Tracker")

today = datetime.date.today()

st.subheader("How are you feeling today?")

mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Neutral"])

if st.button("log Mood"):

    save_mood_data(today, mood)
    st.success("Mood logged successfully!")





