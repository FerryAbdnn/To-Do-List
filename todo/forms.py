from django import forms
from .models import Todo
from django.contrib.auth.forms import AuthenticationForm

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task', 'completed']
