from .models import ExpenseModel,ExpenseTxnModel,UserModel
from django.db.models import Sum
# in ExpenseModel store expendature or all user.
# in ExpenseTxnModel store owes_user and deatils of user to give.


def PerUserSpiltAmount(split_type,total_amount,no_of_member):
    per_user_amount = 0
    if split_type == "EQUAL":
        per_user_amount = total_amount/no_of_member
    
    elif split_type == "PERCENT":
        percent = 100/no_of_member
        per_user_amount = (total_amount*percent)/100
    
    return round(per_user_amount,2)


def get_per_user_detail(user_id):

    user_taken_amount = ExpenseTxnModel.objects.filter(user=user_id).values("owes_user","owes_amount")
    user_given_amount = ExpenseTxnModel.objects.filter(owes_user=user_id).values("user","owes_amount")
    expendature = 0
    taken_amount_from_users = {}
    for data in user_taken_amount:
        if data["owes_user"] == user_id:
            expendature+=data['owes_amount']
        else:
            
            if taken_amount_from_users.get(data["owes_user"],0) == 0:
                taken_amount_from_users[data["owes_user"]] = data["owes_amount"]
            else:
                taken_amount_from_users[data["owes_user"]] += data["owes_amount"]

    given_amount_to_users = {}
    for data in user_given_amount:
        if data["user"] == user_id:
            pass
        else:
            if given_amount_to_users.get(data["user"],0) == 0:
                given_amount_to_users[data["user"]] = data["owes_amount"]
            else:
                given_amount_to_users[data["user"]] += data["owes_amount"]

    final_taken_amount_from_users = {}
    final_given_amount_to_users = {}
    final_key = []
    if len(taken_amount_from_users.keys())>= len(given_amount_to_users.keys()):
        final_key = taken_amount_from_users.keys()
    else:
        final_key = given_amount_to_users.keys()

    for key in final_key:
        final_amount = taken_amount_from_users.get(key,0) - given_amount_to_users.get(key,0)
        if final_amount > 0:
            final_taken_amount_from_users[key] = round(final_amount,2)
        elif final_amount < 0:
            final_given_amount_to_users[key] = round(final_amount,2)

        
    taken_username = UserModel.objects.filter(userId__in = final_taken_amount_from_users.keys()).values_list("name",flat=True)
    
    final_taken = list(zip(taken_username,final_taken_amount_from_users.values()))

    given_username = UserModel.objects.filter(userId__in = final_given_amount_to_users.keys()).values_list("name",flat=True)
    final_given = list(zip(given_username,final_given_amount_to_users.values()))
    
    result_data = {
        "expense" : expendature,
        "final_taken_amount_from_users" :final_taken,
        "final_given_amount_to_users" : final_given,
    }
    
    return result_data