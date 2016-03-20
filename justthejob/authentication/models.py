from django.db import models


class UserContact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    message=models.CharField(max_length=1000)