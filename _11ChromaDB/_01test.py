from config import client
from pprint import pprint

collection=client.create_collection(
    name="courses"
)

collection.add(
    documents=["Learn Java",
               "Python Basics",
               "Spring Boot Guide",
               "I love ooty"
               ],
    ids=["1",
        "2",
        "3",
        "4"
        ],
    metadatas=[
        {
        "Author":"Bala",
        "Level ":"easy"
          },
          {
        "Author":"Bala",
        "Level ":"moderate"
          },
          {
        "Author":"Bala",
        "Level ":"hard"
          },
          {
        "Author":"Bala",
        "Level ":"very hard"
          }
        ]
)
results=collection.query(
    query_texts=["Artificial Intelligence"],
    n_results=5
)

for doc_id,doc in zip(
    results["ids"][0],
    results["documents"][0]
):
    print(f"Id : {doc_id} \nDoc : {doc}")
    print("-" * 50)

pprint(results)
