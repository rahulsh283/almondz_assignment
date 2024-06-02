from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = "__all__"


class ExpenseGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpenseGroupModel
        fields = "__all__"



class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpenseModel
        fields = "__all__"


class ExpenseTxnSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExpenseTxnModel
        fields = "__all__"

