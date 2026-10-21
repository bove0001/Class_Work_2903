from google import genai
from google.genai.types import GenerateContentConfig
import rich
from rich.markdown import Markdown
import sys


client = genai.Client()
chat=client.chats.create(model="gemini-2.5-flash")

try:
    with open('C:/Users/jbove/OneDrive/MCTC/ITEC 2903 Software Development Projects/VSCode/Class_Work_2903/week 8 gemini.venv/chat_system_instructions.txt', 'r') as f:
        system_instruction_text = f.read()
except FileNotFoundError:
    print("Error: The file 'chat_system_instructions.txt' was not found.")
    sys.exit()

while True:
    question = input("Ask a question (or type 'exit' to quit): ")
    if question.lower() == "exit":
        break

    response = chat.send_message(
        message=question,
        config=GenerateContentConfig(
            system_instruction=system_instruction_text
            )
    )

    rich.print(Markdown(response.text))