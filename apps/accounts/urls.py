from django.urls import path

from apps.accounts.views import Login, Logout, ServiceStatus

urlpatterns = [
    path("", ServiceStatus.as_view(), name="open_status"),
    path("accounts/login/", Login.as_view(), name="login"),
    path("accounts/logout/", Logout.as_view(), name="logout")
]
