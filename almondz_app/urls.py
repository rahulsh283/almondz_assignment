from django.contrib import admin
from django.urls import path
from .views import UserView,ExpenseGroupView,ExpenseView,GetBalanceForUser

# Define URL patterns for the application
urlpatterns = [
    path("user/", UserView.as_view(), name="User"),  # Endpoint to handle user-related operations
    path("group/", ExpenseGroupView.as_view(), name="group"),  # Endpoint to handle expense group-related operations
    path("expense/", ExpenseView.as_view(), name="expense"), # Endpoint to handle expense-related operations
    path("getbalance/", GetBalanceForUser.as_view(), name="GetBalanceForUser") # Endpoint to retrieve balance for a user
]
