"""
Django metadata for the Components Django application.
"""
from django.apps import AppConfig


class ComponentsConfig(AppConfig):
    """
    Configuration for the Components Django application.
    """

    name = "openedx_learning.apps.authoring.components"
    verbose_name = "Learning Core > Authoring > Components"
    default_auto_field = "django.db.models.BigAutoField"
    label = "oel_components"

    def ready(self) -> None:
        """
        Register Component and ComponentVersion.
        """
        from ..publishing.api import register_publishable_models  # pylint: disable=import-outside-toplevel
        from .models import Component, ComponentVersion  # pylint: disable=import-outside-toplevel

        register_publishable_models(Component, ComponentVersion)
