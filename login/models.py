from django.db import models

class users(models.Model):
    username = models.CharField(max_length=20,verbose_name="username")
    password = models.CharField(max_length=20,verbose_name="password")
    is_superuser = models.BooleanField(default=False,verbose_name="permissions")

def __str__(self):
    return self.username
