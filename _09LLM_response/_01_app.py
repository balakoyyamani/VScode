from google import genai
import os
print(os.getenv("GOOGLE_API_KEY"))
client=genai.Client(api_key=os.getenv("GenAi_API_KEY"))
cont=input("Enter the prompt :")
response=client.models.generate_content(
    model="gemini-3.5-flash",
    contents=cont
)
print(response.text)

#with open("response.json","w") as file:
    #file.write(response.text)

#for model in client.models.list():
#    print(model.name)