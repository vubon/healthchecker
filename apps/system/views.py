from django.shortcuts import render
from django.views import View

from apps.system.models import System


class ResourceView(View):
    template_name = "system-status.html"

    def get(self, request):
        services = System.objects.all().values("name", "status", "config")
        return render(request, template_name=self.template_name, context={"services": services})
