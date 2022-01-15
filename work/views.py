from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def assign_work(request):
    if request.method=="POST":
        work_assign_form=WorkAssignForm(request.POST)
        if work_assign_form.is_valid():
            lv=Work(employee=work_assign_form.cleaned_data['employee'],total_days=work_assign_form.cleaned_data['total_days'],description=work_assign_form.cleaned_data['description'])
            lv.save()
            return render(request,'work_form.html',{'msg':'successfully assigned work'})
        else:
            return HttpResponse("Invalid form")
    work_assign_form=WorkAssignForm()
    return render(request,'work_form.html',{'form':work_assign_form})




def view_all_assigned_work(request):
    all_works=Work.objects.all().order_by('-id')
    return render(request,'view_works.html',{'work':all_works})


def view_my_work(request):
    my_work=Work.objects.filter(employee=request.user.register)
    return render(request,'view_works.html',{'work':my_work})


def update_percentage(request,work_id):
    work=Work.objects.get(id=work_id)
    print(work)
    update_work_form=UpdatePercentage(instance=work)
    if request.method=="POST":
        update_work_form=UpdatePercentage(request.POST,request.FILES,instance=work)
        update_work_form.save()
        return redirect('view_my_work')
    return render(request,'work_form.html',{'form':update_work_form})



def update_work_additiondays(request,work_id):
    work=Work.objects.get(id=work_id)
    print(work)
    update_work_reason_form=UpdateWorkReason(instance=work)
    if request.method=="POST":
        update_work_reason_form=UpdateWorkReason(request.POST,request.FILES,instance=work)
        update_work_reason_form.save()
        return redirect('view_my_work')
    return render(request,'work_form.html',{'form':update_work_reason_form})