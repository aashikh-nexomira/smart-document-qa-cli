# Smart Document Q&A CLI

A command-line application that uses an LLM to answer questions about a text document and return a structured JSON response.

## Project Overview

The application:

1. Reads a text document.
2. Accepts a question from the user.
3. Sends the document and question to an LLM through an API.
4. Uses prompt engineering techniques to control the response.
5. Returns structured JSON containing:
   - Answer
   - Confidence
   - Source snippet

## Technologies Used

- Python
- Groq API
- OpenAI GPT-OSS 20B model
- JSON
- PowerShell

## Project Structure

```text
Smart-Document-QA/
│
├── read_document.py
├── document.txt
├── README.md
└── .gitignore