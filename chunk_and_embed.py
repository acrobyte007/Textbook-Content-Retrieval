import nltk
from sentence_transformers import SentenceTransformer

nltk.download('punkt')
model = SentenceTransformer('all-MiniLM-L6-v2')

def chunk_text(text, chunk_size=100):
    words = nltk.word_tokenize(text)
    chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

with open("extracted_texts.txt", "r") as f:
    texts = f.read().split("\n\n")

chunks = [chunk for text in texts for chunk in chunk_text(text)]
embeddings = model.encode(chunks)

import pickle
with open("chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

with open("embeddings.pkl", "wb") as f:
    pickle.dump(embeddings, f)
