from django.db import models
from users.models import Author

# Create your models here.

class Category(models.Model):
    name = models.CharField('Name', max_length=64)
    slug = models.SlugField('Slug')

class Blog(models.Model):
    title = models.CharField('Title', max_length=64)
    slug = models.SlugField('Slug')
    text = models.TextField('Text', max_length=512)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)
    published = models.BooleanField('Published')
