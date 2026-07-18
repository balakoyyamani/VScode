from config import model,client
import numpy as np

text1="I need a job"
text2="I am open to work"
response=client.models.embed_content(
    model=model,
    contents=[text1,text2]
)
v1=response.embeddings[0].values
v2=response.embeddings[1].values


def simlar_score(a,b):
    a=np.array(a)
    b=np.array(b)

    return (np.dot(a,b)/
            np.linalg.norm(a)*np.linalg.norm(b))
print("Score :",simlar_score(v1,v2))
