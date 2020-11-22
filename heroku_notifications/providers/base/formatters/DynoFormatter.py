from .BaseFormatter import BaseFormatter


class DynoFormatter(BaseFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._command = self._data['command']
        self._name = self._data['name']
        self._app_name = self._data['app']['name']
        self._size = self._data['size']
        self._state = self._data['state']
        self._type = self._data['type']

    def create(self):
        """
        {
          "actor": {
            "email": "user-0243@example.com",
            "id": "f5e62416-fd74-4d01-ba84-487479cff6b8"
          },
          "data": {
            "attach_url": null,
            "command": "ls",
            "created_at": "2016-10-26T22:44:12Z",
            "id": "7600c07e-b329-4f1d-977a-49559c26efb2",
            "name": "run.1",
            "app": {
              "id": "39c3f6bd-af8f-4714-95f5-d865a2f23b71",
              "name": "sample-app-0146"
            },
            "release": {
              "id": "9f52b70f-fc76-4092-ab9c-a1d75075a507",
              "version": 1
            },
            "size": "1X",
            "state": "up",
            "type": "run",
            "updated_at": "2016-10-26T22:44:12Z"
          },
        }
        """

        return f'New dyno has been created for {self._app_name}.\n' \
               f'Name: {self._name}\n' \
               f'Command: {self._command}\n' \
               f'Size: {self._size}\n' \
               f'Type: {self._type}\n' \
               f'State: {self._state}'
