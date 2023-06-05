from django.apps import AppConfig


class GoPlacesConfig(AppConfig):
    name = "goplaces"
    verbose_name = "App"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self) -> None:
        # Hack to fix the name of the auth app in the django-admin.
        from django.contrib.auth.apps import AuthConfig
        AuthConfig.verbose_name = "Users"

        return super().ready()
