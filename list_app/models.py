from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.TextField(
        max_length=255,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(
        null=True,
        blank=True,
    )
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        to=Tag,
        related_name="tasks",
    )

    def __str__(self) -> str:
        return self.content
