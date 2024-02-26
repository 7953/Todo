from . models import Task
from  django import forms

class Todo(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']