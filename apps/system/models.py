from django.db import models

# Create your models here.
from apps.cores.timestamp import Timestamp


class System(Timestamp):
    name = models.CharField(max_length=100, db_index=True, unique=True)
    status = models.BooleanField(default=False)
    config = models.JSONField(null=True, blank=True)
    service_name = models.CharField(max_length=100, blank=True, null=True, db_index=True)

    class Meta:
        verbose_name = "System"
        verbose_name_plural = "systems"

    def __str__(self):
        return f"{self.name} - {self.created_at}"
