from django import forms

from list_app.models import Task, Tag


class TaskForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",  # Use datetime-local for date and time
                "placeholder": "Set a deadline"
            }
        )
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    
    class Meta:
        model = Task
        fields = ["content", "deadline", "done", "tags",]

