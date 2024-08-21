from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from list_app.models import Task, Tag


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


class TagListView(generic.ListView):
    model = Tag
    template_name = "list_app/tag_list.html"
    context_object_name = "tags"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("list_app:tag-list")
