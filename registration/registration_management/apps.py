from django.apps import AppConfig


class RegistrationManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'registration_management'


    def ready(self):
        import registration_management.signals
