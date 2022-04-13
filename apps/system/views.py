from django.shortcuts import render
from django.views import View

from apps.cores.resource_info import SystemHealthChecker
from apps.system.models import System


class ResourceView(View):
    template_name = "system-status.html"

    def get(self, request):
        system_services = SystemHealthChecker()
        redis = system_services.get_redis()
        system = System.objects.filter(name__iexact=redis.name)
        if system.exists():
            system.update(**{"status": redis.status, "config": redis.config})
        else:
            System.objects.create(name=redis.name, status=redis.status, config=redis.config)

        services = System.objects.all().values("name", "status", "config")
        return render(request, template_name=self.template_name, context={"services": services})
