FROM python:3.9-slim
RUN pip install pymupdf
WORKDIR /app
COPY textbook_extraction.py .
CMD ["python", "textbook_extraction.py"]
