import openai
#openai.api_key = "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"
openai.api_key = "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"
#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 

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "user", "content": reply})
