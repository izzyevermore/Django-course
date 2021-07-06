from django import forms
from .models import Participant

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['email']