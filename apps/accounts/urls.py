from django.urls import path

from apps.accounts.views import Login

urlpatterns = [
    path("", Login.as_view())
]
