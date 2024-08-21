from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from list_app.models import Task


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all().prefetch_related("tags")
    tasks.order_by("-done", "-created_at")
    context = {
        "tasks": tasks,
    }
    return render(
        request=request,
        template_name="list_app/index.html",
        context=context
    )
