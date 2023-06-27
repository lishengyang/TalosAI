import openai
openai.organization = "org-8dDxvNrdfyeMkV8m37fhLUrx"
openai.api_key = "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"

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
    print(f"ChatGPTPlus: {reply}")
    messages.append({"role": "user", "content": reply})
