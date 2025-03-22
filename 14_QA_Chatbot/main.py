import google.generativeai as genai
from dotenv import load_dotenv
import chainlit as cl
import os

load_dotenv()

# gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

@cl.on_chat_start
async def handle_chat_start():
    # Send welcome message to user
    await cl.Message(content="Hello! how can I help you today?").send()



@cl.on_message
async def handle_message(message: cl.Message):

    prompt = message.content
    response = model.generate_content(prompt)
    response_text = response.text if hasattr(response, "text") else ""

    await cl.Message(content = response_text).send()
    

