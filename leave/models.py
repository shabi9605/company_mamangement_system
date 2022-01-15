from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

from account.models import Register

# Create your models here.

class Leave(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    employee=models.ForeignKey(Register,on_delete=models.CASCADE,null=True,blank=True)
    leave_date=models.DateField(null=True,blank=True)
    
    SICK = 'sick'
    CASUAL = 'casual'
    EMERGENCY = 'emergency'
    STUDY = 'study'

    LEAVE_TYPE = [
        (SICK,'Sick Leave'),
        (CASUAL,'Casual Leave'),
        (EMERGENCY,'Emergency Leave'),
        (STUDY,'Study Leave'),
    ]

    reason=models.CharField(max_length=50,choices=LEAVE_TYPE,default=SICK)
    approved='approved'
    pending='pending'
    reject="reject"
    statuses=[
        (approved,'approved'),
        (pending,'pending'),
        (reject,'reject')
    ]
    status=models.CharField(max_length=30,choices=statuses,default=pending)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user)

