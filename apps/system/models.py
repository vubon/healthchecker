from django.db import models

# Create your models here.
from apps.cores.timestamp import Timestamp


class Redis(Timestamp):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    config = models.JSONField()
