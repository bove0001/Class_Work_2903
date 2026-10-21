from google import genai

client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents="""We run a yoga studio in Minneapolis.  Most of our clients
    are women, but we have a few men who attend our classes.  
    We want to create a new marketing campaign to attract more men to our
    yoga classes. """


)

print(response)