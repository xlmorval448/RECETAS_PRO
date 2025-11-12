from django import forms

class Autorform(forms.Form):
    nombre = forms.CharField(max_length=60, label='Nombre del autor:')
    edad = forms.IntegerField(max_value=120, required=False, label='Edad:')
    email = forms.EmailField(max_length=50)
    