from django import forms
from .models import Task, Tag

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline_datetime', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'deadline_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
