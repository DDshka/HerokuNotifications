from .BaseFormatter import BaseFormatter


class AddonFormatter(BaseFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._addon_name = self._data['name']
        self._addon_service_name = self._data['addon_service']['name']
        self._plan_name = self._data['plan']['name']
        self._app_name = self._data['app']['name']
        self._state = self._data['state']
        self._web_url = self._data['web_url']

    def create(self):
        """
       {
          "actor": {
            "email": "user-0043@example.com",
            "id": "3a478127-ebe2-428b-93a7-bede426fcc33"
          },
          "data": {
            "actions": [

            ],
            "config_vars": [

            ],
            "created_at": "2016-10-26T22:48:19Z",
            "id": "ac7eaeaf-cac3-43f2-8854-7c823e7bf755",
            "name": "cloudcounter-encircled-31432",
            "addon_service": {
              "id": "75d809f2-14d1-4e74-9002-35b62d1db6eb",
              "name": "cloudcounter"
            },
            "plan": {
              "id": "d22dadac-b12b-4f49-b7ce-2f95f5bb42b5",
              "name": "cloudcounter:basic"
            },
            "app": {
              "id": "7c9e1f74-ad2c-4daf-91e5-f07bb7cafe90",
              "name": "sample-app-0036"
            },
            "provider_id": "",
            "state": "provisioning",
            "updated_at": "2016-10-26T22:48:19Z",
            "web_url": "https://addons-sso.localhost/apps/7c9e1f74-ad2c-4daf-91e5-f07bb7cafe90/addons/ac7eaeaf-cac3-43f2-8854-7c823e7bf755"
          },
        }
        """

        return f'Addon {self._addon_name} has been created for {self._app_name}\n' \
               f'Addon service: {self._addon_service_name}\n' \
               f'Plan: {self._plan_name}\n' \
               f'State: {self._state}' \
               f'\n' \
               f'{self._web_url}'

    def destroy(self):
        """
        {
          "actor": {
            "email": "slowdb@addons.heroku.com",
            "id": "03d3c927-9a36-4001-9fca-ac30c646a117"
          },
          "data": {
            "actions": [

            ],
            "config_vars": [

            ],
            "created_at": "2016-10-26T22:50:01Z",
            "id": "1ecadf4a-0775-4868-8103-3f5fb689631d",
            "name": "slowdb-infinite-52190",
            "addon_service": {
              "id": "a4d9fe8b-6200-4de1-9132-2d9f7654f784",
              "name": "slowdb"
            },
            "plan": {
              "id": "52b7a016-7dd0-49bc-84ad-638574565f70",
              "name": "slowdb:basic"
            },
            "app": {
              "id": "1cf9ea2a-22d7-43e1-83f7-a1aabc3bd39a",
              "name": "sample-app-0273"
            },
            "provider_id": "provider-id-123",
            "state": "provisioning",
            "updated_at": "2016-10-26T22:50:01Z",
            "web_url": null
          },
        }
        """


        return f'Addon {self._addon_name} has been removed from {self._app_name}.\n' \
               f'Addon service: {self._addon_service_name}\n' \
               f'Plan: {self._plan_name}\n' \
               f'State: {self._state}' \
               f'\n' \
               f'{self._web_url}'

    def update(self):
        """
        {
          "actor": {
            "email": "slowdb@addons.heroku.com",
            "id": "03d3c927-9a36-4001-9fca-ac30c646a117"
          },
          "data": {
            "actions": [

            ],
            "config_vars": [

            ],
            "created_at": "2016-10-26T22:50:01Z",
            "id": "1aa22eb5-157b-4bf3-92d9-d8a256eef621",
            "name": "slowdb-contoured-29490",
            "addon_service": {
              "id": "a4d9fe8b-6200-4de1-9132-2d9f7654f784",
              "name": "slowdb"
            },
            "plan": {
              "id": "52b7a016-7dd0-49bc-84ad-638574565f70",
              "name": "slowdb:basic"
            },
            "app": {
              "id": "5c139c87-6636-4948-9346-44fe86909c7e",
              "name": "sample-app-0272"
            },
            "provider_id": "provider-id-123",
            "state": "provisioning",
            "updated_at": "2016-10-26T22:50:01Z",
            "web_url": null
          },
        }
        """

        return f'Addon {self._addon_name} for {self._app_name} has been updated.\n' \
               f'Addon service: {self._addon_service_name}\n' \
               f'Plan: {self._plan_name}\n' \
               f'State: {self._state}' \
               f'\n' \
               f'{self._web_url}'
