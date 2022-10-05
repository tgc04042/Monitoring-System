from django import forms
from .models import humiditysensor

class HumidForm(forms.ModelForm):
    class Meta:
        model = humiditysensor
        fields = ('s_date')