FROM python:3.9-slim

# Install dependencies
RUN pip install pymilvus

# Set working directory
WORKDIR /app

# Copy script to container
COPY milvus_integration.py .

# Command to run the script
CMD ["python", "milvus_integration.py"]
