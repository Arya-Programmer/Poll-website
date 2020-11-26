from django.db import models

# Create your models here.
class Stat(models.Model):
    ip = models.CharField(max_length=255)
    is_valid = models.BooleanField()
    answers = models.TextField()
    poll_id = models.IntegerField()