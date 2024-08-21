from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from list_app.views import (
    index,
    TagListView,
    TagUpdateView,
    TagCreateView,
    TaskCreateView,
    TaskUpdateView,
    toggle_task_done
)
urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>", TagUpdateView.as_view(), name="tag-update"),
    path("tags/create-tag/", TagCreateView.as_view(), name="tag-create"),
    path("create-task/", TaskCreateView.as_view(), name="create-task"),
    path("toggle-done/<int:pk>", toggle_task_done, name="toggle-done"),
    path("update-task/<int:pk>", TaskUpdateView.as_view(), name="update-task"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

app_name = "list_app"
