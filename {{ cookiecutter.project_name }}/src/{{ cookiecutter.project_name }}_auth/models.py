from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class {{ cookiecutter.project_name|replace('_', ' ')|title|replace(' ', '') }}User(AbstractUser):
    pass