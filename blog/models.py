from typing import Any
from django.db import models
from django.utils.text import slugify



# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=40)
    slug=models.SlugField(null=True,blank=True ,unique=True, db_index=True, editable=False)
    
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Blog(models.Model):
    book_name=models.CharField(max_length=100)
    writer=models.CharField(max_length=100)
    comment=models.TextField()
    picture=models.ImageField(upload_to='blog_uploads')
    homepage=models.BooleanField(default=False)
    best=models.BooleanField(default=False)
    active=models.BooleanField(default=False)
    slug=models.SlugField(null=False, unique=True, db_index=True, editable=False)
    category=models.ManyToManyField(Category)

    def __str__(self):
        return self.book_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.book_name)
        super().save(*args, **kwargs)