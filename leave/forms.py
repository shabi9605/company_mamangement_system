from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class LeaveForm(forms.ModelForm):
    leave_date=forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model=Leave
        fields=('leave_date','reason')



class UpdateLeave(forms.ModelForm):
    class Meta:
        model=Leave
        fields=('status',)