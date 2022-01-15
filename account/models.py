from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

# Create your models here.

class Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=PhoneNumberField()
    address=models.TextField()

    employee='employee'
    manager='manager'

    user_types=[
        (employee,'employee'),
        (manager,'manager')
    ]

    user_type=models.CharField(max_length=30,choices=user_types,default=employee)
    status=models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)




class BankDetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    employee=models.ForeignKey(Register,on_delete=models.CASCADE,null=True,blank=True)
    SBI='SBI'
    FEDERAL='FEDERAL'
    UNION='UNION'
    CANARA='CANARA'
    bank_type=[
        (SBI,'SBI'),
        (FEDERAL,'FEDERAL'),
        (UNION,'UNION'),
        (CANARA,'CANARA')
    ]
    bank=models.CharField(max_length=30,choices=bank_type,default=SBI)
    branch=models.CharField(max_length=50)
    acc_no=models.IntegerField()
    ifsc=models.IntegerField()
    pan=models.IntegerField()
    status=models.CharField(max_length=50)
    sdate=models.DateField(default=timezone.now)
    edate=models.DateField(default=timezone.now)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user.username)



class Experience(models.Model):
    employee=models.ForeignKey(Register,on_delete=models.CASCADE,null=True,blank=True)
    experience=models.CharField(max_length=50)
    def __str__(self):
        return str(self.employee.user.username)




class Salary(models.Model):
    employee=models.ForeignKey(Register,on_delete=models.CASCADE,null=True,blank=True)
    salary=models.IntegerField()
    def __str__(self):
        return str(self.employee.user.username)
