from .BaseFormatter import BaseFormatter


class AppFormatter(BaseFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._app_name = self._data['name']
        self._region_code = self._data['region']['name']

        self._web_url = self._data['web_url']

    def create(self):
        """
        {
          "actor": {
            "email": "user-0278@example.com",
            "id": "4c66e6a9-f574-4f51-9fa7-2d743d8ab713"
          },
          "data": {
            "archived_at": null,
            "buildpack_provided_description": null,
            "build_stack": {
              "id": "5e854079-da33-475b-a209-77f527c0e2fb",
              "name": "cedar-14"
            },
            "created_at": "2016-10-26T22:49:22Z",
            "id": "7c454377-91c6-44e3-87a2-ecb16437ced9",
            "git_url": "https://git.heroku.com/polar-wildwood-81034.git",
            "maintenance": false,
            "name": "polar-wildwood-81034",
            "owner": {
              "email": "org-0058@herokumanager.com",
              "id": "f948a684-4345-4bd2-b6cd-85d4175b93a5"
            },
            "region": {
              "id": "7044c05a-0873-42c2-abbe-6841c5481ba7",
              "name": "us"
            },
            "organization": {
              "id": "f948a684-4345-4bd2-b6cd-85d4175b93a5",
              "name": "org-0058"
            },
            "space": null,
            "released_at": "2016-10-26T22:49:22Z",
            "repo_size": null,
            "slug_size": null,
            "stack": {
              "id": "5e854079-da33-475b-a209-77f527c0e2fb",
              "name": "cedar-14"
            },
            "updated_at": "2016-10-26T22:49:22Z",
            "web_url": "https://polar-wildwood-81034.herokuapp.com/"
          },
        }
        """
        return f'{self._app_name} has been created.\n' \
               f'\n' \
               f'App url: {self._web_url}'

    def destroy(self):
        """
        {
          "action": "destroy",
          "actor": {
            "email": "user-0291@example.com",
            "id": "f7ace9a6-f1be-4a0f-8033-adbeb1ed964a"
          },
          "created_at": "2016-10-26T22:49:26Z",
          "id": "904942e5-8388-4e82-85f5-14d7f6c64f09",
          "data": {
            "archived_at": null,
            "buildpack_provided_description": "Ruby/Rails",
            "build_stack": {
              "id": "5e854079-da33-475b-a209-77f527c0e2fb",
              "name": "cedar-14"
            },
            "created_at": "2016-10-26T22:49:26Z",
            "id": "1578fb48-e184-4568-b2a0-2525101ec4f3",
            "git_url": "https://git.heroku.com/sample-app-0191.git",
            "maintenance": false,
            "name": "sample-app-0191",
            "owner": {
              "email": "user-0291@example.com",
              "id": "f7ace9a6-f1be-4a0f-8033-adbeb1ed964a"
            },
            "region": {
              "id": "7044c05a-0873-42c2-abbe-6841c5481ba7",
              "name": "us"
            },
            "organization": null,
            "space": null,
            "released_at": "2016-10-26T22:49:26Z",
            "repo_size": 1048576,
            "slug_size": null,
            "stack": {
              "id": "5e854079-da33-475b-a209-77f527c0e2fb",
              "name": "cedar-14"
            },
            "updated_at": "2016-10-26T22:49:26Z",
            "web_url": "https://sample-app-0191.herokuapp.com/"
          },
        }
        """
        return f'{self._app_name} has been removed.\n' \
               f'\n' \
               f'App url: {self._web_url}'

    def update(self):
        """
        {
          "actor": {
            "email": "user-0436@example.com",
            "id": "096370c8-f3ad-4e20-a309-fb4f06ec0a89"
          },
          "data": {
            "archived_at": null,
            "buildpack_provided_description": "Ruby/Rails",
            "build_stack": {
              "id": "5e854079-da33-475b-a209-77f527c0e2fb",
              "name": "cedar-14"
            },
            "created_at": "2016-10-26T22:50:14Z",
            "id": "d4714cc8-aa56-4314-817c-0c6a66ff3d41",
            "git_url": "https://git.heroku.com/sample-app-0301.git",
            "maintenance": false,
            "name": "sample-app-0301",
            "owner": {
              "email": "user-0436@example.com",
              "id": "096370c8-f3ad-4e20-a309-fb4f06ec0a89"
            },
            "region": {
              "id": "7044c05a-0873-42c2-abbe-6841c5481ba7",
              "name": "us"
            },
            "organization": null,
            "space": null,
            "released_at": "2016-10-26T22:50:14Z",
            "repo_size": 1048576,
            "slug_size": null,
            "stack": {
              "id": "5e854079-da33-475b-a209-77f527c0e2fb",
              "name": "cedar-14"
            },
            "updated_at": "2016-10-26T22:50:14Z",
            "web_url": "https://sample-app-0301.herokuapp.com/"
          },
        }
        """
        return f'{self._app_name} has been updated.\n' \
               f'\n' \
               f'App url: {self._web_url}'
