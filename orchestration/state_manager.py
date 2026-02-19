class StateManager:

    def __init__(self):

        self.state = {}


    def update(self, decision):

        self.state["last"] = decision


    def get(self):

        return self.state