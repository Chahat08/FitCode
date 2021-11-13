from django.forms import ModelForm, CharField, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import TaskList
from problems.models import Problem

class TaskListForm(ModelForm):
    class Meta:
        model = TaskList
        fields = ['title','problems']

    title = CharField()
    members = ModelMultipleChoiceField(
        queryset=Problem.objects.all(),
        widget=CheckboxSelectMultiple
    )