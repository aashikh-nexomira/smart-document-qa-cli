import os
from groq import Groq
import json

# Create Groq client
client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)

# Read the document
with open("document.txt", "r") as file:
    document = file.read()

# Ask the user a question
question = input("Ask a question about the document: ")

# Send document + question to the LLM
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
messages=[
    {
        "role": "user",
"content": f"""
<document>
{document}
</document>

<task>
Answer the user's question using only the information contained in the document.
</task>

<question>
{question}
</question>

<rules>
1. Use only information contained in the document.
2. Never use outside knowledge or make up information.
3. If the answer is found in the document:
   - Answer the question.
   - Copy the exact sentence(s) that support the answer into source_snippet.
   - Set confidence between 0 and 1.
4. If the answer is NOT found in the document:
   - Say that the document does not contain the answer.
   - Set confidence to 0.
   - Set source_snippet to an empty string.
5. Return only a valid JSON object.
</rules>

<output_format>
{{
    "answer": "answer based only on the document",
    "confidence": 0.0,
    "source_snippet": "exact text from the document supporting the answer"
}}
</output_format>
"""
    }
]
)

# Get the raw response
raw_response = response.choices[0].message.content

# Remove Markdown code fences if the model added them
raw_response = raw_response.replace("```json", "").replace("```", "").strip()

# Convert JSON text into a Python dictionary
result = json.loads(raw_response)

# Print the structured result
print("\nAnswer:", result["answer"])
print("Confidence:", result["confidence"])
print("Source:", result["source_snippet"])