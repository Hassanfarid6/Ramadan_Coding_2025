import streamlit as st
import random
import string


def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters    # Include all letters (A-Z, a-z)

    if use_digits:
        characters += string.digits        # Include digits (0-9)
    
    if use_special:
        characters += string.punctuation   # Include special characters (e.g., !, @, #, etc.)
    
    return "".join(random.choice(characters) for _ in range(length))


st.title("Password Generator")

length = st.slider("SelectPassword Length", min_value=6, max_value=30, value=12)
use_digits = st.checkbox("Include Numbers")
use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(
        length, use_digits, use_special
    )
    st.success(f"Generated Password: {password}")
