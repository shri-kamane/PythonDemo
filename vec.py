from openai import OpenAI
from dotenv import load_dotenv
import os
import chromadb
load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

chroma = chromadb.Client()
collection = chroma.get_or_create_collection("handbook")

### this is for loading and storeing the document in the rag system ###
def load_and_store(filepath):
    with open(filepath,'r',encoding="utf-8") as f:
        text = f.read()
        chunk = [p.strip() for p in text.split('\n') if p.strip()]
        collection.add(
            documents = chunk,
            ids =[f"doc_{i}" for i in range(len(chunk))]
        )

### this funcion is for comparing asdked quetion and documents emmbedding ###        
def ask(quetion):
    results = collection.query(
        query_texts = [quetion],
        n_results = 2
    )
    chunk = results['documents'][0]
    print(f"retrived chunks : {chunk}")
    context = "\n".join(chunk)

### building prompt for llm ###
    rag_prompt = f'''Use ONLY the context given below to answer the question.
                    If the context does not contain the answer, say "i don't have information about in my documents"
                    "context : " {context},"question : " {quetion},"answer : "'''
    response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": rag_prompt}],
            max_tokens=200,
            temperature=0.5
        )
    return response.choices[0].message.content

load_and_store('handbook.txt')
print("document loaded and stord in rag!")
print("type 'exit' to quite : ")
while True:
    query = input("Enter The Quetion?")
    if query.lower == 'exit' :
        break
    answer = ask(query)
    print(f"Bot Answer : {answer}")
            