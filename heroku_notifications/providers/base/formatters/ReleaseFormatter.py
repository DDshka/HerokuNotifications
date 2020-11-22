from .BaseFormatter import BaseFormatter


class ReleaseFormatter(BaseFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._version = self._data['version']
        self._app_name = self._data['app']['name']
        self._description = self._data['description']
        self._status = self._data['status']

    def create(self):
        """
        {
          "actor": {
            "email": "heroku-postgresql@addons.heroku.com",
            "id": "f87b5e7e-4631-46cc-9912-9fcdbbb6c985"
          },
          "data": {
            "addon_plan_names": [
              "heroku-postgresql:hobby-dev"
            ],
            "app": {
              "id": "44dc9c7a-771c-4a9e-bfe9-a8dbc1c55f4d",
              "name": "sample-app-0339"
            },
            "created_at": "2016-10-26T22:50:29Z",
            "description": "Update DATABASE by heroku-postgresql",
            "status": "succeeded",
            "id": "5f1463a4-0210-43ba-b906-52599e246482",
            "slug": null,
            "updated_at": "2016-10-26T22:50:29Z",
            "user": {
              "email": "heroku-postgresql@addons.heroku.com",
              "id": "f87b5e7e-4631-46cc-9912-9fcdbbb6c985"
            },
            "version": 3,
            "current": true
          },
        }
        """

        return f'Release v.{self._version} has been started for {self._app_name}.\n' \
               f'\n' \
               f'Description: {self._description}'

    def update(self, ):
        """
        {
          "actor": {
            "email": "user-0008@example.com",
            "id": "125f0179-2fc8-4833-9e20-6e9314f2b233"
          },
          "data": {
            "app": {
              "id": "61cfe066-573f-45b4-a566-138323880eeb",
              "name": "sample-app-0008"
            },
            "created_at": "2016-05-10T07:30:32Z",
            "description": null,
            "status": "failed",
            "id": "ddc2fba2-b2ad-41f5-bf7c-6e9b4614a53b",
            "slug": null,
            "updated_at": "2016-05-10T07:30:32Z",
            "user": {
              "email": "user-0008@example.com",
              "id": "125f0179-2fc8-4833-9e20-6e9314f2b233"
            },
            "version": 1
          },
        }
        """

        if self._status == 'failed':
            return f'Release v.{self._version} failed for {self._app_name}.'

        return f'Release v.{self._version} succeeded for {self._app_name}.'
