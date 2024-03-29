from django import forms

from .models import Logger


class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'example@example.com'}),
            'message': forms.TextInput(attrs={'placeholder': 'Enter message'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
  
   
  