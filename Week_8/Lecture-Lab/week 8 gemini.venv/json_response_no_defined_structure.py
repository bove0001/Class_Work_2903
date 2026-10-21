from google import genai
from google.genai.types import GenerateContentConfig
from pydantic import BaseModel
from pprint import pprint

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]
    instructions: list[str]




client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents="""Create a recipe with seven ingredients
    """,
    config=GenerateContentConfig(
        system_instruction='Include US and Metric units',
        response_mime_type="application/json",
        response_schema=Recipe
    )

)

print(response.text)
recipe = response.parsed
print(recipe.recipe_name)

for ingredient in recipe.ingredients:
    print(ingredient)   

for step in recipe.instructions:
    print(step)
