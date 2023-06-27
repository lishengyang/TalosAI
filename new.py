import os
import openai

# Set OpenAI API key from environment variable
openai.api_key = "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"

def ask_GPT(system_message, prompt):
    # Construct message array
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt},  # User message
    ]
    
    # Call OpenAI ChatCompletion API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # gpt-3.5-turbo or gpt-4
        messages=messages,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=1
    )
    
    # Return response text
    return response['choices'][0]['message']['content']
    
# Example usage
system_message = "You are an expert"
prompt = "tell me one joke"
response = ask_GPT(system_message, prompt) 
print(response)
