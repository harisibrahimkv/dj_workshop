from django.db import models

# Create your models here.

class Tweet(models.Model):
    hashtag = models.CharField(max_length=85)
    author = models.CharField(max_length=85)
    created_at = models.DateTimeField()
    text = models.CharField(max_length=225)
