from django.db import models
from django.contrib import admin

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created  = models.DateField()
    updated = models.DateField()
class Comment(models.Model):
    body = models.TextField()
    author = models.CharField(max_length=60)
    created = models.DateField()
    updated = models.DateField()
    post = models.ForeignKey(Post)        
admin.site.register(Post)
admin.site.register(Comment)
