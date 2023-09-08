from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PromptData(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.TextField(blank=True)

    def __str__(self):
        return self.data

    # list_display = Admin._meta.get_all_field_names()
