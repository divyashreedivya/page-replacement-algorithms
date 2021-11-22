from django import forms
from django.utils.safestring import mark_safe

class InputForm(forms.Form):
    seq = forms.CharField(label=mark_safe("Sequence"))
    frames = forms.CharField(label=mark_safe("Frame Size"))