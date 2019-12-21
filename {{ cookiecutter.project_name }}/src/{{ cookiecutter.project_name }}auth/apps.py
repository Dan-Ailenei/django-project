from django.apps import AppConfig

class {{ cookiecutter.project_name |replace('_', ' ')|title|replace(' ', '')}}AuthConfig(AppConfig):
    name = '{{ cookiecutter.project_name }}_auth'
