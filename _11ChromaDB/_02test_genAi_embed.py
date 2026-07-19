from google import genai
import chromadb
import os
from pprint import pprint

api=os.getenv("GOOGLE_API_KEY_EMBED_01")
client=genai.Client(api_key=api)

clientdb=chromadb.Client()

collections=clientdb.create_collection(
    name="programming_courses"
)

texts = [
    "Learn Java Programming",
    "Spring Boot REST API",
    "Python for Beginners"
]
response=client.models.embed_content(
    model="gemini-embedding-001",
    contents=texts
)

vector=[]
for embed in response.embeddings:
    vector.append(embed.values)


collections.add(
    ids=["1","2","3"],
    documents=texts,
    embeddings=vector
)

query=input("Search :")

query_response=client.models.embed_content(
    model="gemini-embedding-001",
    contents=query
)
query_vector=query_response.embeddings[0].values

results=collections.query(
    query_embeddings=[query_vector],
    n_results=2
)

pprint(results)

for doc_id,doc in zip(
    results["ids"][0],
    results["documents"][0]
):
    print(f"Id : {doc_id}")
    print(f"Documents : {doc}")
    print("-" * 50)

