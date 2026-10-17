from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Author(User):
    author_name = models.CharField('Author\'s Name', max_length=64)
