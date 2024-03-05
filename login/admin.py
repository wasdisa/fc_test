from django.contrib import admin
from .models import users
# Register your models here.
admin.site.register(users)

def __str__(self):
    return self.username.value