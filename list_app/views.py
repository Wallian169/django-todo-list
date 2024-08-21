from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from list_app.forms import TaskForm
from list_app.models import Task, Tag


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all().prefetch_related("tags")
    tasks = tasks.order_by("done", "-created_at")
    context = {
        "tasks": tasks,
    }
    return render(
        request=request,
        template_name="list_app/index.html",
        context=context
    )


def toggle_task_done(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(id=pk)
    task.done = not task.done
    task.save()
    return redirect("list_app:index")


def delete_task(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("list_app:index")


def delete_tag(request: HttpRequest, pk: int) -> HttpResponse:
    tag = Tag.objects.get(id=pk)
    tag.delete()
    return redirect("list_app:tag-list")


class TagListView(generic.ListView):
    model = Tag
    template_name = "list_app/tag_list.html"
    context_object_name = "tags"


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("list_app:tag-list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("list_app:tag-list")


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("list_app:index")
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("list_app:index")
    form_class = TaskForm
