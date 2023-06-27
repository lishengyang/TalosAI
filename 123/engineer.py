import openai
openai.api_key = "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"

messages = [
    {"role": "system", "content": "you are an embeddeed engineer who is specilized in designing electronic and pcb boards,the target od design is a product that everyone in the world would be chasing for,the product line is based on industrial business and consuming electronics,show me the most used electronic product in the world"},
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
    messages.append({"role": "assistant", "content": reply})
