from django.urls import path

from apps.projects.views import CreateService, ServiceStatus, ProjectList, CreateProject, ProjectService

urlpatterns = [
    path('project/', ProjectList.as_view(), name='project'),
    path('project/<int:pk>/', ProjectService.as_view(), name='project_view'),
    path('project/create/', CreateProject.as_view(), name='project_create'),
    path('service/create/', CreateService.as_view(), name='service_create'),
    path('service/status/', ServiceStatus.as_view(), name='service_status'),
]
