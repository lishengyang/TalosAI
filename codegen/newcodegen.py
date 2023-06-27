import os
import openai
import re
import threading
import queue

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

def extract_code(response, code_queue):
    # Extract code block from response using regex
    code_block = re.findall(r'```python([\s\S]*?)```', response)

    if code_block:
        code_queue.put(code_block[0].strip())
    else:
        code_queue.put(None)

def save_code_to_file(code_queue, filename_queue):
    code = code_queue.get()
    filename = filename_queue.get()

    if code:
        with open(filename, 'w') as f:
            f.write(code)
        print(f"Code saved to {filename}")
    else:
        print("No code block found in the response.")

# Example usage
system_message = "You are an embedded system and linux expert who build all kinds of electronic products and using mcu"
prompt = "i am building a code demo for testing pwm on my arm board which is the raspberry pi 4,show me the steps.Reply like this:1.xxx 2.xxx ..."
response = ask_GPT(system_message, prompt)
print(response)

code_queue = queue.Queue()
filename_queue = queue.Queue()

code_thread = threading.Thread(target=extract_code, args=(response, code_queue))
code_thread.start()

filename = "generated_code.py"
filename_queue.put(filename)

save_thread = threading.Thread(target=save_code_to_file, args=(code_queue, filename_queue))
save_thread.start()

code_thread.join()
save_thread.join()

