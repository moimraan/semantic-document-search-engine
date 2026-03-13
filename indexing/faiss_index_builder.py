import faiss
import numpy as np

class IndexBuilder:

    def __init__(self, dim):

        self.index = faiss.IndexFlatL2(dim)
        self.docs = []

    def build(self, embeddings, docs):

        self.index.add(np.array(embeddings))
        self.docs = docs

    def search(self, query_embedding, k=5):

        distances, indices = self.index.search(query_embedding, k)

        results = []

        for i in indices[0]:
            results.append(self.docs[i])

        return results
