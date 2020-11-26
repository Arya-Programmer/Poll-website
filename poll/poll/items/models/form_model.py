from django.db import models
from django.utils.timezone import now


class Form(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    date = models.DateField(default=now)
    questions = models.ManyToManyField("Question")
    active = models.BooleanField()


    def __str__(self):
        return f"{self.title}"
