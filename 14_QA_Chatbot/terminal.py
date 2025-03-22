import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")


while True:
    user_input = input("Enter your question (or 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Thank you for using the chatbot!")
        break

    response = model.generate_content(user_input)
    print("Bot: ", response.text)
    
    

