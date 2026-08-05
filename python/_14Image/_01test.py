from google import genai
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("API_KEY")

client=genai.Client(api_key=api_key)

image1=Image.open("img_1.jpg")
image2=Image.open("img_2.jpg")

response=client.models.generate_content(
    model="gemini-3.5-flash",
    contents=["is the car damaged or not (every image)",image1,image2]
)

print(response.text)
