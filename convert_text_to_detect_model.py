from openai import OpenAI, api_key

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="API_KEY_HERE",
)

completion = client.chat.completions.create(
    model="x-ai/grok-4.1-fast",
    messages=[
        {
            "role": "system",
            "content": "You are an going to say that either this customer service issue can needs a human or emails only write email or human as your answer",
        },
        {
            "role": "user",
            "content": "Hello, I’m calling today because my son is sick",
        },
    ],
)

print(completion.choices[0].message.content)
