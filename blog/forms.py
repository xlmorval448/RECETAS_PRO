from django import forms
from .models import Autor

class Autorform(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','edad','email']