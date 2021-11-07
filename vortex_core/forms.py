from django import forms
from .models import Briefing


class BriefingForm(forms.ModelForm):
    class Meta:
        model = Briefing
        fields = '__all__'