from django.apps import AppConfig


class HerokuDeployConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'heroku_deploy'
