from pymilvus import Collection
from sentence_transformers import SentenceTransformer
import numpy as np
import nltk

nltk.download('punkt')

collection = Collection("raptor_index")
model = SentenceTransformer('all-MiniLM-L6-v2')

def expand_query(query):
    words = nltk.word_tokenize(query)
    synonyms = set(words)  
    expanded_query = " ".join(synonyms)
    return expanded_query

def retrieve_and_answer_query(query):
    expanded_query = expand_query(query)
    query_embedding = model.encode(expanded_query)
    search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
    results = collection.search([query_embedding], "embedding", search_params, limit=10)
    
    answers = []
    for result in results[0]:
        text = result.entity.get("text")
        title = result.entity.get("textbook_title")
        page = result.entity.get("page_number")
        answer = model.encode(text)  
        answers.append({"textbook_title": title, "page_number": page, "answer": answer})
    return answers


query = "Who is gorge?"
results = retrieve_and_answer_query(query)
for result in results:
    print(f"Textbook: {result['textbook_title']}, Page: {result['page_number']}")
    print(f"Answer: {result['answer']}")
