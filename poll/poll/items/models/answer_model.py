from django.db import models


class Answer(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
