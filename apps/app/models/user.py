from django.db import models

from .base_model import BaseModel


# Create your models here.
class User(BaseModel):
    user = None
    user_edit = None
    name = models.CharField(max_length=250)
    chat_id = models.CharField(max_length=50)

    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'auth\".\"users'
