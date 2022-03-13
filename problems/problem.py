class Problem:

    def evaluate(self, state):
        raise NotImplementedError

    def neighbors(self, state):
        raise NotImplementedError

    def show(self, state):
        pass
