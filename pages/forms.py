from django import forms
from .models import Robot


class RobotForm(forms.ModelForm):
    class Meta:
        model = Robot
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name of the Robot'}),
            'host': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Hostname or IP Address of the Robot'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'serial_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Robot Serial No'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }
