from .BaseFormatter import BaseFormatter


class AddonAttachmentFormatter(BaseFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._addon_name = self._data['addon']['name']
        self._app_name = self._data['app']['name']

    def create(self):
        """
        {
          "actor": {
            "email": "user-0165@example.com",
            "id": "33500732-3b64-436f-9710-64cc569c3e4f"
          },
          "data": {
            "addon": {
              "id": "c53451e0-bd35-4a30-b2c1-6220cc8d759e",
              "name": "my-resource-0003",
              "app": {
                "id": "d2f24bd2-399a-4868-9467-bc0ba2411cc2",
                "name": "sample-app-0084"
              }
            },
            "app": {
              "id": "d2f24bd2-399a-4868-9467-bc0ba2411cc2",
              "name": "sample-app-0084"
            },
            "id": "25bfb830-8c4a-49e1-b0a3-831da386de90",
            "name": "DATABASE",
            "created_at": "2016-10-26T22:48:45Z",
            "updated_at": "2016-10-26T22:48:45Z",
            "web_url": "https://postgres.localhost/discover?hid=resource17@localhost"
          },
        }
        """
        return f'Addon attachment {self._addon_name} has been created for {self._app_name}.'

    def destroy(self):
        """
        {
          "actor": {
            "email": "slowdb@addons.heroku.com",
            "id": "03d3c927-9a36-4001-9fca-ac30c646a117"
          },
          "data": {
            "addon": {
              "id": "1ecadf4a-0775-4868-8103-3f5fb689631d",
              "name": "slowdb-infinite-52190",
              "app": {
                "id": "1cf9ea2a-22d7-43e1-83f7-a1aabc3bd39a",
                "name": "sample-app-0273"
              }
            },
            "app": {
              "id": "1cf9ea2a-22d7-43e1-83f7-a1aabc3bd39a",
              "name": "sample-app-0273"
            },
            "id": "1ce601cc-314d-4f53-ab57-41983258c894",
            "name": "SLOWDB",
            "created_at": "2016-10-26T22:50:01Z",
            "updated_at": "2016-10-26T22:50:01Z",
            "web_url": null
          },
        }
        """
        return f'Addon attachment {self._addon_name} has been removed from {self._app_name}.'
