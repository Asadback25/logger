from django.apps import AppConfig

class LogsConfig(AppConfig):
    name = "log"

    def ready(self):
        import log.signals