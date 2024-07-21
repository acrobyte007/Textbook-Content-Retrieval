FROM python:3.9-slim
RUN pip install scikit-learn transformers
WORKDIR /app
COPY clustering_and_summarization.py .
CMD ["python", "clustering_and_summarization.py"]
