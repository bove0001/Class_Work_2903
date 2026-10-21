from google import genai
from google.genai.types import GenerateContentConfig
import rich
from rich.markdown import Markdown


client = genai.Client()
chat=client.chats.create(model="gemini-2.5-flash")

while True:
    question = input("Ask a question (or type 'exit' to quit): ")
    if question.lower() == "exit":
        break

    response = chat.send_message(
        message=question,
        config=GenerateContentConfig(
            system_instruction="""You are a helpful programming tutor for Java programming students.
            You can explain concepts and programs but don't give the answers.
            """
        )
    )

    rich.print(Markdown(response.text))