FROM python:3.9-slim
RUN pip install nltk sentence-transformers
RUN python -m nltk.downloader punkt
WORKDIR /app
COPY chunk_and_embed.py .
CMD ["python", "chunk_and_embed.py"]
