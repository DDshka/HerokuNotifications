class ActorFormatter:
    def __init__(self, actor: dict):
        self._actor = actor
        self._email = self._actor['email']

    def format(self, message: str):
        return f'{message}' \
               f'\n' \
               f'Initiated by {self._email}'
