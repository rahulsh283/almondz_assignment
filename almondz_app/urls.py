from django.contrib import admin
from django.urls import path
from .views import UserView,ExpenseGroupView,ExpenseView,GetBalanceForUser

urlpatterns = [
    path("user/", UserView.as_view(), name="User"),
    path("group/", ExpenseGroupView.as_view(), name="group"),
    path("expense/", ExpenseView.as_view(), name="expense"),
    path("getbalance/", GetBalanceForUser.as_view(), name="GetBalanceForUser")
]
