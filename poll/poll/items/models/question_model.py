from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(choices=(("RadioButton", "RadioButton"),("MultiChoice", "MultiChoice"), ("Text", "Text")), max_length=100, default="RadioButton")
    answers = models.ManyToManyField("Answer")

    def __str__(self):
        return f"{self.title}"
