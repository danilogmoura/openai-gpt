import os
import openai
from dotenv import load_dotenv

# loading variables from .env file
load_dotenv()

# Initialize the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Calling the OpenAI API and listing models
models = openai.Engine.list()
print(models)
