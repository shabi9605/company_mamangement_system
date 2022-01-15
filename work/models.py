from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

from account.models import Register
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.


class Work(models.Model):
    employee=models.ForeignKey(Register,on_delete=models.CASCADE,null=True,blank=True)
    percentage=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],null=True,blank=True)
    total_days=models.IntegerField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    addition_days=models.IntegerField(null=True,blank=True)
    reason=models.TextField(null=True,blank=True)
    def __str__(self):
        return str(self.employee.user.username)
