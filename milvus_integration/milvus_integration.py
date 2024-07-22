from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection
import pickle

with open("embeddings.pkl", "rb") as f:
    embeddings = pickle.load(f)

with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

connections.connect()

fields = [
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=384),
    FieldSchema(name="text", dtype=DataType.STRING),
    FieldSchema(name="textbook_title", dtype=DataType.STRING),
    FieldSchema(name="page_number", dtype=DataType.INT64)
]
schema = CollectionSchema(fields)
collection = Collection("raptor_index", schema)

entities = [
    embeddings.tolist(),
    chunks,
    ["Textbook1"] * len(chunks),
    [1] * len(chunks)
]

collection.insert(entities)
