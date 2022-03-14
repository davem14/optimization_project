class Problem:
    def __init__(self):
        self.optimal_val = 0

    def evaluate(self, state):
        raise NotImplementedError

    def neighbors(self, state):
        raise NotImplementedError

    def show(self, state):
        pass
