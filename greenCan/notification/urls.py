from django.urls import path

from . import views

app_name = "notification"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "get-notificatios/",
        views.get_notifications,
        name="get-notificatios",
    ),
]
