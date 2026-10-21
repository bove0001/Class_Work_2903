from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents="""We are a business selling logging and monitoring products
    What are good products to give away at our booth at PyCon?
    Last year we gave away tote bags and met our budget.
    This year we want to give away something different, but still within our budget.
    """
)

print(response.text)