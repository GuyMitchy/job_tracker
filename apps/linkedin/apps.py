from django.apps import AppConfig

class LinkedInConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.linkedin'
    verbose_name = 'LinkedIn'

    def ready(self):
        try:
            import apps.linkedin.signals  # noqa F401
        except ImportError:
            pass 