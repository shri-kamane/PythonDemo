from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

""" Created the Hadbok of the rules """
handbook = ['Anuanl leave policy :full staff get 15 dayts annual leaves and 10 days sick leaves per year',
            'Library Houurs : the college library is open from 8am to 8pm on weekdays and 10am to 6pm on weekends',
            'Cafeteria Menu : the college cafeteria serves breakfast from 7am to 10am, lunch from 12pm to 2pm, and dinner from 6pm to 8pm'
            ]

""" craeted the embeddings """
def get_embeddings(text):
    embeddings = model.encode(text)
    return embeddings.tolist()

store = []

for entry in handbook:
    embeddings = get_embeddings(entry)
    store.append({"Text" : entry,"embeddings" : embeddings})
    
def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    norm_vec1 = sum(a * a for a in vec1) ** 0.5
    norm_vec2 = sum(b * b for b in vec2) ** 0.5
    return dot_product / (norm_vec1 * norm_vec2)

while True:
    query = input("Enter your question(or 'exit' to quit): ")
    if query.lower() == 'exit':
        break

    query_emmbedding = get_embeddings(query)
    scores = []
    for entry in store:
        score = cosine_similarity(query_emmbedding, entry["embeddings"])
        scores.append(score, entry["Text"])

    print("Score Similarity : ", scores)
    scores.sort(reverse=True)
    best_score, best_chunk = scores[0]

    print(f'best macth : {best_chunk} , score : {best_score: .4f}')
    rag_prompt = f'''Use ONLY the context given below to answer the question.
                    If the context does not contain the answer, say "i don't know"
                    "context : " {best_chunk},"question : " {query},"answer : "'''

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": rag_prompt}],
        max_tokens=200,
        temperature=0.5
    )

    print(response.choices[0].message.content)
    
    

