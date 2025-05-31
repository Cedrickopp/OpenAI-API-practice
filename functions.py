from system_prompt import SYSTEM_PROMPT
from user_prompts import questions
from dotenv import load_dotenv
import os
import openai

# Load the environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# creating the client
client = openai.OpenAI()
model = "gpt-3.5-turbo"

# creating the conversation
conversation = [{"role": "system", "content": SYSTEM_PROMPT}]

def generate_response(questions):
    """
    This function generates a response for a given question using the OpenAI API
    
    Args:
        questions (list): A list of questions to generate responses for
        
    Returns:
        list: A list of responses
    """
    # Initialize conversation with system prompt
    conversation = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    for question in questions:
        # Add user question to conversation
        conversation.append({"role": "user", "content": str(question)})
        
        # Make API call with only the system prompt and current question
        current_messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": str(question)}
        ]
        
        response = client.chat.completions.create(
            model=model,
            messages=current_messages,
            temperature=1.0,
            max_tokens=100
        )
        
        # Add assistant's response to conversation
        conversation.append({"role": "assistant", "content": str(response.choices[0].message.content)})
    
    # Print the entire conversation
    for message in conversation:
        if message["role"] in ["user", "assistant"]:
            speaker = "User" if message["role"] == "user" else "Assistant"
            print(f"{speaker}: {message['content']}\n")