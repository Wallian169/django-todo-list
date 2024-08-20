from django.urls import path

from list_app.views import (
    index,
)
urlpatterns = [
    path("", index, name="index"),
]

app_name = "list_app"