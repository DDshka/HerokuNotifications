from .BaseFormatter import BaseFormatter


class BuildFormatter(BaseFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._app_name = self._data['app']['name']
        self._output_stream_url = self._data['output_stream_url']
        self._status = self._data['status']

    def create(self):
        """
        {
          "actor": {
            "email": "username@example.com",
            "id": "7c1e3b25-40a1-416f-91a9-7cd01e517a28"
          },
          "data": {
            "app": {
              "id": "7c9e1f74-ad2c-4daf-91e5-f07bb7cafe90",
              "name": "example-app"
            },
            "buildpacks": null,
            "created_at": "2017-08-23T18:51:37Z",
            "id": "d1315ea5-4885-4288-bc99-a470a005bbcc",
            "output_stream_url": "https://build-output.heroku.com/streams/01234567-89ab-cdef-0123-456789abcdef",
            "release": null,
            "slug": null,
            "source_blob": {
              "checksum": null,
              "url": "https://example.com/source.tgz?token=xyz",
              "version": null
            },
            "stack": "heroku-16",
            "status": "pending",
            "updated_at": "2017-08-23T18:51:37Z",
            "user": {
              "email": "username@example.com",
              "id": "7c1e3b25-40a1-416f-91a9-7cd01e517a28"
            }
          },
        }
        """

        return f'Build started for {self._app_name}.\n' \
               f'\n' \
               f'Build log: {self._output_stream_url}'

    def update(self):
        """
        {
          "actor": {
            "email": "username@example.com",
            "id": "7c1e3b25-40a1-416f-91a9-7cd01e517a28"
          },
          "data": {
            "app": {
              "id": "7c9e1f74-ad2c-4daf-91e5-f07bb7cafe90",
              "name": "example-app"
            },
            "buildpacks": [
              {
                "url": "https://codon-buildpacks.s3.amazonaws.com/buildpacks/heroku/ruby.tgz"
              }
            ],
            "created_at": "2017-08-23T18:51:37Z",
            "id": "d1315ea5-4885-4288-bc99-a470a005bbcc",
            "output_stream_url": "https://build-output.heroku.com/streams/01234567-89ab-cdef-0123-456789abcdef",
            "release": {
              "id": "e3e65aaa-3f63-4ab6-9f7f-9f7aaccf8073",
              "version": 10
            },
            "slug": {
              "id": "7adfdf15-f4a8-429d-bfbf-09d130ee2182",
              "commit": null
            },
            "source_blob": {
              "checksum": null,
              "url": "https://example.com/source.tgz?token=xyz",
              "version": null
            },
            "stack": "heroku-16",
            "status": "succeeded",
            "updated_at": "2017-08-23T18:51:58Z",
            "user": {
              "email": "username@example.com",
              "id": "7c1e3b25-40a1-416f-91a9-7cd01e517a28"
            }
          },
        }
        """

        if self._status == 'succeeded':
             message = f'Build succeeded for {self._app_name}.\n'
        else:
            message = f'Build failed for {self._app_name}.\n'

        message += f'Build log: {self._output_stream_url}'

        return message
