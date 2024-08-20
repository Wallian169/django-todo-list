from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from list_app.models import Task


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    context = {
        "tasks": tasks
    }
    return render(
        request=request,
        template_name="index.html",
        context=context
    )
