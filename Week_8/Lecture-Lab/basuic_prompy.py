from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="genai-bison",
    contents='Why is the sky blue?  Can you explain it in simple terms?'

)

print(response)