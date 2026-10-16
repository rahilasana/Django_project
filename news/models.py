from django.db import models

# Create your models here.

from tinymce.models import HTMLField  

# TinyMCE provides a rich-text editor for formatting news content.


class News(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField() # here is the tiny-mc editor
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# products model
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.name