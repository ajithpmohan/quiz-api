from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    # user = models.ForeignKey(
    #     User,
    #     related_name='%(app)s_%(class)s',
    #     on_delete=models.CASCADE
    # ) #WIP
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
