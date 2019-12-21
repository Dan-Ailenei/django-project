from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class {{ cookiecutter.project_name|replace('_', ' ')|title|replace(' ', '') }}User(AbstractUser):
    pass