from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PromptData(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.data
