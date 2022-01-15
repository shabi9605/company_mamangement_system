from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.


def apply_leave(request):
    if request.method=="POST":
        leave_form=LeaveForm(request.POST)
        if leave_form.is_valid():
            employe=Register.objects.get(user=request.user)
            lv=Leave(user=request.user,leave_date=leave_form.cleaned_data['leave_date'],reason=leave_form.cleaned_data['reason'],employee=employe)
            lv.save()

            
            return render(request,'leave_form.html',{'msg':'successfully submitted leave'})
        else:
            return HttpResponse("Invalid form")
    leave_form=LeaveForm()
    return render(request,'leave_form.html',{'leave_form':leave_form})


def view_my_leave(request):
    view_leave=Leave.objects.filter(user=request.user)
    return render(request,'view_leave.html',{'view_leave':view_leave})



def view_all_leave(request):
    all_leave=Leave.objects.all().order_by('-date')
    return render(request,'view_leave.html',{'view_leave':all_leave})



def update_leave(request,leave_id):
    leave=Leave.objects.get(id=leave_id)
    print(leave)
    update_leave_form=UpdateLeave(instance=leave)
    if request.method=="POST":
        update_leave_form=UpdateLeave(request.POST,request.FILES,instance=leave)
        update_leave_form.save()
        return redirect('view_all_leave')
    return render(request,'leave_form.html',{'leave_form':update_leave_form})





def my_leave_count(request):
    my_leave=Leave.objects.filter(user=request.user,status='approved').count()
    return render(request,'leave_count.html',{'my_leave':my_leave})