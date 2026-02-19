class VectorStore:

    def __init__(self):

        self.vectors = []


    def add(self, vector):

        self.vectors.append(vector)


    def search(self, query):

        return self.vectors