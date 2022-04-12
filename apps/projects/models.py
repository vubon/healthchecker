from django.db import models

from django_celery_beat.models import PeriodicTask

from apps.cores.timestamp import Timestamp


# Create your models here.

class Project(Timestamp):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    descriptions = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.created_at.date()}"

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        db_table = "projects"


class Service(Timestamp):
    STATUS = (
        ("checking", "Checking"),
        ("error", "Error"),
        ("unavailable", "Unavailable"),
        ("ok", "OK")
    )
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, blank=True, null=True)

    name = models.CharField(max_length=100, unique=True)
    health_url = models.URLField(help_text='Health Check URL')
    interval = models.PositiveSmallIntegerField()
    enabled = models.BooleanField(default=True, verbose_name='Enabled',
                                  help_text='Set to False to disable the schedule')

    status = models.CharField(choices=STATUS, default="checking", max_length=20)

    def __str__(self):
        return f"Project: {self.project.name} - Service: {self.name}"

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
