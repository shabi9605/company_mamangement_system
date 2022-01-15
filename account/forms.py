from django import forms
from django.forms.widgets import NumberInput
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    username=forms.CharField(help_text=None,label='Username')
    password1=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Confirm Password')
    
    class Meta:
        model=User
        fields=('username','password1','password2','email',)
        labels=('password1','Password','password2','Confirm_Password')

class ProfileForm(forms.ModelForm):
    address=forms.Textarea()
    class Meta:
        model=Register
        fields=('address','phone','user_type')




class UpdateForm(forms.ModelForm):
    username=forms.CharField(help_text=None,label='Username')
    
    class Meta:
        model=User
        fields=('username','email')

class UpdateProfileForm(forms.ModelForm):
    address=forms.Textarea()
    
    class Meta:
        model=Register
        fields=('address','phone')


class BankDetailsForm(forms.ModelForm):
    sdate=forms.DateField(required=True,widget=NumberInput(attrs={'type':'date'}),label='Start Date')
    edate=forms.DateField(required=True,widget=NumberInput(attrs={'type':'date'}),label='End Date')
    class Meta:
        model=BankDetails
        fields=('bank','branch','acc_no','ifsc','pan','status','sdate','edate')




class CustomModelFilter(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s %s" % (obj.user, obj.user_type)



class ExperienceForm(forms.ModelForm):
    employee = CustomModelFilter(queryset=Register.objects.all())
    class Meta:
        model=Experience
        fields=('employee','experience')



class SalaryForm(forms.ModelForm):
    employee = CustomModelFilter(queryset=Register.objects.all())
    class Meta:
        model=Salary
        fields=('employee','salary')