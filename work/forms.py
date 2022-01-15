from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class WorkAssignForm(forms.ModelForm):
    class Meta:
        model=Work
        fields=('employee','total_days','description')




class UpdatePercentage(forms.ModelForm):
    class Meta:
        model=Work
        fields=('percentage',)


class UpdateWorkReason(forms.ModelForm):
    class Meta:
        model=Work
        fields=('addition_days','reason')