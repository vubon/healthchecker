from django.contrib import admin

from apps.projects.models import Project, Service

admin.site.register(Project)
admin.site.register(Service)
