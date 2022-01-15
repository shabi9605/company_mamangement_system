from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')



def register(request):
    reg=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=ProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()

            reg=True
            return redirect('user_login')

        else:
            HttpResponse('invalid form')
    else:
        user_form=UserForm()
        profile_form=ProfileForm()
       
    return render(request,'register.html',{'register':reg,'user_form':user_form,'profile_form':profile_form})


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        try:
            user1=Register.objects.get(user=user)
        except:
            pass
        if user:
            if user.is_active:
                try:
                    if user1:
                        active=Register.objects.all().filter(user_id=user.id,status=True)
                        if active:
                            login(request,user)
                            return HttpResponseRedirect(reverse('dashboard'))
                        else:
                            return HttpResponse("Waiting for approval")
                except:
                    pass
                try:
                    if user.is_superuser:
                        login(request,user)
                        return HttpResponseRedirect(reverse('dashboard'))
                    else:
                        return HttpResponse("Waiting for approval")
                except:
                    pass
                
            else:
                return HttpResponse('not active')
        else:
            return HttpResponse('Invalid username or password')
    else:
        return render(request,'login.html')




def dashboard(request):
    try:
        profile=Register.objects.get(user=request.user)
        return render(request,'dashboard.html',{'profile':profile})
    except:
        return render(request,'dashboard.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')




def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"YOUR PASSWORD SUCCESSFULLY UPDATED")
            return render(request,'change_password.html')
        else:
            messages.error(request,"PLEASE CORRECT ERROR")
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'change_password.html',{"form":form})



def update_profile(request):
    if request.method=="POST":
        update_form=UpdateForm(request.POST,instance=request.user)
        update_profile_form=UpdateProfileForm(request.POST,instance=request.user.register)
        if update_form.is_valid() and update_profile_form.is_valid():
            update_form.save()
            update_profile_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('dashboard')
    else:
        update_form=UpdateForm(instance=request.user)
        update_profile_form=UpdateProfileForm(instance=request.user.register)
    context={
        'update_form':update_form,
        'update_profile_form':update_profile_form
    }
    return render(request,'update_profile.html',context)



def add_bank_details(request):
    if request.method=="POST":
        bank_form=BankDetailsForm(request.POST)
        if bank_form.is_valid():
            employe=Register.objects.get(user=request.user)
            lv=BankDetails(user=request.user,employee=employe,bank=bank_form.cleaned_data['bank'],branch=bank_form.cleaned_data['branch'],acc_no=bank_form.cleaned_data['acc_no'],ifsc=bank_form.cleaned_data['ifsc'],pan=bank_form.cleaned_data['pan'],status=bank_form.cleaned_data['status'],sdate=bank_form.cleaned_data['sdate'],edate=bank_form.cleaned_data['edate'])
            lv.save()

            
            return render(request,'bank_form.html',{'msg':'successfully submitted leave'})
        else:
            return HttpResponse("Invalid form")
    bank_form=BankDetailsForm()
    return render(request,'bank_form.html',{'form':bank_form})


def view_my_account_details(request):
    my_account=BankDetails.objects.filter(user=request.user)
    return render(request,'my_account.html',{'my_account':my_account})



def add_experience(request):
    if request.method=="POST":
        experience_form=ExperienceForm(request.POST)
        if experience_form.is_valid():
            lv=Experience(employee=experience_form.cleaned_data['employee'],experience=experience_form.cleaned_data['experience'])
            lv.save()
            return render(request,'experience_form.html',{'msg':'successfully submitted leave'})
        else:
            return HttpResponse("Invalid form")
    experience_form=ExperienceForm()
    return render(request,'experience_form.html',{'form':experience_form})


def add_salary(request):
    if request.method=="POST":
        salary_form=SalaryForm(request.POST)
        if salary_form.is_valid():
            lv=Salary(employee=salary_form.cleaned_data['employee'],salary=salary_form.cleaned_data['salary'])
            lv.save()
            return render(request,'salary_form.html',{'msg':'successfully submitted leave'})
        else:
            return HttpResponse("Invalid form")
    salary_form=SalaryForm()
    return render(request,'salary_form.html',{'form':salary_form})




def view_all_salary(request):
    all_salary=Salary.objects.all().order_by('-id')
    return render(request,'view_salary.html',{'salary':all_salary})

def view_my_salary(request):
    my_salary=Salary.objects.filter(employee=request.user.register)
    return render(request,'view_salary.html',{'salary':my_salary})


def view_all_experience(request):
    all_experience=Experience.objects.all().order_by('-id')
    return render(request,'view_experience.html',{'exp':all_experience})


def view_my_experience(request):
    my_experience=Experience.objects.filter(employee=request.user.register)
    return render(request,'view_experience.html',{'exp':my_experience})

