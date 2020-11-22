from .BaseFormatter import BaseFormatter


class FormationFormatter(BaseFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._app_name = self._data['app']['name']

        self._command = self._data['command']
        self._type = self._data['type']
        self._quantity = self._data['quantity']
        self._size = self._data['size']

    def destroy(self):
        """
        {
          "actor": {
            "email": "user-4451@example.com",
            "id": "0a8411fe-aae7-49bb-a75d-69c8e94cb4cb"
          },
          "data": {
            "app": {
              "id": "c6085e11-9769-4036-b64a-3c60da3fc925",
              "name": "sample-app-2263"
            },
            "command": "ruby server.rb",
            "created_at": "2014-01-01T08:00:00Z",
            "id": "d77750f3-71db-494f-93cc-1c3111190f8b",
            "type": "web",
            "quantity": 0,
            "size": "1X",
            "updated_at": "2014-01-01T08:00:00Z"
          },
        }
        """
        return f'Formation has been removed for {self._app_name}\n' \
               f'Command: {self._command}\n' \
               f'Type: {self._type}\n' \
               f'Quantity: {self._quantity}\n' \
               f'Size: {self._size}'

    def update(self):
        """
        {
          "actor": {
            "email": "user-0297@example.com",
            "id": "2530e242-a531-4d37-99ab-d8997e2335d0"
          },
          "data": {
            "app": {
              "id": "b225a8d2-1602-42c3-a1a2-98c3c266cc0d",
              "name": "sample-app-0197"
            },
            "command": "ruby server.rb",
            "created_at": "2016-10-26T22:49:29Z",
            "id": "13f27e47-df06-48a1-92be-f521babd9060",
            "type": "web",
            "quantity": 0,
            "size": "1X",
            "updated_at": "2016-10-26T22:49:29Z"
          },
        }
        """
        return f'Formation has been updated for {self._app_name}\n' \
               f'Command: {self._command}\n' \
               f'Type: {self._type}\n' \
               f'Quantity: {self._quantity}\n' \
               f'Size: {self._size}'
