import json

from django.db import DatabaseError, transaction
from django.shortcuts import render
from django.views import View
from django.contrib import messages

from django_celery_beat.models import PeriodicTask, IntervalSchedule

from apps.projects.models import Project, Service


class CreateService(View):
    template_name = 'service/index.html'

    def get(self, request):
        queryset = Project.objects.all().values("id", "name")
        return render(request, template_name=self.template_name, context={"projects": queryset})

    def post(self, request):
        queryset = Project.objects.all().values("id", "name")
        try:
            with transaction.atomic():
                schedule, created = IntervalSchedule.objects.get_or_create(
                    every=int(request.POST.get("interval", 10)),
                    period=IntervalSchedule.SECONDS
                )
                service = Service.objects.create(
                    project=Project.objects.get(pk=1),
                    name=request.POST.get("service_name", "default_task"),
                    interval=request.POST.get("interval", 20),
                    health_url=request.POST.get("service_url")
                )
                periodic = PeriodicTask.objects.create(
                    interval=schedule,  # we created this above.
                    name=request.POST.get("service_name", "default_task"),
                    task='apps.projects.tasks.fetch_data',
                    kwargs=json.dumps({f'{service.pk}': request.POST.get("service_url")})
                )
                if request.POST.get("enable") == "on":
                    periodic.enabled = True
                else:
                    periodic.enabled = False
                periodic.save()
            messages.success(request, "Service Created")
        except DatabaseError:
            pass
        return render(request, template_name=self.template_name, context={"projects": queryset})


class ServiceStatus(View):
    template_name = "service/status.html"

    def get(self, request):
        services = Service.objects.all().values("name", "status", "interval")
        return render(request, self.template_name, {"services": services})
