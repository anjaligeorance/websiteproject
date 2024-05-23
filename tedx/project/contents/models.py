from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class table2(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    Physics=models.SmallIntegerField(null=True)
    Chemistry=models.SmallIntegerField(null=True)
    Maths=models.SmallIntegerField(null=True)


class table1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
    student_id=models.CharField(max_length=300,null=True)
    name=models.CharField(max_length=300,null=True)
    phone_no=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    