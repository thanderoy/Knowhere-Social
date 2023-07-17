from django import forms
from .models import Image

class ImageCreateForm(forms.ModelChoiceField):
    class Meta:
        model = Image
        fields = ["title", "url", "description"]
        widgets = {
            "url": forms.HiddenInput,
        }