import requests
from openai import OpenAI

# ---------------------------
# CONFIG (PUT YOUR KEY HERE)
# ---------------------------
OPENAI_API_KEY = "YOUR_API_KEY"
client = OpenAI(api_key=OPENAI_API_KEY)


# ---------------------------
# GPT MODEL
# ---------------------------
def ask_gpt(question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message.content


# ---------------------------
# OLLAMA MODEL (LOCAL)
# ---------------------------
def ask_llama(question):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": question,
            "stream": False
        }
    )
    return response.json()["response"]


# ---------------------------
# MAIN WRAPPER
# ---------------------------
def ask_llm(question, model="gpt"):
    if model == "gpt":
        return ask_gpt(question)
    elif model == "llama":
        return ask_llama(question)
    else:
        return "Invalid model"