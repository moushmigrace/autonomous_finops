class ShortTermMemory:

    def __init__(self, window=10):
        self.window = window
        self.data = {}

    def store(self, key, value):

        if key not in self.data:
            self.data[key] = []

        self.data[key].append(value)

        if len(self.data[key]) > self.window:
            self.data[key].pop(0)

    def get(self, key):
        return self.data.get(key, [])