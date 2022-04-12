from django.urls import path

from apps.system.views import ResourceView

urlpatterns = [
    path('system/status/', ResourceView.as_view(), name='system_status'),
]
