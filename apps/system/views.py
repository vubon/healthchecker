from django.shortcuts import render
from django.views import View

from apps.cores.resource_info import SystemHealthChecker
from apps.system.models import Redis


class ResourceView(View):
    template_name = "system-status.html"

    def get(self, request):
        system_services = SystemHealthChecker()
        redis = system_services.get_redis()
        Redis.objects.create(name=redis.name, status=redis.status, config=redis.config)
        services = Redis.objects.all().values("name", "status", "config")
        return render(request, template_name=self.template_name, context={"services": services})
