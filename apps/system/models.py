from django.db import models

# Create your models here.
from apps.cores.timestamp import Timestamp


class System(Timestamp):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    config = models.JSONField()

    class Meta:
        verbose_name = "System"
        verbose_name_plural = "systems"

    def __str__(self):
        return f"{self.name} - {self.created_at}"
