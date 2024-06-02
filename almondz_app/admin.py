from django.contrib import admin
from .models import UserModel,ExpenseGroupModel,ExpenseTxnModel,ExpenseModel
# Register your models here.
admin.site.register(UserModel)
admin.site.register(ExpenseGroupModel)
admin.site.register(ExpenseModel)
admin.site.register(ExpenseTxnModel)