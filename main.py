import json
import pandas as pd
import time

from llm_runner import ask_llm
from evaluator import evaluate


# ---------------------------
# LOAD DATASET
# ---------------------------
with open("dataset.json") as f:
    data = json.load(f)


results = []

# ---------------------------
# MODELS TO COMPARE
# ---------------------------
models = ["gpt", "llama"]


# ---------------------------
# RUN EVALUATION
# ---------------------------
for model in models:
    print(f"\nRunning model: {model}")

    for item in data:
        question = item["question"]
        expected = item["expected_answer"]

        start = time.time()
        answer = ask_llm(question, model)
        latency = time.time() - start

        score = evaluate(answer, expected)

        results.append({
            "model": model,
            "question": question,
            "answer": answer,
            "expected": expected,
            "score": score,
            "latency": latency
        })


# ---------------------------
# SAVE RESULTS
# ---------------------------
df = pd.DataFrame(results)
df.to_csv("results.csv", index=False)

print("\nEvaluation complete! results.csv generated.")