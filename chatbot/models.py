from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PromptData(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.TextField(blank=True)
    output = models.TextField(blank=True)

    def __str__(self):
        return self.output

    # list_display = Admin._meta.get_all_field_names()
