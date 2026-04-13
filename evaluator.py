from openai import OpenAI

OPENAI_API_KEY = "YOUR_API_KEY"
client = OpenAI(api_key=OPENAI_API_KEY)


def evaluate(answer, expected):
    prompt = f"""
You are an evaluator.

Expected Answer: {expected}
Model Answer: {answer}

Is the model answer correct?
Reply only YES or NO.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content.strip()

    if "YES" in result.upper():
        return 1
    return 0