from heroku_notifications.config.models import NotificationConfig

from .formatters.ActorFormatter import ActorFormatter
from .formatters.AddonAttachmentFormatter import AddonAttachmentFormatter
from .formatters.AddonFormatter import AddonFormatter
from .formatters.AppFormatter import AppFormatter
from .formatters.BaseFormatter import BaseFormatter
from .formatters.BuildFormatter import BuildFormatter
from .formatters.DynoFormatter import DynoFormatter
from .formatters.FormationFormatter import FormationFormatter
from .formatters.ReleaseFormatter import ReleaseFormatter


class Formatter:
    actor_formatter = ActorFormatter

    addon_attachment_formatter = AddonAttachmentFormatter
    addon_formatter = AddonFormatter
    app_formatter = AppFormatter
    build_formatter = BuildFormatter
    dyno_formatter = DynoFormatter
    formation_formatter = FormationFormatter
    release_formatter = ReleaseFormatter

    formatters_mapping = {
        NotificationConfig.HerokuEntitiesEnum.AddonAttachment: addon_attachment_formatter,
        NotificationConfig.HerokuEntitiesEnum.Addon: addon_formatter,
        NotificationConfig.HerokuEntitiesEnum.App: app_formatter,
        NotificationConfig.HerokuEntitiesEnum.Build: build_formatter,
        NotificationConfig.HerokuEntitiesEnum.Dyno: dyno_formatter,
        NotificationConfig.HerokuEntitiesEnum.Formation: formation_formatter,
        NotificationConfig.HerokuEntitiesEnum.Release: release_formatter,
    }

    def __init__(self, heroku_data: dict):
        self._heroku_data = heroku_data

        self._data = self._heroku_data['data']
        self._actor = self._heroku_data['actor']

        self._action = self._heroku_data['action']
        self._resource = self._heroku_data['resource']

    def format(self) -> str:
        action = NotificationConfig.HerokuEventTypesEnum(self._action)

        formatter = self._get_formatter()

        mapping = {
            NotificationConfig.HerokuEventTypesEnum.Create: formatter.create,
            NotificationConfig.HerokuEventTypesEnum.Update: formatter.update,
            NotificationConfig.HerokuEventTypesEnum.Destroy: formatter.destroy,
        }

        formatter_method = mapping.get(action)
        if not formatter_method:
            raise ValueError(f'Can\'t retrieve formatter for {self._action} action type.')

        message = formatter_method()
        return self.actor_formatter(self._actor).format(message)

    def _get_formatter(self) -> BaseFormatter:
        resource = NotificationConfig.HerokuEntitiesEnum(f'api:{self._resource}')

        formatter = self.formatters_mapping.get(resource)
        if not formatter:
            raise ValueError(f'Can\'t retrieve formatter for {self._resource} resource type.')

        return formatter(self._data)
