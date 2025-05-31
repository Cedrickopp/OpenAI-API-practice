from functions import generate_response
from user_prompts import questions

# Call the OpenAI API with the questions defined in user_prompts.py
responses = generate_response(questions)

#print the returned responses
print(responses)
