class BaseFormatter:
    def __init__(self, data: dict):
        self._data = data

    def create(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def destroy(self):
        raise NotImplementedError


