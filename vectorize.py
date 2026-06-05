import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

#to load dataset 
df = pd.read_csv("data/financial_anomaly_data.csv")

#to convert every row into text
documents = []

for _, row in df.iterrows():

    text = f"""
    Transaction {row['TransactionID']}
    Account {row['AccountID']}
    Amount {row['Amount']}
    Merchant {row['Merchant']}
    """

    documents.append(text)

print("TOTAL DOCUMENTS:", len(documents))

# to load embedding moddel
model = SentenceTransformer('all-MiniLM-L6-v2')

# to create the embeddings
embeddings = model.encode(documents)

print("Embedding Shape:", embeddings.shape)

# now create FAISS vector DB
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

print("TOTAL VECTORS IN DATABASE:", index.ntotal)