from typing import Union


class Problem:

    def evaluate(self, state):
        raise NotImplementedError

    def neighbors(self, state):
        raise NotImplementedError

    @property
    def opt(self) -> Union[max, min]:
        raise NotImplementedError

    def show(self, state):
        pass
