from django.apps import AppConfig


class AlmondzAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'almondz_app'

    def ready(self):
        from jobs import updater
        updater.start()
        return super().ready()
