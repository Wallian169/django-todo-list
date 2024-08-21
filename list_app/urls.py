from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from list_app.views import (
    index,
    TagListView,
)
urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "list_app"
