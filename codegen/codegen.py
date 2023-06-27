import os
import openai
import re

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

def extract_code(response):
    # Extract code block from response using regex
    code_block = re.findall(r'```python([\s\S]*?)```', response)

    if code_block:
        return code_block[0].strip()
    else:
        return None

def save_code_to_file(code, filename):
    with open(filename, 'w') as f:
        f.write(code)

# Example usage
system_message = "You are an very helpful assistant"
prompt = "i am building a code demo for testing uart on my arm board which is the raspberry pi 4,show me the code"
response = ask_GPT(system_message, prompt)
print(response)

code = extract_code(response)

if code:
    filename = "generated_code.py"
    save_code_to_file(code, filename)
    print(f"Code saved to {filename}")
else:
    print("No code block found in the response.")

