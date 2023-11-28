from django.apps import AppConfig


class AntiqueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'antique'

    def ready(self):
        import antique.signals
        
