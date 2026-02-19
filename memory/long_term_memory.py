class LongTermMemory:

    def __init__(self):

        self.history = []


    def store(self, record):

        self.history.append(record)


    def get_all(self):

        return self.history