FROM python:3.9-slim
RUN pip install pymilvus sentence-transformers nltk
RUN python -m nltk.downloader punkt
WORKDIR /app
COPY retrieval.py .
CMD ["python", "retrieval.py"]
