import streamlit as st
import random
import requests
import time



st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 100)

st.subheader("Instant Cash Generator")

if st.button("Generator Money"):
    st.write("counting your money...")
    time.sleep(2)
    amount = generate_money()
    st.success(f"You made ${amount}!")


def fetch_side_hustle():
    try:
        response = requests.get("https://fastapi-api.vercel.app/side_hustles")
        if response.status_code == 200:  # If request successful
            hustles = response.json()  # Convert response to JSON
            return hustles["side_hustle"]
        else:
            return "freelancing"
    except :
        st.info(f"Something went wrong!")

st.subheader("Side Hustle Ideas")

if st.button("show Hustle ideas"):
    idea =  fetch_side_hustle()
    st.success(idea)



def fetch_money_quotes():
    try:
        response = requests.get("https://fastapi-api.vercel.app/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quote"]
        else:
            return "Money is the root of all evil!"
    except:
        return "Something went wrong!"
    


st.subheader("Money-Making Motivation")
if st.button("Get Inspired"):
    quote = fetch_money_quotes()
    st.success(quote)       

