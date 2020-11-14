from typing import Dict, Type

from .base import BaseProvider


class ProviderRegistry:
    _registry: Dict[str, Type[BaseProvider]] = dict()

    @classmethod
    def register(cls, provider_class: Type[BaseProvider]) -> Type[BaseProvider]:
        cls._registry.setdefault(provider_class.name, provider_class)
        return provider_class

    @classmethod
    def unregister(cls, provider_name: str) -> None:
        cls._registry.pop(provider_name)

    @classmethod
    def get_provider(cls, provider_name: str) -> BaseProvider:
        provider = cls._registry.get(provider_name)

        if not provider:
            raise ValueError(f'No provider found for {provider_name}.')

        return provider()
