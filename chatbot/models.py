from django.db import models

# Create your models here.
class PromptData(models.Model):
    username = models.CharField(max_length=16)
    prompt = models.CharField(max_length=280)

    def __str__(self):
        return self.prompt
