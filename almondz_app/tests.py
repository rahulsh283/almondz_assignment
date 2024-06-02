from django.test import TestCase

# Create your tests here.


import csv

data = {
    'expense': 0,
    'final_taken_amount_from_users': [('atul', 500), ('manish', 250)],
    'final_given_amount_to_users': [('rahul', -800)]
}


csv_file_path = 'output.csv'

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(['Type', 'Name', 'Amount'])
    writer.writerow(['expense', '', data['expense']])
    
    for name, amount in data['final_taken_amount_from_users']:
        writer.writerow(['final_taken_amount_from_users', name, amount])
    
    for name, amount in data['final_given_amount_to_users']:
        writer.writerow(['final_given_amount_to_users', name, amount])

