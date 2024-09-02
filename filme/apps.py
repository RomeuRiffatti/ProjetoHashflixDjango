from django.apps import AppConfig

class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'

    def ready(self):
        import filme.signals  # Importe o arquivo de sinais