# README

## Project Overview

This project involves the selection, content extraction, chunking, and indexing of digital textbooks using advanced natural language processing (NLP) techniques. The primary goal is to create a RAPTOR index for efficient content retrieval and to implement a sophisticated question-answering system using BERT.

## Steps and Methodology

### 1. Textbook Selection and Content Extraction

Task:
- Select three digital textbooks, each containing more than 300 pages.
- Extract the content from these textbooks thoroughly, ensuring that all relevant text is captured.

Approach:
- Utilize a PDF parser to read and extract the text from each page of the textbooks.
- Ensure that all textual information is accurately captured without omitting any relevant sections.

### 2. Data Chunking and RAPTOR Indexing

Task:
- Chunk the extracted content into short, contiguous texts of approximately 100 tokens each, preserving sentence boundaries.
- Embed the chunked texts using Sentence-BERT (SBERT) to create vector representations.
- Implement the RAPTOR indexing method.

Approach:
- Chunking:
  - Divide the text into chunks of around 100 tokens each, ensuring sentence boundaries are preserved.
- Embedding:
  - Use SBERT to convert text chunks into vector embeddings.
- RAPTOR Indexing:
  - Clustering: 
    - Use Gaussian Mixture Models (GMMs) for soft clustering of the embedded chunks, allowing nodes to belong to multiple clusters.
  - Summarization:
    - Summarize the clusters using BERT to create concise representations of the grouped texts.
  - Recursive Clustering and Summarization:
    - Re-embed the summarized texts and recursively apply the clustering and summarization process to form a hierarchical tree structure.
  - Storage:
    - Store the RAPTOR index in a MILVUS vector database, including metadata such as the textbook title and page number.

### 3. Retrieval Techniques

Task:
- Implement query expansion techniques to enhance the retrieval process.
- Employ hybrid retrieval methods and evaluate their effectiveness in retrieving relevant content from the RAPTOR index.

Approach:
- Retrieval Methods:
  - BM25 with BERT/bi-encoder based retrieval
- Re-Ranking:
  - Re-rank the retrieved data based on relevance and similarity to the query using appropriate ranking algorithms.

### 4. Question Answering

Task:
- Pass the retrieved and re-ranked data to BERT for question answering.
- Generate accurate and relevant answers based on the retrieved data from the RAPTOR index.

Approach:
- Utilize BERT capable of understanding and generating contextually relevant answers.
- Ensure that the answers provided by BERT are based on the data retrieved from the RAPTOR index, maintaining accuracy and relevance.

## Tools and Technologies

- Text Extraction: PDF parsers
- Chunking and Embedding: SBERT (Sentence-BERT)
- Clustering: Gaussian Mixture Models (GMMs)
- Summarization: BERT
- Indexing and Storage: MILVUS vector database
- Question Answering: BERT

## Dependencies

- Docker
- Python
- Sentence-BERT (SBERT)
- Scikit-learn (for GMMs)
- BERT
- Milvus vector database

## Setup Instructions

1. Clone the Repository:
   git clone <https://github.com/acrobyte007/Textbook-Content-Retrieval>
  
2. Install Docker:
   - Follow the official Docker documentation to install Docker on your system.

3. Build and Run Docker Containers:
   Just run the yml file
   
5. Configure MILVUS:
   - Follow the official MILVUS documentation to set up and configure the MILVUS vector database on localhost.

6. Run the Pipeline:
   - Execute the main script to start the content extraction, chunking, embedding, indexing, and question-answering pipeline.

## Usage

1. Textbook Selection and Extraction:
   - Place the digital textbooks in the designated input directory.
   - Run the extraction script to process and extract text content from the textbooks.

2. Chunking and Indexing:
   - Execute the chunking and embedding script to create vector representations of the text chunks.
   - Run the RAPTOR indexing script to build the hierarchical index and store it in MILVUS.

3. Query and Retrieval:
   - Use the retrieval script to perform queries against the RAPTOR index.
   - Implement query expansion techniques as needed.

