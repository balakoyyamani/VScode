from config import client,model
import numpy as np

documents = [
    "Learn Java Programming",
    "Spring Boot REST API Guide",
    "Python Basics",
    "SQL Tutorial",
    "Cricket Rules",
    "Docker for Beginners",
    "React Fundamentals"
]

response=client.models.embed_content(
    model=model,
    contents=documents
)

vector=[]
for embedding in response.embeddings:
    vector.append(embedding.values)

query=input("Search : ")

query_response=client.models.embed_content(
    model=model,
    contents=query
)
query_vector=query_response.embeddings[0].values

def similar(a,b):
    a=np.array(a)
    b=np.array(b)
    score=np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
    return score

score=[]

for i in range(len(vector)):
    score.append(similar(query_vector,vector[i]))

results=list(zip(documents,score))

for document, score in results[:-1]:
    print(f"{score:.3f} -> {document}")


results.sort(key=lambda x:x[1],reverse=True)
print("\nTop Matches\n")

for document, score in results[:3]:
    print(f"{score:.3f} -> {document}")