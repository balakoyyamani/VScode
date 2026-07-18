from google import genai
import os

api=os.getenv("GOOGLE_API_KEY_EMBED_01")

client=genai.Client(api_key=api)

model="gemini-embedding-001"
