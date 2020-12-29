from .models import Types
from django.forms import ModelForm, TextInput, Textarea


class TypesForm(ModelForm):
    class Meta:
        model = Types
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }