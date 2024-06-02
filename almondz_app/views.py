from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .utils import PerUserSpiltAmount,get_per_user_detail
from .models import *
from django.db.models import Count
# Create your views here.

# Api for add user 
class UserView(APIView):

    def post(self,request):
        try:
            data  = request.data
            name = data["name"]
            serializer = UserSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save() 
            status = 200
            res = {
                "error" : False,
                "msg" : f"{name} Added successfully."
            }
        except Exception as e:
            status = 400
            res = {
                "error" : e.args[0],
                "msg" : "Something Went Wrong"
            }
        return Response(res,status)



# Api for create group of user
class ExpenseGroupView(APIView):

    def post(self,request):
        try:
            data  = request.data
            group_name = data['group_name']
            users = data["users"]
            if len(users) >1000:
                raise ValueError("Each expense can not have more than 1000 participants.")
            serializer = ExpenseGroupSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save() 
            status = 200
            res = {
                "error" : False,
                "msg" : f"{group_name} Group Added successfully."
            }
        except Exception as e:
            status = 400
            res = {
                "error" : e.args[0],
                "msg" : "Something Went Wrong"
            }
        return Response(res,status)

# Api for add expense in every user
class ExpenseView(APIView):

    def post(self,request):
        try:
            data  = request.data
            user_id = data["user"]
            group_id = data['group']
            total_amount = data['amount']
            split_type = data['split_type']
            percent_data = data.get('percent_data',[])
            exact_data = data.get('exact_data',[])
            serializer = ExpenseSerializer(data=data)
            if total_amount > 10000000:
                raise ValueError("An expense can not more than INR 1,00,00,000/-")
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                expence_id = serializer.data["id"]
            groupobj = ExpenseGroupModel.objects.annotate(user_count=Count('users')).get(id=group_id)
            user_count = groupobj.user_count
            user_list = groupobj.users.values_list("userId",flat=True)
            expense_txn_array = []
            if split_type == "EQUAL":
                split_amount = PerUserSpiltAmount(split_type,total_amount,user_count)
                for userid in user_list:
                    expense_txn = ExpenseTxnModel(
                        expense_id = expence_id,
                        owes_user_id = userid,
                        user_id = user_id,
                        owes_amount = split_amount
                    )
                    expense_txn_array.append(expense_txn)

            elif split_type == "PERCENT":
                user_totalperson_dict = {}
                for data in percent_data:
                    user_totalperson_dict[data['user_id']] = data['total_person']
                total_count = sum(user_totalperson_dict.values())
                split_amount = PerUserSpiltAmount(split_type,total_amount,total_count)
                for userid in user_list:
                    expense_txn = ExpenseTxnModel(
                        expense_id = expence_id,
                        owes_user_id = userid,
                        user_id = user_id,
                        owes_amount = split_amount*user_totalperson_dict[userid]
                    )
                    expense_txn_array.append(expense_txn)

            elif split_type == "EXACT":
                user_owes_amount_dict = {}
                for data in exact_data:
                    user_owes_amount_dict[data['user_id']] = data['owes_amount']
                amount = sum(user_owes_amount_dict.values())
                if amount!=total_amount:
                    raise ValueError("Total Split Amount must be equal to Total amount")
                for userid in user_owes_amount_dict.keys():
                    expense_txn = ExpenseTxnModel(
                        expense_id = expence_id,
                        owes_user_id = userid,
                        user_id = user_id,
                        owes_amount = user_owes_amount_dict[userid]
                    )
                    expense_txn_array.append(expense_txn)
            ExpenseTxnModel.objects.bulk_create(expense_txn_array)

            status = 200
            res = {
                "error" : False,
                "msg" : "Expense Added successfully."
            }
        except Exception as e:
            status = 400
            res = {
                "error" : True,
                "msg" : e.args[0]
            }
        return Response(res,status)

# Api for get balance of user
class GetBalanceForUser(APIView):

    def get(self,request):
        try:
            user_id = int(request.GET.get("user_id"))  # pass user_id in query params
            data = get_per_user_detail(user_id)

            data["final_taken_amount_from_users"] = dict(data["final_taken_amount_from_users"])
            data["final_given_amount_to_users"] = dict(data["final_given_amount_to_users"])
            status = 200
            res = {
                "error" : False,
                "msg" : "Balance Retrive Successfully.",
                "data" : data
            }
        except Exception as e:
            status = 400
            res = {
                "error" : e.args[0],
                "msg" : "Something Went Wrong"
            }
        return Response(res,status)
