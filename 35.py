import openai
openai.api_key = "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"

def generate_answer(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7
    )
    message = completions.choices[0].text.strip()
    return message


if __name__ == '__main__':
    prompt = input("prompt: \n")
    res = generate_answer(prompt)
    print(res)
