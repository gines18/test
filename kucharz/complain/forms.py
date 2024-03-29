from django import forms

from .models import Complain


class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'example@example.com'}),
            'message': forms.TextInput(attrs={'placeholder': 'Enter message'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
  