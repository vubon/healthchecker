from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from apps.projects.models import Service


class Login(View):
    template_name = "account/index.html"

    def get(self, request):
        return render(request, template_name=self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("project")
        else:
            messages.add_message(request, messages.WARNING, "Check your username or password")
            return render(request, self.template_name)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("open_status")


class ServiceStatus(View):
    template_name = "public/service-status.html"

    def get(self, request):
        services = Service.objects.all().values("name", "is_activate", "interval", "enabled")
        return render(request, self.template_name, {"services": services})
