from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for UserModel.
    """ 

    class Meta:
        model = UserModel
        fields = "__all__"


class ExpenseGroupSerializer(serializers.ModelSerializer):
    """
    Serializer for ExpenseGroupModel.
    """
    class Meta:
        model = ExpenseGroupModel
        fields = "__all__"



class ExpenseSerializer(serializers.ModelSerializer):
    """
    Serializer for ExpenseModel.
    """

    class Meta:
        model = ExpenseModel
        fields = "__all__"


class ExpenseTxnSerializer(serializers.ModelSerializer):
    """
    Serializer for ExpenseTxnModel.
    """
    class Meta:
        model = ExpenseTxnModel
        fields = "__all__"

