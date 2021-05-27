from django.urls import path

from apps.projects.views import CreateService, ServiceStatus

urlpatterns = [
    path('service/create/', CreateService.as_view(), name='service_create'),
    path('service/status/', ServiceStatus.as_view(), name='service_status'),
]
