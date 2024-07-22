import pickle
from sklearn.mixture import GaussianMixture
from transformers import pipeline

with open("embeddings.pkl", "rb") as f:
    embeddings = pickle.load(f)

gmm = GaussianMixture(n_components=10, covariance_type='full')
gmm.fit(embeddings)
cluster_labels = gmm.predict(embeddings)

with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

cluster_texts = {i: [] for i in range(10)}
for idx, label in enumerate(cluster_labels):
    cluster_texts[label].append(chunks[idx])

summarizer = pipeline("summarization", model="bert-base-uncased")

def summarize_text(texts):
    summaries = summarizer(texts, max_length=50, min_length=25, do_sample=False)
    return [summary['summary_text'] for summary in summaries]

cluster_summaries = {i: summarize_text(cluster_texts[i]) for i in range(10)}

with open("cluster_summaries.pkl", "wb") as f:
    pickle.dump(cluster_summaries, f)
