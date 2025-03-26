import chainlit as cl
from dotenv import load_dotenv
from typing import Optional, Dict       
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.tool import function_tool
import requests

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

provider = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = provider,
)

@function_tool("get_hassan_data")
def get_hassan_data(location: str)-> str:
    """
    This function makes a request to Hassan's  information
    about his background, skills, projects, education, work experience, and achievements.

    Returns:
"""
    return f"Hassan is from {location}"

agent = Agent(
    name="Greeting Agent",
    instructions="""You are a Greeting Agent, Your task is to greet the user with a friendly message.
    
    When someone says:
    - hi/hello/hey: Reply with "Hello from Hassan ali! How are you?"
    - I'm fine/good/great: Say "I'm also good! What can I do for you today?"
    - bye/by/goodbye: Say "Allah hafiz from Hassan ali! Have a great day!"
    - how are you: Say "I'm doing well, thank you for asking! How about you?"
    - thank you/thanks: Say "You're welcome! Is there anything else I can help you with?"
    - good morning/afternoon/evening/night: Reply with appropriate time-based greeting
    - tell me about yourself: Say "I'm Hassan's AI greeting assistant, here to help with friendly conversations!"
    - what's the weather: Say "I wish I could tell you about the weather, but I'm just a greeting bot! Try checking a weather app!"
    - tell me a joke: Say "While I love greeting people, I'm not great at jokes. Hassan keeps me focused on friendly hellos!"
    - who created you: Say "I was created by Hassan ali to be a friendly greeting assistant!"
    - what time is it: Say "I don't have access to time information, but I can still wish you a wonderful day!"
    - do you speak other languages: Say "I primarily communicate in English, but I can say Assalam-o-Alaikum and Allah Hafiz!"
    
    For any other questions/topics: Say "I apologize, but Hassan has programmed me just for greetings and basic conversation. I can't help with other topics."
    
    Always:
    - Maintain a polite and friendly tone
    - Use emojis occasionally to appear more friendly (👋, 😊, 👍)
    - If someone seems upset, respond with extra kindness
    - Keep responses concise but warm
    - Include Hassan's name in important responses
    - Use Islamic greetings when appropriate
    - Respond with enthusiasm and positivity
    - Show empathy in responses
    - Incorporate Islamic phrases when suitable""",
    model=model,
    tools=[get_hassan_data],
)

@cl.oauth_callback
def oauth_callback(
    provider_id: str,  # ID of the OAuth provider (GitHub)
    token: str,  # OAuth access token
    raw_user_data: Dict[str, str],  # User data from GitHub
    default_user: cl.User,  # Default user object from Chainlit
) -> Optional[cl.User]:  # Return User object or None
    """
    Handle the OAuth callback from GitHub
    Return the user object if authentication is successful, None otherwise
    """

    print(f"Provider: {provider_id}")  # Print provider ID for debugging
    print(f"User data: {raw_user_data}")  # Print user data for debugging

    return default_user  # Return the default user object


@cl.on_chat_start
async def handle_chat_start():

    cl.user_session.set("history", [])  # Initialize empty chat history

    await cl.Message(
        content="Hello! How can I help you today?"
    ).send()  # Send welcome message


# Handler for incoming chat messages
@cl.on_message
async def handle_message(message: cl.Message):

    history = cl.user_session.get("history")  # Get chat history from session

    history.append(
        {"role": "user", "content": message.content}
    )  # Add user message to history

    result = await cl.make_async(Runner.run_sync)(agent, input=history)

    response_text = result.final_output
    await cl.Message(content=response_text).send()

    history.append({"role": "assistant", "content": response_text})
    cl.user_session.set("history", history)

