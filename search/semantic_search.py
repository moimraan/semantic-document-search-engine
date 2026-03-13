from embeddings.embedding_model import EmbeddingModel

class SemanticSearch:

    def __init__(self, index):

        self.index = index
        self.embedder = EmbeddingModel()

    def search(self, query):

        query_embedding = self.embedder.encode([query])

        results = self.index.search(query_embedding)

        return results
