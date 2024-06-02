from django.db import models
from .enums import SplitType
# Create your models here.


class UserModel(models.Model):

    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)
    mobile_no = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ExpenseGroupModel(models.Model):

    group_name = models.CharField(max_length=500)
    users = models.ManyToManyField(UserModel,related_name="groups")
    total_amount = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ExpenseModel(models.Model):

    user = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    group = models.ForeignKey(ExpenseGroupModel,on_delete=models.CASCADE)
    amount = models.IntegerField()
    expense_name = models.CharField(max_length=200)
    split_type = models.CharField(max_length=100,choices=SplitType.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ExpenseTxnModel(models.Model):

    expense = models.ForeignKey(ExpenseModel,on_delete=models.CASCADE)
    owes_user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name="owes_user")
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name="user")
    owes_amount = models.IntegerField()
    no_of_people = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
